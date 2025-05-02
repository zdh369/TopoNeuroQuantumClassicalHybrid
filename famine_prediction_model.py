import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

class FaminePredictionModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    def load_data(self, features, labels):
        self.X = np.array(features)
        self.y = np.array(labels)

    def train(self):
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))

    def predict(self, new_data):
        return self.model.predict(new_data)

if __name__ == "__main__":
    # Placeholder example data
    features = [
        [0.1, 0.2, 0.3],  # e.g., rainfall, crop yield, market price
        [0.4, 0.1, 0.5],
        [0.3, 0.6, 0.2],
        [0.9, 0.8, 0.7],
        [0.5, 0.4, 0.6]
    ]
    labels = [0, 0, 1, 1, 0]  # 0: no famine, 1: famine risk

    model = FaminePredictionModel()
    model.load_data(features, labels)
    model.train()

    # Predict on new sample
    new_sample = np.array([[0.2, 0.3, 0.4]])
    prediction = model.predict(new_sample)
    print(f"Famine risk prediction for new sample: {prediction[0]}")
