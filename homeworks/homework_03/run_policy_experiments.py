"""Homework 3: inspect policy-iteration rounds on MazeGrid.

Run from the repository root:
    python3 homeworks/homework_03/run_policy_experiments.py
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "gridworld"))
from agent import PolicyIterationAgent, ValueIterationAgent
from gridworld import getMazeGrid


for noise in (0.2, 0.0):
    mdp = getMazeGrid()
    mdp.setNoise(noise)
    start = mdp.getStartState()

    policy_agent = PolicyIterationAgent(mdp, discount=0.9, iterations=100)
    value_agent = ValueIterationAgent(mdp, discount=0.9, iterations=100)
    first_nonzero = next(
        (i for i, value in enumerate(policy_agent.start_values_by_round, 1)
         if abs(value) > 1e-10), None
    )

    print(f"\nMazeGrid: noise={noise}, discount=0.9")
    print(f"First round with nonzero start value: {first_nonzero}")
    print(f"Policy improvement rounds to stability: {policy_agent.rounds}")
    print(f"Policy iteration V(start): {policy_agent.getValue(start):.6f}")
    print(f"Value iteration V(start):  {value_agent.getValue(start):.6f}")
    print("Start-state value after each policy evaluation:")
    for round_number, value in enumerate(policy_agent.start_values_by_round, 1):
        print(f"  Round {round_number}: {value:.9f}")
