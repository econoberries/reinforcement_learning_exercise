# Review of uploaded written homework (visual check)

## Homework 1: `homework1_msolution.pdf` (2 pages)

The handwritten solution distinguishes the two deterministic policies by the
alternating two-step reward cycle. Their infinite-horizon values are:

- `V_left = 1 / (1 - gamma^2)`
- `V_right = 2*gamma / (1 - gamma^2)`

Thus left is preferred at `gamma=0`, both tie at `gamma=0.5`, and right is
preferred at `gamma=0.9`. The written table reports 1.00 vs 0.00,
1.33 vs 1.33, and 5.26 vs 9.47, respectively.

For the random-policy Monte Carlo task, the handwritten solution gives
MazeGrid sample mean around `0.0022` and SD about `0.012` with `10,000`
episodes. With a 95% normal approximation, the approximate required
sample size is `(1.96*sigma/epsilon)^2`; the handwritten answer rounds
this to approximately 3,743 or 4,000 episodes for `epsilon=0.0004`.
For DiscountGrid at `gamma=0.95` the handwritten mean is about `-6.37`
and SD about `3.768`, leading to a sample-size estimate on the order
of 5,500–5,700 episodes for `epsilon=0.1` (rounded to 6,000).

**Code audit:** the selected HW1 `m_solution` script retains a fixed
`meanwithin=0.1` even for MazeGrid, so do not interpret its reported
required `n` for MazeGrid without changing the precision to `0.0004`.

## Homework 2: `homework2_part1.pdf` (1 page)

The handwritten 4×4-gridworld state-action values read:

- `q_pi(11, down) = -1`
- `q_pi(7, down) = -15`
- `q_pi(9, left) = -21`

The solution expresses `v*(s) = max_a q*(s,a)` and the policy as
`argmax_a q*(s,a)`. It also outlines substituting `v_pi(s')`
with `sum_a' pi(a'|s') q_pi(s',a')` in the Bellman expectation equation.

## Homework 2: `hw2_part2_part3` Google document

The uploaded write-up reports for MazeGrid, discount 0.9 and noise 0.2:

- 100-step value-iteration estimate: `0.282195`
- Average sampled return with 10 episodes: `0.261735`
- Average sampled return with 10,000 episodes: `0.283002`

The empirical average approaches the computed expected value as the number
of episodes grows; the policy is not updated by those episodes.

These figures record the user's source materials; Monte Carlo results
vary between independent runs. The numerical code snapshots were smoke tested,
not exhaustively graded against the course specification.
