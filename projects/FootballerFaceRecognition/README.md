# ⚽ Footballer Face Recognition System

[![Live](https://img.shields.io/badge/LIVE-VISIT%20NOW-red?style=for-the-badge&logo=firefox)](https://footballerimageclassifier.onrender.com/)

![Screenshot (167)](https://github.com/user-attachments/assets/61898a64-19fe-4d15-9e9a-6a19db45ee3d)

## 📌 Overview

A multi-class face recognition system that identifies famous professional footballers using classical machine learning techniques and OpenCV. The project integrates computer vision and ML models into a full-stack web application, allowing users to upload group or individual photos and receive real-time predictions.

---

## ⚙️ Key Features

- Multi-face detection and classification in one image
- Haar Cascade + HOG + SVM-based pipeline
- Drag-and-drop image prediction interface
- Flask backend with HTML/CSS/JS frontend

---

## 🧑‍💼 Footballers in the Dataset

1. Lionel Messi  
2. Cristiano Ronaldo  
3. Zlatan Ibrahimović  
4. Neymar Jr  
5. Kylian Mbappé  
6. Kevin De Bruyne  
7. Erling Haaland  
8. Robert Lewandowski  
9. Sergio Ramos  
10. Jude Bellingham  

---

## 🗂️ Folder Structure

```bash
FootballerFaceRecognition/
├── client/       # Frontend: HTML, CSS, JavaScript
├── server/       # Backend: Flask server handling prediction logic
├── model/        # Jupyter notebook, saved models, utility scripts
└── dataset/      # Training data of labeled footballer images
```

## 🔧 Technologies Used
- Python
- NumPy, OpenCV – Image preprocessing
- Matplotlib, Seaborn – Data visualization
- Scikit-learn – Model training (SVM)
- Flask – Backend server
- HTML, CSS, JavaScript – User Interface
- Jupyter Notebook, VS Code, PyCharm – Development tools

## 🚀 How to Run Locally
1. Clone the repository
   ```bash
   git clone --no-checkout https://github.com/niloysannyal/Data_Science.git

2. Navigate to the project folder
   ```bash
   cd FootballerFaceRecognition

3. Install the required dependencies for the backend
   ```bash
   pip install -r requirements.txt

4. Start the Flask server
   ```bash
   cd server
   python server.py

6. Open the frontend
   - Open `client/app.html` in your browser.
  

## 📬 Contact
For any questions or collaborations, feel free to reach out at niloysannyal@gmail.com
