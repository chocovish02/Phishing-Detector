import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from feature_extraction import extract_features

# Load dataset
data = pd.read_csv('dataset.csv')

# Feature extraction
data['features'] = data['URL'].apply(extract_features)
feature_data = pd.DataFrame(data['features'].tolist())

# Prepare data for model training
X = feature_data
y = data['Label']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate model
accuracy = model.score(X_test, y_test)
print(f'Model Accuracy: {accuracy}')

# Save model to file
joblib.dump(model, 'phishing_model.pkl')
