import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

df = pd.read_csv("sample_data.csv")

X = df[["reaction_ms", "delta_x", "delta_y", "click_std", "recoil_std"]]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test, pred))

joblib.dump(model, "cheat_model.pkl")
print("모델 저장 완료")