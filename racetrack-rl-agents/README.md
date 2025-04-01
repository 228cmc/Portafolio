
# Tabular Reinforcement Learning in a Racetrack Environment

This project contains a jupyter that compares tabular reinforcement learning algorithms : Monte Carlo, Sarsa, and Q-Learning  in a stochastic racetrack environment. It also includes a modified temporal-difference agent that improves learning efficiency over standard Q-Learning.

Originally developed as part of the CM50270 Reinforcement Learning module at the University of Bath.  
The file `racetrack_env.py`, the `.json` files with reference returns, and `track.txt` were provided in the unit.  
All learning algorithms, experimental setups, and analysis are my own work.

## Project Structure

```
.
├── images/                     # Visual assets for the racetrack and action grid
├── racetrack_env.py            # Provided racetrack environment
├── track.txt                   # Provided track layout
├── correct_returns_*.json      # Reference returns for validation (provided)
├── rl_cw_2_racetrack.ipynb     # Main notebook with implementations and experiments
├── requirements.txt            # Python dependencies
├── README.md                   # Project overview (this file)
└── venv/             # Virtual environment
```

## The Racetrack Environment

The environment simulates a simplified racing scenario based on Sutton & Barto (2018). The agent moves on a grid and must learn to reach the finish line as quickly as possible, avoiding going off-track.

Each state is defined by position and velocity:  
`(position_y, position_x, velocity_y, velocity_x)`

Actions change the velocity in x and y directions (total of 9 actions). The environment is stochastic: with 20% probability, the chosen action has no effect.  
Rewards:
- -1 per step  
- -10 if the agent leaves the track  
- +10 for reaching the finish line

The episode ends only when the agent reaches the goal.

## Environment API

The `RacetrackEnv` class provides:

- `reset()` – Initializes the environment and returns a start state.
- `step(action)` – Takes an action and returns the next state, reward, and terminal flag.
- `render(sleep_time)` – Visualizes the environment (for debugging only).
- `get_actions()` – Returns available actions (integers 0–8).

States are Python tuples. Actions correspond to combinations of velocity changes as per an indexed 3x3 grid.

## Baseline Algorithm Comparison

Three RL algorithms were implemented and compared under shared conditions:

- Monte Carlo
- Sarsa
- Q-Learning

All agents used the following hyperparameters:

- ε = 0.15 (exploration rate)  
- γ = 0.9 (discount factor)  
- Q₀ = 0.0 (initial values)  
- α = 0.2 (learning rate for Sarsa and Q-Learning)

Learning curves show convergence behaviors and highlight algorithmic differences.  
Monte Carlo stabilizes late but steadily.  
Sarsa is smoother due to on-policy updates.  
Q-Learning improves faster but fluctuates due to off-policy updates.

## Improved TD Agent

A modified agent was developed to improve sample efficiency and convergence. Enhancements include:

- Experience replay with multiple updates per step
- Epsilon decay over time
- Decaying learning rate
- Parallel agents for stability
- Optional extensions: double Q-learning, reward shaping

The modified agent showed:

- Faster convergence  
- Higher and more stable final returns  
- Lower variance across training seeds

## Evaluation Setup

- 5 agents trained independently  
- 150 episodes per agent  
- Rewards tracked per episode  
- Learning curves plotted and compared

## Reflections

The improvements addressed exploration-exploitation balance, sample reuse, and policy stability. The final agent outperformed the Q-Learning baseline both in speed of learning and consistency. Use of multiple enhancements in tandem (decay, replay, learning rate scheduling) was especially effective.

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Open the notebook:

```bash
jupyter notebook rl_cw_2_racetrack.ipynb
```

3. Run all cells to view baseline training, modified agent evaluation, and plots.

