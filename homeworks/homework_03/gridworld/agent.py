import util, random
from gridworldClass import Gridworld


class Agent:

  def getAction(self, state):
    """
    For the given state, get the agent's chosen
    action.  The agent knows the legal actions
    """
    abstract

  def getValue(self, state):
    """
    Get the value of the state.
    """
    abstract

  def getQValue(self, state, action):
    """
    Get the q-value of the state action pair.
    """
    abstract

  def getPolicy(self, state):
    """
    Get the policy recommendation for the state.

    May or may not be the same as "getAction".
    """
    abstract

  def update(self, state, action, nextState, reward):
    """
    Update the internal state of a learning agent
    according to the (state, action, nextState)
    transistion and the given reward.
    """
    abstract


class RandomAgent(Agent):
  """
  Clueless random agent, used only for testing.
  """

  def __init__(self, actionFunction):
    self.actionFunction = actionFunction

  def getAction(self, state):
    return random.choice(self.actionFunction(state))

  def getValue(self, state):
    return 0.0

  def getQValue(self, state, action):
    return 0.0

  def getPolicy(self, state):
    return 'random'

  def update(self, state, action, nextState, reward):
    pass


################################################################################
# Exercise 2

class ValueIterationAgent(Agent):

  def __init__(self, mdp: Gridworld, discount = 0.9, iterations = 100):
    """
    Your value iteration agent should take a mdp on
    construction, run the indicated number of iterations
    and then act according to the resulting policy.
    """
    self.mdp = mdp
    self.discount = discount
    self.iterations = iterations

    values = {state: 0.0 for state in mdp.getStates()}
    for _ in range(iterations):
      buffer = values.copy()

      for state in mdp.getStates():
        actions = mdp.getPossibleActions(state)

        if not actions:
          continue

        q_values = []

        for action in actions:
          q = 0.0

          for next_state, probability in mdp.getTransitionStatesAndProbs(state, action):
            reward = mdp.getReward(state, action, next_state)
            q+= probability * (reward + discount * values[next_state])

          q_values.append(q)

        buffer[state] = max(q_values)

      values = buffer

    self.values = values



  def getValue(self, state):
    """
    Look up the value of the state (after the indicated
    number of value iteration passes).
    """
    return self.values[state]



  def getQValue(self, state, action):
    """
    Look up the q-value of the state action pair
    (after the indicated number of value iteration
    passes).  Note that value iteration does not
    necessarily create this quantity and you may have
    to derive it on the fly.
    """
    q_value = 0.0

    for next_state, probability in self.mdp.getTransitionStatesAndProbs(state, action):
        reward = self.mdp.getReward(state, action, next_state)

        q_value += probability * (
            reward + self.discount * self.values[next_state]
        )

    return q_value



  def getPolicy(self, state):
    """
    Look up the policy's recommendation for the state
    (after the indicated number of value iteration passes).
    """

    return self.getAction(state)



  def getAction(self, state):
    """
    Return the action recommended by the policy.
    """
    actions = self.mdp.getPossibleActions(state)

    if not actions:
      return None

    best_action = actions[0]
    for action in actions:
      if self.getQValue(state, action) > self.getQValue(state, best_action):
        best_action = action
    return best_action


  def update(self, state, action, nextState, reward):
    """
    Not used for value iteration agents!
    """

    pass


################################################################################
# Homework 3: Policy Iteration (work in progress)

class PolicyIterationAgent(Agent):
  """Evaluate a policy, improve it, and repeat until it stops changing."""

  def __init__(self, mdp, discount=0.9, iterations=100):
    self.mdp = mdp
    self.discount = discount
    self.values = {state: 0.0 for state in mdp.getStates()}

    # Start by choosing the first available action in each state.
    self.policy = {}
    for state in mdp.getStates():
      actions = mdp.getPossibleActions(state)
      if actions:
        self.policy[state] = actions[0]

    self.rounds = 0
    self.start_values_by_round = []
    stable = False

    for _ in range(iterations):
      # 1. Evaluate the current policy.
      self.evaluate_policy()
      self.rounds += 1
      self.start_values_by_round.append(self.getValue(mdp.getStartState()))

      # 2. Improve the policy.
      stable = True
      for state, old_action in self.policy.items():
        best_action = old_action
        best_q = self.getQValue(state, old_action)
        for action in mdp.getPossibleActions(state):
          q = self.getQValue(state, action)
          if q > best_q + 1e-12:
            best_action, best_q = action, q
        if best_action != old_action:
          self.policy[state] = best_action
          stable = False

      # 3. Stop if no action changes.
      if stable:
        break

    # Ensure the values match the final policy if the iteration limit was hit.
    if self.rounds > 0 and not stable:
      self.evaluate_policy()

  def evaluate_policy(self):
    """Repeat Bellman expectation updates until values stabilize."""
    for _ in range(10000):
      new_values = self.values.copy()
      for state, action in self.policy.items():
        new_values[state] = self.getQValue(state, action)
      change = max(abs(new_values[s] - self.values[s]) for s in self.values)
      self.values = new_values
      if change < 1e-12:
        return
    raise RuntimeError("Policy evaluation did not converge")

  def getValue(self, state):
    return self.values[state]

  def getQValue(self, state, action):
    q = 0.0
    for next_state, probability in self.mdp.getTransitionStatesAndProbs(state, action):
      reward = self.mdp.getReward(state, action, next_state)
      q += probability * (reward + self.discount * self.values[next_state])
    return q

  def getPolicy(self, state):
    return self.policy.get(state)

  def getAction(self, state):
    return self.getPolicy(state)

  def update(self, state, action, nextState, reward):
    pass


################################################################################
# Below can be ignored for Exercise 2

class QLearningAgent(Agent):

  def __init__(self, actionFunction, discount = 0.9, learningRate = 0.1, epsilon = 0.2):
    """
    A Q-Learning agent gets nothing about the mdp on
    construction other than a function mapping states to actions.
    The other parameters govern its exploration
    strategy and learning rate.
    """
    self.setLearningRate(learningRate)
    self.setEpsilon(epsilon)
    self.setDiscount(discount)
    self.actionFunction = actionFunction

    raise "Your code here."




  # THESE NEXT METHODS ARE NEEDED TO WIRE YOUR AGENT UP TO THE CRAWLER GUI

  def setLearningRate(self, learningRate):
    self.learningRate = learningRate

  def setEpsilon(self, epsilon):
    self.epsilon = epsilon

  def setDiscount(self, discount):
    self.discount = discount

  # GENERAL RL AGENT METHODS

  def getValue(self, state):
    """
    Look up the current value of the state.
    """

    raise ValueError("Your code here.")



  def getQValue(self, state, action):
    """
    Look up the current q-value of the state action pair.
    """

    raise ValueError("Your code here.")



  def getPolicy(self, state):
    """
    Look up the current recommendation for the state.
    """

    raise ValueError("Your code here.")



  def getAction(self, state):
    """
    Choose an action: this will require that your agent balance
    exploration and exploitation as appropriate.
    """

    raise ValueError("Your code here.")



  def update(self, state, action, nextState, reward):
    """
    Update parameters in response to the observed transition.
    """

    raise ValueError("Your code here.")
