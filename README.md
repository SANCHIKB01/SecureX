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
├── frontend/
│   ├── app.py
│   ├── tutorial8.py
├── haarcascades/
├── securex-main/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   ├── Components/
│   │   │   ├── Create.js
│   │   │   ├── Login.js
│   │   │   └── Logintr.js
│   │   └── Containers/
│   │       ├── Auth/
│   │       ├── Exam/
│   │       ├── MPage/
│   │       ├── StPage/
│   │       ├── TcPage/
│   │       └── LeaderBoard.js
│   └── public/
├── screenshots/
```


# 📸 Screenshots
### Main Page

![image](https://github.com/SANCHIKB01/SecureX/blob/main/screenshots/Main%20Page.jpg)

### Student Page

![image](https://github.com/SANCHIKB01/SecureX/blob/main/screenshots/Student%20Page.jpg)

### Exam Page

![image](https://github.com/SANCHIKB01/SecureX/blob/main/screenshots/Exam%20Page.jpg)

### Teacher Page

![image](https://github.com/SANCHIKB01/SecureX/blob/main/screenshots/Teacher%20Page.png)

### Student Result Data

![image](https://github.com/SANCHIKB01/SecureX/blob/main/screenshots/Student%20Result%20Data.png)


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
