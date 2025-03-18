import eventlet
eventlet.monkey_patch()  # Must be the very first thing

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import numpy as np
import cv2
import base64
import time

# Initialize Flask and SocketIO with CORS
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*")

# Emotion labels
EMOTION_LABELS = ['happy', 'sad', 'angry', 'fear', 'surprise', 'neutral']

# Simulate model (replace with your actual model)
def simulate_model_predict(frame):
    timestamp = time.time()
    if timestamp % 10 < 2:
        return np.array([0.95, 0.02, 0.01, 0.01, 0.005, 0.005], dtype=np.float32)
    elif timestamp % 10 < 4:
        return np.array([0.10, 0.85, 0.02, 0.01, 0.01, 0.01], dtype=np.float32)
    else:
        return np.array([0.05, 0.05, 0.85, 0.02, 0.01, 0.02], dtype=np.float32)

# Simulate audio emotion
def simulate_audio_emotion():
    timestamp = time.time()
    if timestamp % 10 < 3:
        return {'emotion': 'happy', 'confidence': 0.90}
    elif timestamp % 10 < 6:
        return {'emotion': 'sad', 'confidence': 0.80}
    else:
        return {'emotion': 'angry', 'confidence': 0.75}

# Process video frame
def process_frame(frame_data):
    encoded_data = frame_data.split(',')[1]
    decoded_data = base64.b64decode(encoded_data)
    np_arr = np.frombuffer(decoded_data, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    frame = cv2.resize(frame, (224, 224))
    frame = frame / 255.0
    frame = np.expand_dims(frame, axis=0)
    return frame

# Route for serving the front-end
@app.route('/')
def index():
    return render_template('index.html')

# Handle incoming video frames
@socketio.on('video_frame')
def handle_video_frame(data):
    global is_running
    if not is_running:
        return
    try:
        frame = process_frame(data)
        video_emotions = simulate_model_predict(frame)
        video_emotion_idx = np.argmax(video_emotions)
        video_emotion = EMOTION_LABELS[video_emotion_idx]
        video_confidence = float(video_emotions[video_emotion_idx])

        audio_data = simulate_audio_emotion()
        audio_emotion = audio_data['emotion']
        audio_confidence = audio_data['confidence']

        final_emotion = video_emotion if video_confidence > audio_confidence else audio_emotion
        final_confidence = max(video_confidence, audio_confidence)

        emotion_data = {
            'video_emotion': video_emotion,
            'video_confidence': video_confidence,
            'audio_emotion': audio_emotion,
            'audio_confidence': audio_confidence,
            'final_emotion': final_emotion,
            'final_confidence': final_confidence
        }
        
        emit('emotion_update', emotion_data)
        print(f"Sent: {emotion_data}")

    except Exception as e:
        print(f"Error processing frame: {str(e)}")
        emit('error', {'message': str(e)})
@socketio.on('start_detection')
def start_detection():
    global is_running
    is_running = True
    emit('detection_started', {'message': 'Live detection started'})
    print("Detection started by user")
    
# Handle stop detection
@socketio.on('stop_detection')
def stop_detection():
    global is_running
    is_running = False
    emit('detection_stopped', {'message': 'Live detection stopped'})
    print("Detection stopped by user")

# Global flag to control detection
is_running = True

# Run the app
if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5000, debug=True)