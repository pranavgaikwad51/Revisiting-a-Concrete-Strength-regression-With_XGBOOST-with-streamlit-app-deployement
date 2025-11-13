# 🧱 Concrete Compressive Strength Prediction using XGBoost

## 📌 Overview

This project predicts the **compressive strength of concrete** using the **Yeh Concrete Dataset** and an advanced **XGBoost regression model**. The application is deployed using **Streamlit**, providing an interactive interface for real-time predictions.

Concrete strength prediction is a critical problem in civil engineering, and machine learning models—especially gradient boosting algorithms—are highly effective due to their ability to model nonlinear relationships in the data.

---

## 🧩 Problem Statement

The goal is to build a machine learning model that can accurately predict the **compressive strength (MPa)** of concrete based on its ingredient proportions and age.

The ingredients include:

* Cement
* Blast Furnace Slag
* Fly Ash
* Water
* Superplasticizer
* Coarse Aggregate
* Fine Aggregate
* Age (in days)

---

## 🎯 Objective

* Perform Exploratory Data Analysis (EDA)
* Handle outliers and clean the dataset
* Train an XGBoost regression model
* Build a **Streamlit web app** for real-time prediction
* Deploy the app online (Streamlit Cloud / GitHub)

---

## 📊 Dataset

**Name:** Yeh Concrete Strength Dataset

**Source:** Kaggle — *Yeh Concrete Data*

**Rows:** 1030

**Columns:** 9 numeric features (8 inputs + 1 target)

**Target Variable:** Compressive Strength (MPa)

Each feature represents the quantity (in kg/m³) of a component used in concrete.

---

## 🛠️ Tools & Libraries

* Python 3.x
* Streamlit
* XGBoost
* Pandas
* NumPy
* Scikit-learn
* Matplotlib / Seaborn

---

## 🧠 Model Architecture

### **Algorithm: XGBoost Regressor**

XGBoost is a high-performance gradient boosting algorithm optimized for speed and accuracy.

Key characteristics:

* Regularization (L1 & L2)
* Tree pruning
* Handles missing values automatically
* Efficient with tabular data

Parameters used:

* `n_estimators=300`
* `learning_rate=0.05`
* `max_depth=6`
* `subsample=0.9`
* `colsample_bytree=0.9`
* `objective='reg:squarederror'`

---

## 🧹 Data Preprocessing

### Steps:

1. Loaded dataset
2. Performed descriptive statistics
3. Plotted **boxplots** for all columns
4. Detected and removed outliers (except target variable)
5. Split data into training/testing sets (80/20)
6. Trained XGBoost model
7. Saved model as `model.pkl`

---

## 📈 Evaluation Metrics

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

These metrics help evaluate the model’s predictive accuracy and reliability.

---

## 🖥️ Streamlit App Features

### **User Inputs:**

* Cement
* Slag
* Fly Ash
* Water
* Superplasticizer
* Coarse Aggregate
* Fine Aggregate
* Age

### **Outputs:**

* Predicted compressive strength (MPa)

### **Sidebar Includes:**

* Developer info (contact, GitHub, LinkedIn)
* Career goals
* Learning progress

---

## 🚀 Deployment Guide

### **To run locally:**

```
pip install -r requirements.txt
streamlit run app.py
```

### **To deploy on Streamlit Cloud:**

1. Push all files to a GitHub repository
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Select **Deploy App**
4. Choose your repo and branch
5. Set `app.py` as main file

---

## 📂 Project Structure

```
Concrete-Strength-XGBoost-App/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── model.pkl
└── concrete_data.csv
```

---

## 🙋‍♂️ Developer

### **Pranav Gaikwad**

* 📧 Email: [gaikwadpranav988@gmail.com](mailto:gaikwadpranav988@gmail.com)
* 📱 Phone: 7028719844
* 🔗 LinkedIn: [https://www.linkedin.com/in/pranav-gaikwad-0b94032a](https://www.linkedin.com/in/pranav-gaikwad-0b94032a)
* 🐙 GitHub: [https://github.com/pranavgaikwad51](https://github.com/pranavgaikwad51)
* 🚀 Streamlit App: [https://loan-prediction-using-data-engineering-machine-learning--pranav.streamlit.app/](https://loan-prediction-using-data-engineering-machine-learning--pranav.streamlit.app/)

### **Career Goal:**

Data Scientist → AI/ML Engineer → Chief AI Scientist

---

## 📜 License

This project is open-source and free to use for learning and development.

---

## 🙏 Acknowledgements

* Yeh (1998) — Concrete Strength Dataset
* Kaggle Community
* Streamlit Team
* XGBoost Developers

---

## 🎓 Learning Notes

This project strengthens skills in:

* EDA
* Outlier handling
* XGBoost modeling
* App deployment
* Portfolio development
