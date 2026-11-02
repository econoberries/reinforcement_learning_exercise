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
  """Update values using the Bellman optimality equation."""

  def __init__(self, mdp, discount=0.9, iterations=100):
    self.mdp = mdp
    self.discount = discount
    self.values = {state: 0.0 for state in mdp.getStates()}

    # Repeat the value iteration update.
    for _ in range(iterations):
      new_values = self.values.copy()
      for state in mdp.getStates():
        actions = mdp.getPossibleActions(state)
        if actions:
          new_values[state] = max(self.getQValue(state, action) for action in actions)
      self.values = new_values

  def getValue(self, state):
    return self.values[state]

  def getQValue(self, state, action):
    q = 0.0
    for next_state, probability in self.mdp.getTransitionStatesAndProbs(state, action):
      reward = self.mdp.getReward(state, action, next_state)
      q += probability * (reward + self.discount * self.values[next_state])
    return q

  def getPolicy(self, state):
    actions = self.mdp.getPossibleActions(state)
    if not actions:
      return None

    best_action = actions[0]
    for action in actions:
      if self.getQValue(state, action) > self.getQValue(state, best_action):
        best_action = action
    return best_action

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
