# Working with the existing private GitHub repository

Repository: https://github.com/econoberries/reinforcement_learning_exercise

## Clone it to your Mac

```bash
cd ~/Documents
git clone https://github.com/econoberries/reinforcement_learning_exercise.git
cd reinforcement_learning_exercise
python3 -m unittest discover -s tests -v
```

## Develop the next homework

Each homework is a self-contained runnable snapshot. Keep earlier versions unchanged.
Work on HW3 in `homeworks/homework_03/gridworld`, and commit one logical change at a time.

```bash
git status
git add homeworks/homework_03/gridworld/agent.py homeworks/homework_03/gridworld/gridworld.py
git commit -m "HW3: implement policy evaluation"
git push origin main
```

Do not commit secrets, raw starter ZIPs, provided assignment sheets, submitted PDFs, or virtual environments. The course's underlying educational code carries sharing restrictions; keep the repo **private** unless your instructor approves publication.
