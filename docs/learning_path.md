# Reinforcement Learning learning path

| | HW1 | HW2 | HW3 |
|---|---|---|---|
| Agent | Random | Value iteration | Policy iteration |
| Learning/planning input | Observed episode returns | Full known MDP | Full known MDP |
| Objective | Evaluate fixed random policy | Optimize action choice | Optimize via policy evaluation and improvement |
| Fundamental equation | `G_t = R_(t+1) + gamma * G_(t+1)` | `V_(k+1)(s) = max_a sum_s' P(s'|s,a)[r + gamma V_k(s')]` | `V^pi(s) = sum_a pi(a|s) sum_s' P(s'|s,a)[r + gamma V^pi(s')]` |

## Tutorial 2 (five pages)

MDP tuple `(S, A, P, R, gamma)` and a small four-state example; solve
Bellman optimality via value iteration and extract the greedy policy.

## Tutorial 3 (seven pages)

Monte Carlo estimation from observed rollouts, average returns from each
state visit, and temporal-difference updates:
`V(S_t) <- V(S_t) + alpha * [R_(t+1) + gamma V(S_(t+1)) - V(S_t)]`.

## Conceptual distinction

- HW1 is **sample-based policy evaluation** (random actions, observed rollouts).
- HW2 uses **dynamic programming with full transition knowledge**, not
  trial-and-error reinforcement learning.
- HW3 is another **planning algorithm** for known MDPs. TD(lambda) in the
  theoretical question connects to the sample-based RL methods in the tutorial,
  but is **not** the algorithm requested for Q3.

**Preterminal nuance:** entering a reward-labelled Gridworld square does not
end an episode. An additional `exit` action transitions to the actual terminal
state and yields that reward. This affects the number of iterations needed for
reward information to propagate backward.
