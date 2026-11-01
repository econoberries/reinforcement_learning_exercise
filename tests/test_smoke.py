"""Tiny non-GUI smoke tests for preserved homework snapshots."""
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


def run_gridworld(hw, *args):
    work = ROOT / 'homeworks' / hw / 'gridworld'
    return subprocess.run([sys.executable, 'gridworld.py', '-t', '-q', *args],
                          cwd=work, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          text=True, timeout=30)


class HomeworkSmokeTests(unittest.TestCase):
    def test_hw1_random_policy(self):
        result = run_gridworld('homework_01', '-g', 'MazeGrid', '-k', '2')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Mean returns:', result.stdout)

    def test_hw2_value_iteration(self):
        result = run_gridworld('homework_02', '-g', 'MazeGrid', '-a', 'value',
                               '-i', '100', '-k', '1')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('S: 0.28', result.stdout)

    def test_hw3_retains_value_iteration(self):
        result = run_gridworld('homework_03', '-g', 'MazeGrid', '-a', 'value',
                               '-i', '100', '-k', '1')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('S: 0.28', result.stdout)

    def test_hw2_benchmark_precision(self):
        work = ROOT / 'homeworks' / 'homework_02' / 'gridworld'
        code = ('from gridworld import getMazeGrid; '
                'from agent import ValueIterationAgent; '
                'm=getMazeGrid(); m.setNoise(0.2); '
                'a=ValueIterationAgent(m, 0.9, 100); '
                'print(f"{a.getValue(m.getStartState()):.6f}")')
        result = subprocess.run([sys.executable, '-c', code], cwd=work,
                                text=True, capture_output=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('0.282195', result.stdout)

    def test_hw3_policy_option_exists_but_is_incomplete(self):
        result = run_gridworld('homework_03', '-g', 'MazeGrid', '-a', 'policy',
                               '-i', '3', '-k', '0')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('NotImplementedError', result.stderr)

if __name__ == '__main__':
    unittest.main()
