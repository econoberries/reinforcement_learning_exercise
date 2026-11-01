# Drive materials: file and version audit (1 November 2026)

Source folder: https://drive.google.com/drive/folders/1DmU6sHs4NqCFOZ8c8U2MZwvkf2nxhGqr

**Course texts located:** Homework Sheets 1, 2 and 3; Tutorial 02 and Tutorial
03; `homework2_part1.pdf`, `hw2_part2_part3` write-up, and a Homework 1
handwritten solution PDF. The handwritten HW1 (two pages) and HW2 Part 1 (one page) files were
also visually reviewed; they were not reproduced in this repository.

**Zipped versions inspected:**

- HW1 starter `1_gridworld_explore.zip` — 9 Python files.
- `1_gridworld_explore_solution.zip` — 9 Python files; returns + mean but no
  SD output in that reference snapshot.
- HW2 starter `2_gridworld.zip` — 9 Python files plus 1,500+ IDE/virtualenv
  archive entries; virtualenv and IDE metadata deliberately excluded.
- `2_gridworld_value-iteration_solution.zip` — 9 Python files plus readme,
  has a NumPy-based reference implementation and a `getCustomGrid()` example.
- HW3 `2_gridworld.zip` — 9 Python files, with ValueIterationAgent reset to TODOs.

**Separately uploaded code:** `homework_1/k_solution/gridworld.py` (uses a
`dataclass` to track individual discounted rewards),
`homework_1/m_solution/gridworld.py` (scalar discounted return, mean and SD);
`homework_2/agent.py` (value iteration); `homework_2/gridworld.py`
(HW1-style return collection). This repository chooses `m_solution` for HW1
and the two standalone files for HW2 as its student-side snapshots. Reference
solutions are not published or copied into the project.

**Verified code differences:**

- HW1 modifies `runEpisode()` to accumulate `reward * gamma**step` and
  reports mean/SD across episodes.
- HW2 adds synchronous Bellman-optimality sweeps and Q/value/policy getters
  in `ValueIterationAgent`.
- The HW3 starter is not a cumulative finished version: it reintroduces
  unimplemented value iteration methods. Carry forward HW2 instead.
- Actual standalone HW2 `gridworld.py` does not include `getCustomGrid`
  despite the custom-grid discussion in the written answers.
- Both HW1 and HW2 standalone gridworld scripts have an imprecise/confusing
  hard-coded CLT tolerance of 0.1, which is not appropriate to HW1 MazeGrid's
  requested precision of 0.0004.
- HW2's standalone value-iteration implementation printed every possible
  transition in every iteration. Two debugging lines have been removed in
  this repository, leaving the Bellman computation unchanged.
