
## Probabilistic Decision-Making with Bayesian Linear Regression

This repository contains a Jupyter notebook that illustrates how Bayesian linear regression can be used not only to make predictions, but also to decide *when not to predict*, based on the model's quantified uncertainty.

### Overview

The notebook simulates a realistic scenario where:
- Accurate predictions (absolute error ≤ 0.15) are **rewarded with £10**
- Inaccurate predictions (error > 0.15) are **penalized with £20**
- The model may choose to **abstain** from predicting when uncertainty is too high, resulting in no gain or loss

This setting reflects how Bayesian models provide tools for decision-making under uncertainty, using:

- **Posterior predictive standard deviation** to estimate uncertainty
- **Marginal likelihood (log evidence)** to assess model confidence in each test point

### Key Features

- Bayesian decision algorithm that combines uncertainty and marginal likelihood
- Dynamic thresholding based on predictive variance
- Evaluation metrics:
  - Number of predictions made
  - Accuracy and failure rates
  - Total earnings under the reward-cost structure
- Visualizations:
  - Where predictions are accepted vs. declined
  - Uncertainty intervals around the Bayesian predictor
  - Distribution of marginal likelihoods

### File

- `ProbabilisticDecisionMaking.ipynb`: Contains the full implementation, evaluation, and visual analysis

---

## Setup Instructions

To run the notebook in a clean environment:

1. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install required packages**:

   ```bash
   pip install requirements.txt
   ```

3. **Launch the notebook**:

   ```bash
   jupyter notebook
   ```

---

## Purpose

This notebook serves as an educational resource, demonstrating how probabilistic models can be applied in risk-aware decision-making. It is intended as an introduction to core Bayesian thinking and a foundation for more advanced topics in probabilistic machine learning.

