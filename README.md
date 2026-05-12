# 🏥 Disease Prediction System using Random Forest

## 📌 Project Overview

This project is a Machine Learning based Disease Prediction System that predicts diseases based on user-selected symptoms.

The project uses the **Random Forest Algorithm** for prediction and provides a simple and interactive user interface using **Streamlit**.

---

# 🚀 Features

* Predicts diseases based on symptoms
* Uses Random Forest Classifier
* Interactive Streamlit UI
* Trained using symptom-based dataset
* Displays prediction instantly

---

# 🧠 Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit

---

# 📂 Project Structure

```plaintext
├── Disease_prediction.py   # Model training and testing
├── app.py                  # Streamlit user interface
├── disease.csv             # Training dataset
├── Testing.csv             # Testing dataset
├── requirements.txt        # Required libraries
```

---

# ⚙️ How It Works

1. The dataset containing symptoms and diseases is loaded.
2. The Random Forest model is trained using the training dataset.
3. The model is tested using separate testing data.
4. The user selects symptoms in the Streamlit UI.
5. The model predicts the most likely disease.

---

# 🌳 Algorithm Used

## Random Forest Classifier

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

---

# 📊 Model Evaluation

The model performance is evaluated using:

* Accuracy Score
* Classification Report

---

# ▶️ How to Run the Project

## 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

# 📷 Output

The application allows users to:

* Select symptoms
* Click Predict
* View predicted disease instantly

---

# 🎯 Future Improvements

* Better UI design
* Deploy as web application
* Add more disease datasets
* Improve prediction accuracy

---

# ⚠️ Disclaimer

This project is developed for educational purposes only and should not be used for real medical diagnosis.

---

# 🌐 Live Demo

[https://disease-predictor1.streamlit.app/](https://disease-predictor1.streamlit.app/)

---

# 👨‍💻 Author

Made with ❤️ by Vivaan Garg
