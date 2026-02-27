import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*40

################################################################################################
# Step 1 - Load the Dataset
################################################################################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded sucessfully..")
print("Initial entries from dataset :")
print(df.head())
print(df.tail())

################################################################################################
# Step 2 - Data Analysis (EDA)
################################################################################################

print("Shape of Dataset :", df.shape)
print("Column names :", list(df.columns))
print("Column names :", list(df.dtypes))

print("Missing values (Per Column)")
print(df.isnull().sum())

print("Class Distribution (Species count)")
print(df["FinalResult"].value_counts)

print("Statistical report of dataset")
print(df.describe())

X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================
# FEATURE IMPORTANCE
# ==============================
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

importances = pd.Series(model.feature_importances_, index=X.columns)
print("\nFeature Importance:")
print(importances.sort_values(ascending=False))

# ==============================
# REMOVE SleepHours
# ==============================
X2 = df.drop(["FinalResult", "SleepHours"], axis=1)

X2_train, X2_test, y2_train, y2_test = train_test_split(
    X2, y, test_size=0.2, random_state=42
)

model2 = DecisionTreeClassifier(random_state=42)
model2.fit(X2_train, y2_train)

print("\nAccuracy (full features):", model.score(X_test, y_test))
print("Accuracy (without SleepHours):", model2.score(X2_test, y2_test))

# ==============================
# USE ONLY StudyHours + Attendance
# ==============================
X3 = df[["StudyHours", "Attendance"]]

X3_train, X3_test, y3_train, y3_test = train_test_split(
    X3, y, test_size=0.2, random_state=42
)

model3 = DecisionTreeClassifier(random_state=42)
model3.fit(X3_train, y3_train)

print("\nAccuracy (2 features):", model3.score(X3_test, y3_test))

# ==============================
# PREDICT 5 NEW STUDENTS
# ==============================
new_students = pd.DataFrame({
    "StudyHours": [5, 2, 7, 3, 6],
    "Attendance": [80, 60, 90, 50, 85],
    "PreviousScore": [70, 40, 85, 45, 78],
    "AssignmentsCompleted": [8, 4, 10, 5, 9],
    "SleepHours": [7, 6, 8, 5, 7]
})

predictions = model.predict(new_students)
new_students["PredictedResult"] = predictions

print("\nNew Student Predictions:")
print(new_students)

# ==============================
# MANUAL ACCURACY
# ==============================
y_pred = model.predict(X_test)
manual_accuracy = (y_test == y_pred).sum() / len(y_test)

print("\nManual Accuracy:", manual_accuracy)
print("Sklearn Accuracy:", model.score(X_test, y_test))

# ==============================
# MISCLASSIFIED STUDENTS
# ==============================
misclassified = X_test[y_test != y_pred]
print("\nMisclassified Students:")
print(misclassified)
print("Total Misclassified:", len(misclassified))

# ==============================
# DIFFERENT RANDOM STATES
# ==============================
print("\nRandom State Comparison:")
for rs in [0, 10, 42]:
    m = DecisionTreeClassifier(random_state=rs)
    m.fit(X_train, y_train)
    print(f"random_state={rs} → accuracy:", m.score(X_test, y_test))

# ==============================
# DECISION TREE VISUALIZATION
# ==============================
plt.figure(figsize=(12,8))
plot_tree(model, feature_names=X.columns, class_names=["Fail", "Pass"], filled=True)
plt.show()

# ==============================
# NEW FEATURE PerformanceIndex
# ==============================
df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

X4 = df.drop("FinalResult", axis=1)
y4 = df["FinalResult"]

X4_train, X4_test, y4_train, y4_test = train_test_split(
    X4, y4, test_size=0.2, random_state=42
)

model4 = DecisionTreeClassifier(random_state=42)
model4.fit(X4_train, y4_train)

print("\nAccuracy with PerformanceIndex:", model4.score(X4_test, y4_test))

# ==============================
# MAX DEPTH = NONE
# ==============================
deep_model = DecisionTreeClassifier(max_depth=None, random_state=42)
deep_model.fit(X_train, y_train)

print("\nTraining Accuracy:", deep_model.score(X_train, y_train))
print("Testing Accuracy:", deep_model.score(X_test, y_test))