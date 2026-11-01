# Homework 3 — TD(lambda) and policy iteration

**Assignment date:** 27 October 2026. **Due:** 3 November 2026, 14:00.

- Q1: distinguish MRP and MDP, and explain the fixed-policy relation.
- Q2: derive the recursion for an n-step return and a lambda-return.
- Q3: create `PolicyIterationAgent`, compare number of rounds before
  MazeGrid start value becomes nonzero and the convergence behavior under
  default versus zero noise; discuss policy iteration vs. value iteration.

## Why the HW3 folder inherits HW2

The official HW3 archive uses the HW2 codebase but resets the ValueIterationAgent
methods to `raise ValueError("Your code here.")`. Copying it on top of the HW2
working folder would destroy the previous assignment. This folder therefore
starts with your HW2 working solution plus an explicit HW3 class skeleton.

`-a policy` is registered, but **policy iteration is NOT implemented yet**.
The class raises `NotImplementedError` to keep incompleteness obvious.

## How we will develop it

1. Choose an initial policy over nonterminal states.
2. Evaluate that fixed policy (Bellman expectation updates).
3. Improve by selecting the action maximizing q under the evaluated values.
4. Repeat until unchanged; record rounds and optionally evaluation sweeps.
5. Compare results under `-n 0.2` and `-n 0.0`.

**Run existing value agent**:
`cd gridworld && python3 gridworld.py -g MazeGrid -a value -i 100 -k 10 -t -q`
