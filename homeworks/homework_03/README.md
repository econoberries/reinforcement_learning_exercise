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

The CLI option `-a policy` is registered and `PolicyIterationAgent` is implemented.
`-i` counts **policy-evaluation + policy-improvement rounds**, not individual
Bellman value sweeps. Each policy evaluation uses synchronous backups until
the largest value change is below `1e-12`.

We initialize a deterministic policy with the first available action (usually
`north`), evaluate it, then greedily improve it. If the last improvement occurs
at the `-i` limit, the new policy is evaluated once more so the displayed values
are consistent with it.

For HW3 3(b)/(c), instantiate `PolicyIterationAgent` from Python and inspect:
- `rounds`: evaluation + improvement rounds performed (including stable round)
- `converged`: whether the policy reached stability
- `start_values_by_round`: start-state values **before each improvement step**
- `policy_changes_by_round`: number of policy changes in each round

A round here always means **one complete policy evaluation and one greedy
improvement**, not one inner Bellman sweep. Use the recorded values when
counting the first evaluation where the start state becomes nonzero.

## How we will develop it

1. Choose an initial policy over nonterminal states.
2. Evaluate that fixed policy (Bellman expectation updates).
3. Improve by selecting the action maximizing q under the evaluated values.
4. Repeat until unchanged; record rounds and optionally evaluation sweeps.
5. Compare results under `-n 0.2` and `-n 0.0`.

**Run existing value agent**:
`cd gridworld && python3 gridworld.py -g MazeGrid -a value -i 100 -k 10 -t -q`


**Run policy iteration**:
`cd gridworld && python3 gridworld.py -g MazeGrid -a policy -i 100 -k 0 -t -q`

**Compare against value iteration**:
`python3 gridworld.py -g MazeGrid -a value -i 100 -k 0 -t -q`

**Reproduce the measurements for 3(b) and 3(c)**:
`python3 homeworks/homework_03/run_policy_experiments.py` (from repository root).
