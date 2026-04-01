# Step 1: Import libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Step 2: Load datasets
train_data = pd.read_csv("disease.csv")
test_data = pd.read_csv("Testing.csv")
# # Step 3: Split features and target
X_train = train_data.drop("prognosis", axis=1)
y_train = train_data["prognosis"]

X_test = test_data.drop("prognosis", axis=1)
y_test = test_data["prognosis"]
X_test = X_test.reindex(columns=X_train.columns, fill_value=0)


# Step 4: Create model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Step 5: Train model
model.fit(X_train, y_train)

# Step 6: Predict on TEST data
y_pred = model.predict(X_test)

# Step 7: Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy:", accuracy)
