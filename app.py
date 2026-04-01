import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Title
st.title("Disease Prediction System")


# Load data
@st.cache_data
def load_data():
    data = pd.read_csv("disease.csv")
    return data


data = load_data()

# Split
X = data.drop("prognosis", axis=1)
y = data["prognosis"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

st.write("### Select Symptoms")

# Create input dict
input_data = {}

# Show checkboxes (limit to 15 for UI)
symptoms = list(X.columns)[:15]

for symptom in symptoms:
    input_data[symptom] = st.checkbox(symptom)

# Predict button
if st.button("Predict"):
    # Convert True/False → 1/0
    input_df = pd.DataFrame(
        [[1 if input_data[s] else 0 for s in symptoms]], columns=symptoms
    )

    # Match all columns
    full_input = pd.DataFrame([[0] * len(X.columns)], columns=X.columns)

    for col in symptoms:
        full_input[col] = input_df[col]

    prediction = model.predict(full_input)

    st.success(f"Predicted Disease: {prediction[0]}")
