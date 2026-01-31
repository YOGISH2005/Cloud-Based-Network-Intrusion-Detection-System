from sklearn.ensemble import IsolationForest
import joblib
import numpy as np

X = np.random.rand(500, 5)

model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X)

joblib.dump(model, "model/iforest.pkl")
print("Model trained and saved")
