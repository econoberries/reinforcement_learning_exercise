# Homework 1 — Return estimation

**Assignment date:** 13 October 2026. **Due:** 20 October 2026, 14:00.

- Q1: compare two deterministic policies by their discounted returns.
- Q2.1: inspect the Gridworld interface and transition noise.
- Q2.2: implement episode return and mean/standard deviation from the random
  policy, then use the CLT to estimate required sample sizes.

**Code:** `gridworld/gridworld.py` is the `m_solution` file provided in Drive;
the other eight `.py` files are from the original HW1 starter archive.

**Run:** `cd gridworld && python3 gridworld.py -g MazeGrid -k 10000 -t -q`

**Audit note:** The supplied code computes population SD (divide by N) and
hard-codes a confidence tolerance of `0.1` irrespective of grid. For the
MazeGrid CI exercise the question asks for a much smaller tolerance,
`0.0004`: substitute that value before interpreting the printed sample-size
calculation. Keep the original solution unmodified for now.

**Do not confuse:** a Monte Carlo sample mean of returns under a *random
policy* with the optimal expected value computed in HW2.
