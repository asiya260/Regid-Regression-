import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

# Title
st.title("🏠 House Price Prediction (Ridge Regression)")

# Load dataset
df = pd.read_csv("housing.csv")
df = df.dropna()

# Convert categorical
df = pd.get_dummies(df, columns=['ocean_proximity'], drop_first=True)

# Features & target
X = df.drop("median_house_value", axis=1)
y = df["median_house_value"]

# Train model
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = Ridge(alpha=1.0)
model.fit(X_scaled, y)

st.subheader("Enter House Details")

# User inputs
inputs = []
for col in X.columns:
    value = st.number_input(f"{col}", value=float(X[col].mean()))
    inputs.append(value)

# Predict button
if st.button("Predict Price"):
    input_array = np.array(inputs).reshape(1, -1)
    input_scaled = scaler.transform(input_array)

    prediction = model.predict(input_scaled)

    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")
