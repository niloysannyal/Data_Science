# 🏠 Dhaka Home Rent Prediction

[![Live](https://img.shields.io/badge/LIVE-VISIT%20NOW-red?style=for-the-badge&logo=firefox)](https://dhakahomerentprediction.onrender.com/)

![Screenshot](https://github.com/user-attachments/assets/40e7e80f-ff39-4cd1-bee7-5e01129ee024)

## 📌 About the Project
This data science project demonstrates a full-stack machine learning pipeline for predicting house rents in Dhaka. It includes:

- 📊 A machine learning model built using **Random Forest Regressor**
- 🌐 A **Flask** server to handle predictions
- 💻 A responsive **web frontend** for user input and prediction display

## 💡 Key Features
- User inputs: Area (Square feet), Bedrooms, Bathrooms, Location.
- Real-time rent prediction
- End-to-end integration: Model → Server → Frontend

## 📁 Folder Structure
```
DhakaHomeRentPrediction/
├── client/      # HTML/CSS/JS website frontend
├── server/      # Flask backend API
├── model/       # Model training notebook, data, and artifacts
├── requirements.txt
├── Procfile
└── README.md
```

## 🧠 Concepts Covered
- Data loading and cleaning
- Outlier detection and removal
- Feature engineering
- Dimensionality reduction
- Hyperparameter tuning with GridSearchCV
- K-Fold Cross Validation

## 🛠️ Tech Stack
- Python (Pandas, NumPy, Scikit-learn, Matplotlib)
- Flask
- HTML / CSS / JavaScript
- Jupyter Notebook
- VS Code / PyCharm
- Render (for deployment)

## 🚀 How to Run Locally

1. Clone the repository
   ```bash
   git clone https://github.com/niloysannyal/Data_Science.git
2. Nevigate to the project folder
   ```bash
   cd Data_Science/projects/DhakaHomeRentPrediction
3. Install the required dependencies for the backend
   ```bash
   pip install -r requirements.txt
4. Start the Flask server
   ```bash
   cd server
   python server.py
5. Open the frontend
   - Open `client/app.html` in your browser.

