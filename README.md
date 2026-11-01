# Reinforcement Learning: Gridworld Homework Portfolio

Course: **Reinforcement Learning, WS 2026/27, University of Tübingen**.

A private learning repository with a **separate runnable snapshot for each homework**.
The code evolves from estimating returns (HW1), to model-based value iteration
(HW2), to policy iteration (HW3, not implemented yet).

> **Keep this repository PRIVATE.** The course code appears adapted from the
> Berkeley CS188 Gridworld/Pacman educational material. A publicly accessible
> Berkeley version explicitly disallows distributing/publishing solutions.
> The adapted coursework's redistribution rules should be confirmed with the
> teaching staff before publishing code, solution PDFs, or assignment sheets.
> See `docs/provenance.md`.

## Learning progression

| Homework | Main topic | Coding status | Main code |
|---|---|---|---|
| [01](homeworks/homework_01/README.md) | Episode returns / random-policy Monte Carlo | Existing personal solution included | `gridworld.py` |
| [02](homeworks/homework_02/README.md) | Bellman optimality / value iteration | Existing personal code included | `agent.py`, `gridworld.py` |
| [03](homeworks/homework_03/README.md) | Policy evaluation / policy iteration | **TODO**; inherits working HW2 value iteration | `agent.py`, `gridworld.py` |

Other notes: [`docs/learning_path.md`](docs/learning_path.md),
[`docs/gridworld_architecture.md`](docs/gridworld_architecture.md),
[`docs/source_audit.md`](docs/source_audit.md), and
[`docs/written_answers_review.md`](docs/written_answers_review.md).

## Quick start (macOS, Python 3)

All three assignments are self-contained: each folder has the Python modules
required to run its version of Gridworld. Start in the selected directory.

```bash
# HW1: Monte Carlo return from a random policy (text-only)
cd homeworks/homework_01/gridworld
python3 gridworld.py -g MazeGrid -k 100 -t -q

# HW2: 100 passes of value iteration, run 10 episodes
cd ../../homework_02/gridworld
python3 gridworld.py -g MazeGrid -a value -i 100 -k 10 -t -q

# HW3: HW2 value iteration still works; new policy agent is unfinished
cd ../../homework_03/gridworld
python3 gridworld.py -g MazeGrid -a value -i 100 -k 10 -t -q
# The next command currently raises NotImplementedError, on purpose:
# python3 gridworld.py -g MazeGrid -a policy -i 100 -k 10 -t -q
```

For the graphical interface omit `-t -q`. macOS Python needs Tk support
for the graphical interface; CLI text mode is easier for debugging.

## Files / development principles

- `homeworks/homework_01/`, `homework_02/`, `homework_03/` are independent,
  runnable snapshots, **not** packages that import across homework folders.
- `docs/` records explanations, comparisons, source provenance, and a small
  Git workflow.
- `.venv/`, IDE settings, compiled files, and private submissions are excluded.
- Course sheets and reference solutions are linked in your private Drive instead
  of being redistributed as part of this repository.
- HW2 and HW3 copies have the two overly verbose value-iteration
  debugging `print()` calls removed; their text display also has a Python 3
  `zip`/`reduce` fix. HW1 uses the supplied `m_solution`
  variant. HW3's `PolicyIterationAgent` is a skeleton, not a finished answer.

## Running tests

```bash
python3 -m unittest discover -s tests -v
```

The smoke tests check the runnable homework code and the default value-iteration
benchmark; they do not substitute for a full course autograder.
