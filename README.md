# SecureX - Face Detection & Monitoring System
### SecureX (Flask + OpenCV + MySQL + React)
SecureX is an intelligent face detection and exam proctoring system built with OpenCV, Flask, React, and MySQL. It provides real-time webcam monitoring, live video streaming, and automatic multi-face detection to ensure exam integrity. With full-screen enforcement, violation alerts, and an easy-to-use dashboard for teachers and students, SecureX safeguards exams and can easily adapt to security needs


# 🚀 Features
- 🎥 Real-time face and eye detection using OpenCV Haar Cascades
- ⚠️ Multi-face warning system for exam proctoring
- 🔴 Live video streaming through Flask backend
- 👨‍🏫 Separate login systems for teachers and students
- 📝 Exam creation and management functionality
- 🏆 Leaderboard system for performance tracking
- 🌐 Fully responsive React frontend with modern UI
- 💾 MySQL database integration for persistent storage
  

# 🛠️ Tech Stack

| Layer        | Tools Used                                      |
|--------------|--------------------------------------------------|
| Frontend     | React.js, React Router,  Bootstrap              |
| Backend      | Python (Flask), OpenCV, Flask-CORS              |
| Computer Vision  | OpenCV Haar Cascades for face/eye detection     |
| Streaming    | Flask Response streaming for live video         |
| Database     | MySQL for user data and exam storage            |

                    
# 📂 Project Structure
```
securex/
├── app.py
├── tutorial8.py
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   ├── Components/
│   │   │   ├── Create.js
│   │   │   ├── Login.js
│   │   │   └── Logintr.js
│   │   └── Containers/
│   │       ├── TcPage/
│   │       ├── StPage/
│   │       ├── MPage/
│   │       ├── Exam/
│   │       └── LeaderBoard/
│   └── public/
├── screenshots/
```


# 📸 Screenshots
### Project View

![image](https://github.com/user-attachments/assets/cc9f92ee-a726-4627-9811-330d3cd9e876)

### Uploading File and QnA

![image](https://github.com/user-attachments/assets/1cac202d-7156-4f4c-873f-a01a0c7037c0)

### Delete the document

![image](https://github.com/user-attachments/assets/adf5ff38-aa97-4866-b670-0634a91715dc)

### MongoDB Chat messages

![image](https://github.com/user-attachments/assets/77555947-0de6-40ee-9f5a-ad1062b14d7f)

### Redix Cache messages

![image](https://github.com/user-attachments/assets/ba52f197-0e0b-47af-8cdb-79a3b97d7b8c)


# 🗣️ Set Your Database Configuration
Before running the app, you need to configure your MySQL database and create a Google Form for test creation:

1. MySQL Database - Create database named `securex` and update password in `app.py`
2. Google Form - Create a Google Form for test/exam creation and get the shareable link


# 🎥 Demo Video You can watch a full walkthrough here:
https://drive.google.com/file/d/1kgMNXO42R5DTQNe4EOXKZoS8Bf9mNV6a/view?usp=sharing


# 🔗 GitHub Repo: 
https://github.com/SANCHIKB01/SecureX


# 🖥 Local Setup
```bash
git clone https://github.com/SANCHIKB01/SecureX.git
```
### Backend Setup
```bash 
cd securex
pip install flask opencv-python flask-cors mysql-connector-python
python app.py
```
### Frontend Setup
```bash
cd frontend
npm install
npm install react-router-dom bootstrap
npm start
```
