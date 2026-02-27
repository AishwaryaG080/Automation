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
################################################################################################
# Step 3 - Decide Independent & Dependent Variables
################################################################################################

print(Border)
print("Step 3 : Decide Independent & Dependent Variables ")
print(Border)

Feature_Cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
    ]

Class_Cols = [
    "FinalResult"
]

X = df[Feature_Cols]
Y = df["FinalResult"]

print("X Shape", X.shape)
print("Y Shape", Y.shape)

################################################################################################
# Step 5 - Split into Training and Testing data
################################################################################################

print(Border)
print("Step 5 : Split into Training and Testing data ")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size= 0.2,
    random_state=42
)

print("Data splitting activity done :")

print("X - Independent :", X.shape) 
print("Y - Dependent :", Y.shape)   

print("X_train :", X.shape)       
print("X_test :", X.shape)       

print("Y_train :", Y.shape)       
print("Y_test :", Y.shape)        

################################################################################################
# Step 6 - Build the model
################################################################################################

print(Border)
print("Step 6 : Build the model")
print(Border)

print("We are going to use DesicionTreeClassifier")

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=1,
    random_state=42
)
model = model.fit(X,Y)


################################################################################################
# Step 6 : Build the model
################################################################################################

print(Border)
print("Step 6 : Build the model")
print(Border)

model.fit(X_train,Y_train)

print("Model training completed")

################################################################################################
# Step 8 - Evaluate/Testing the model
################################################################################################

print(Border)
print("Step 8 - Evaluate/Testing the model")
print(Border)

Y_pred = model.predict(X_test)

print("Model Evaluation/Testing Complete")  

print(Y_pred.shape)

print("Expected answers :")
print(Y_test)

print("Predicted answers :")
print(Y_pred)

################################################################################################
# Step 9 - Evaluate the model performance
################################################################################################

print(Border)
print("Step 9 - Evaluate the model performance")
print(Border)

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of model is :", accuracy*100)

cm =confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix :")
print(cm)

print("Classification Report")
print(classification_report(Y_test,Y_pred))

################################################################################################
# Step 10 - Plot Confusion Matrix
################################################################################################

print(Border)
print("Step 10 - Plot Confusion Matrix")
print(Border)

data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)
data.plot()
plt.title("Confusion Matrix of Student Performance")
plt.show()



