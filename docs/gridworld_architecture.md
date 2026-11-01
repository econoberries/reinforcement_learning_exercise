# Gridworld code architecture

Each homework snapshot includes:

| File | Responsibility |
|---|---|
| `gridworld.py` | Grid constructors, CLI flags, runEpisode, simulations, visualization callbacks |
| `gridworldClass.py` | Underlying MDP states, legal actions, rewards and probabilistic transitions |
| `agent.py` | RandomAgent, ValueIterationAgent; HW3 adds PolicyIterationAgent stub |
| `mdp.py` | Abstract Markov decision process interface |
| `environment.py` | Abstract environment interface |
| `util.py` | Support utilities such as Counter |
| `graphicsGridworldDisplay.py`, `graphicsUtils.py` | Optional Tk-based GUI |
| `textGridworldDisplay.py` | Console/text display |

**Critical distinction:** `Gridworld` is the *model*, while
`GridworldEnvironment` is the *sampler* of transitions. The planner takes a
known model; the episode runner samples the environment.

Typical flow:

`gridworld.py -> Gridworld (MDP) -> Agent (policy/values) -> Environment (sampled episode) -> print/display`

Use `-g MazeGrid`, `-a random|value|policy`, `-i <planner passes>`,
`-k <sample episodes>`, `-d <discount>`, `-n <noise>`, `-r <living reward>`,
`-t` (text-only), `-q` (quiet). `-a policy` is HW3 only and is intentionally
unimplemented until Homework 3 is worked through.
