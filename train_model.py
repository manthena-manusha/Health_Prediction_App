import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.DataFrame({
    "glucose": [120,180,90,200,110,220,100,250],
    "haemoglobin": [13,11,15,10,14,9,16,8],
    "cholesterol": [180,250,160,300,190,320,170,350],
    "risk": [0,1,0,1,0,1,0,1]
})

X = data[["glucose","haemoglobin","cholesterol"]]
y = data["risk"]

model = RandomForestClassifier()

model.fit(X, y)

with open("model.pkl","wb") as file:
    pickle.dump(model,file)

print("Model Trained Successfully")