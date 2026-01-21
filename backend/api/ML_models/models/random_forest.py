import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score
import  joblib
from sklearn.metrics import classification_report


dataframe = pd.read_csv("../data/new_data/ML_ready_data.csv", index_col=0)
                        
# 1. Stratified split with fixed random state
X = dataframe.drop(columns=["player1_win"])
y = dataframe['player1_win']
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 2. Classifier with reproducibility
rf = RandomForestClassifier(n_estimators=250, max_depth=10, random_state=42)
rf.fit(x_train, y_train)

# 3. Comprehensive evaluation
y_pred = rf.predict(x_test)
print(classification_report(y_test, y_pred))

joblib.dump(rf, 'random_forest_model.joblib')