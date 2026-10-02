# GestureMorse
GestureMorse is a real-time, webcam-based system that recognizes hand gestures representing Morse code and converts them into readable text. Using computer vision and temporal gesture analysis, the project detects short and long gesture patterns as dots and dashes then decodes them into characters and words.

Unlike basic gesture-recognition projects, GestureMorse focuses on touchless communication, dynamic gesture timing and user adaptability. It is designed as a low-cost communication interface that works with only a standard camera making it useful for accessibility, silent interaction and low-resource environments.

This project helps fill the gap between simple static hand-gesture demos and practical, sequence-based communication systems by combining real-time hand tracking, Morse decoding and error-tolerant recognition.

# Tech Stack
Python – core programming language
OpenCV – video capture and image processing
MediaPipe – hand landmark detection and tracking
NumPy – numerical operations
Scikit-learn / PyTorch – gesture classification and adaptive ML models
Streamlit / Flask / FastAPI – interface or backend integration
NLTK / SymSpell – optional text correction after Morse decoding
