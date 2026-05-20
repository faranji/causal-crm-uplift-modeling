# CausalCRM: Algorithmic ROI Optimization with Uplift Modeling

### 🌟 Project Overview
Traditional CRM and marketing models focus strictly on predicting "who will buy" or "who will churn," often leading to wasted budget on already loyal customers (Sure Things) or ignoring unresponsive segments. 

**CausalCRM** is a next-generation marketing optimization project designed to isolate and target only the **"Persuadables"**—customers who will buy *only* if they receive a specific marketing action. By combining causal inference and advanced machine learning architectures, this project transforms raw campaign data into strategic financial value, maximizing Return on Investment (ROI) by ensuring every marketing dollar is spent on true incremental growth while minimizing campaign fatigue.

### Technical Superpowers
- **Metodology:** Uplift Modeling (Causal Inference) using the `scikit-uplift` framework.
- **Feature Engineering:** Custom domain-driven interaction features (`Digital Affinity`, `Spending Intensity`) to enhance feature importance.
- **Model Architecture:** Advanced Stacking Ensemble combining the categorical processing power of **CatBoost** and the leaf-wise speed of **LightGBM**, managed by a Logistic Regression meta-learner to eliminate overfitting.
- **Validation Strategy:** Rigorous out-of-sample testing validated via **Qini Curves (Qini AUC)** to measure true incremental revenue.
