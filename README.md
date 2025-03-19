# 🎭 Emotion Detection


Real-time emotion detection from video and audio using Flask, SocketIO, and machine learning.

## 🌟 Overview
This project brings emotion detection to life by analyzing video (facial expressions) and audio (voice tone) in real-time. Built with Flask and SocketIO, it features a sleek, scrollable web interface that displays detected emotions (e.g., "angry") with confidence scores in a dynamic bar chart. Whether you're uploading media files or using your webcam for live detection, this tool provides an intuitive way to explore emotions.

## ✨ Key Features
- Real-Time Analysis 🕒: Detect emotions live via webcam or from uploaded video/audio files.
- Dual Input Processing 🎥🎙️: Combines video and audio for more accurate emotion detection.
- Interactive Dashboard 📊: Scrollable UI with start/stop controls, file uploads, and a confidence bar chart.
- Cross-Platform 💻: Works seamlessly on Windows with Python and a modern browser.

## 🚀 Getting Started
### Prerequisites
Ensure you have the following installed:

**Python 3.6+ 🐍**
**Git** (to clone the repository) 📦
A modern **web browser** (e.g., Chrome, Firefox) 🌐

### Dependencies
The project relies on several Python libraries, listed in requirements.txt:

- Flask
- Flask-SocketIO
- eventlet
- numpy
- OpenCV (cv2)
- Chart.js (for the bar chart)

## Installation
  - 1. Clone the Repository 📥
       ```bash
       git clone https://github.com/DigiDARATechnologies/Emotion-Detection-Project.git
       cd Emotion-Detection-Project
       ```
    2. Install Dependencies 🛠️
       ```bash
       pip install -r requirements.txt
       ```
      If requirements.txt is missing, generate it:
      ```bash
      pip freeze > requirements.txt
      ```
    3. Run the Application 🚀
       ```bash
       python app.py
       ```
       - The server will start at http://127.0.0.1:5000/.
       - Open this URL in your browser to access the interface.

## 🎮 Usage
1. Upload Files 📂
   - Use the "Upload Video" or "Upload Audio" inputs to select files.
   - Click Upload Files to process and analyze emotions.
2. Start Live Detection 📹
   - Click Start Live Detection to enable your webcam.
   - Watch as emotions (e.g., "angry") and confidence scores (e.g., 85%, 75%) update in real-time.
3. Stop Detection ⏹️
   - Click Stop Live Detection to end the webcam feed.
4. View Results 📈
   - Emotions and confidence scores are displayed for video and audio inputs.
   - A bar chart visualizes the confidence levels for both sources.

## 📂 Project Structure
 ```text
Emotion-Detection-Project/
├── app.py                  # Flask backend with SocketIO for real-time processing
├── templates/
│   └── index.html          # HTML, CSS, and JavaScript for the web interface
├── haarcascade_frontalface_default.xml  # OpenCV face detection classifier
├── requirements.txt        # Python dependencies
├── .gitignore              # Excluded files (e.g., __pycache__, venv)
├── README.md               # This file
```

## 🤝 Contributing
We welcome contributions to enhance this project! Follow these steps:
  1. **Fork the Repository 🍴**
  2. **Create a Feature Branch 🌿**
     ```bash
     git checkout -b feature/your-feature-name
     ```
  3. **Commit Your Changes 💾**
     ```bash
     git commit -m "Add your feature description"
     ```
  4. **Push to Your Branch 📤**
     ```bash
     git push origin feature/your-feature-name
     ```
  5. **Open a Pull Request 🔄**

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 📬 Contact
 - Maintainer: Ranjeeth11 (GitHub)
 - Organization: DigiDARATechnologies
 - Issues & Feedback: Open an issue

## 🙌 Acknowledgments
  - **Flask & SocketIO**: For enabling real-time web applications.
  - **OpenCV**: For face detection and video processing.
  - **Chart.js**: For the interactive bar chart visualization.
  - **Community**: Thanks to the open-source community for inspiration and support.
