# Face Recognition System

## Overview
This project verifies user identity by comparing their face to previously stored data. It captures a face during login and checks if it matches the saved data, making it ideal for secure login systems.

## Features
- **Face Registration**: Capture multiple photos of your face from different angles.
- **Face Login**: Capture a single photo to verify identity.
- **Error Handling**: Displays messages for no face detected or incorrect input.

## Prerequisites
- **Python 3.x**
- Required libraries:
  - OpenCV for face detection
  - face-recognition for comparing faces
  - dlib for facial feature processing

Install dependencies with:
```bash
pip install opencv-python face-recognition dlib
```
## How It Works

### Registration Mode
- Type **'y'** to register a face.
- Move your head in different directions (left, right, up, down) to capture multiple photos from various angles.
- These photos are saved and used for future recognition.

### Login Mode
- Type **'n'** to log in.
- A single photo of your face is captured and compared to the saved faces for identity verification.

### Error Handling
- If no face is detected, the system will alert you with an error message.
- Invalid inputs (anything other than 'y' or 'n') will be handled and prompt the user to provide the correct input.

## Key Functions

- **`capture_face(multiple=False, num_photos=1)`**: Captures a face, either for registration (multiple photos) or login (one photo).
  
- **`save_faces(captured_faces, user_name)`**: Saves the captured photos of the user for future recognition.

- **`recognize_face(captured_face)`**: Compares the captured face with saved faces to verify the user's identity.

## Future Improvements

- **Improve Accuracy**: Capture more photos during registration to enhance the recognition process or integrate more advanced face recognition techniques.

- **Liveness Detection**: Add liveness detection to ensure the face presented is real, preventing spoofing attempts (e.g., using a photo).

- **Web/Mobile Expansion**: Extend the system's functionality to web or mobile platforms to make it more accessible and versatile.

---

This system is designed to enhance security by making login easier and more efficient through facial recognition.
