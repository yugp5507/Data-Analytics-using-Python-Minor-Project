import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler 
from sklearn.cluster import KMeans 
from sklearn.decomposition import PCA 
import matplotlib.pyplot as plt
import joblib 

# Load models
kmeans = joblib.load("D:\\VNSGU_PDA_DATA\\Data-Analytics-using-Python-Minor-Project\\models\\kmeans_model.pkl")
scaler = joblib.load("D:\\VNSGU_PDA_DATA\\Data-Analytics-using-Python-Minor-Project\\models\\scaler.pkl")

# User input
print("Enter Student Marks:")
new_student = {
    "AWD_Total": float(input("AWD Total: ")),
    "WFS_Total": float(input("WFS Total: ")),
    ".NET_Total": float(input(".NET Total: ")),
    "LOS_Total": float(input("LOS Total: ")),
    "NT_Total": float(input("NT Total: ")),
    "CC_Total": float(input("CC Total: "))
}

# Predict
new_df = pd.DataFrame([new_student])
new_scaled = scaler.transform(new_df)
cluster = kmeans.predict(new_scaled)[0]

performance_map = {
    1: "High Performer",
    0: "Average Performer",
    2: "Needs Improvement"
}

print("Performance Level:", performance_map[cluster])
