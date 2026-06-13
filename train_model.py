import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv(r"C:\Users\manus\OneDrive\Desktop\HealthPredictionApp\health.csv")
X = df[['chol', 'fbs', 'thalach']]
y = df['target']

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model saved successfully")