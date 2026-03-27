# 🏠 House Price Prediction using Ridge Regression

## 📌 Overview

This project builds a **Ridge Regression model** to predict house prices based on demographic and geographic features from the California Housing Dataset.

The model handles **multicollinearity** between features using **L2 regularization**, improving prediction stability and performance.

---

## 📊 Dataset

Dataset used: *California Housing Dataset*

### Features:

* `longitude` → Distance west
* `latitude` → Distance north
* `housing_median_age` → Age of houses
* `total_rooms` → Total rooms
* `total_bedrooms` → Total bedrooms
* `population` → Population in the area
* `households` → Number of households
* `median_income` → Median income
* `ocean_proximity` → Location near ocean (categorical)

### Target:

* `median_house_value` → House price

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## 🔍 Project Workflow

### 1. Data Preprocessing

* Removed missing values
* Converted categorical feature (`ocean_proximity`) using one-hot encoding

### 2. Feature Selection

* Selected all numerical features
* Target variable: `median_house_value`

### 3. Data Splitting

* Training set: 80%
* Testing set: 20%

### 4. Feature Scaling

* Applied `StandardScaler` to normalize features

### 5. Model Building

* Used **Ridge Regression**
* Alpha value: `1.0`

### 6. Model Evaluation

* Mean Squared Error (MSE)
* R² Score

---

## 🤖 Model Explanation

### Why Ridge Regression?

* Handles **multicollinearity**
* Reduces **overfitting**
* Improves generalization

### What is Alpha?

* Regularization strength parameter
* Higher value → simpler model
* Lower value → more complex model

---

## 🚀 Streamlit App

An interactive web app is built using Streamlit where users can:

* Input housing features
* Get predicted house price instantly

---

## 📁 Project Structure

```
├── app.py
├── housing.csv
├── requirements.txt
├── README.md
```

---

## ▶️ How to Run Locally

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run Streamlit app:

```
streamlit run app.py
```

---

## 🌐 Deployment

The project is deployed using Streamlit Cloud via GitHub integration.

---

## 📈 Output

* Predicts house prices based on user input
* Displays results instantly in the web interface

---

## 📌 Conclusion

This project demonstrates how Ridge Regression can be used effectively for real-world prediction problems while handling correlated features.

---
want to test the project :
Run real time - https://8isml5cj5msctjadzmeqse.streamlit.app/

## ✍️ Author

Asiya
