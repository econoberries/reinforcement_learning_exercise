# Homework 2 — Bellman optimality and value iteration

**Assignment date:** 20 October 2026. **Due:** 27 October 2026, 14:00.

- Q1: compute state-action values in a 4x4 episodic gridworld and derive
  Bellman/policy expressions.
- Q2.2: implement synchronous value iteration in `agent.py`.
- Q2.3: design a custom grid and investigate `noise`, `discount`, and
  `livingReward`.

**Code:** the two standalone `agent.py` and `gridworld.py` files from the HW2
Drive folder override the starter zip. Two verbose debugging prints in
`ValueIterationAgent` were removed; the numerical algorithm is unchanged.

**Run:** `cd gridworld && python3 gridworld.py -g MazeGrid -a value -i 100 -k 10 -t -q`

**Benchmark recorded in written work:** MazeGrid value-iteration result
0.282195; empirical returns for 10 and 10,000 episodes are 0.261735 and
0.283002 respectively. Individual sampled returns vary without a seed.

**Audit note:** The custom `BowlingGrid` / `CustomGrid` referenced in the
HW2 write-up was **not found in the separate student `gridworld.py`** in
Drive. It occurs in a different reference archive but should be reconciled
before marking Q2.3 finished. The CLI also reports estimated required
sample size using a fixed 0.1 tolerance carried over from HW1.
