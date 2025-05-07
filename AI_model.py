import cv2
import os
from deepface import DeepFace
import uuid
import numpy as np

# Folder where faces are stored
FACES_FOLDER = "faces"

# Number of photos to capture for new users
NUM_PHOTOS = 5

# Make sure faces folder exists
os.makedirs(FACES_FOLDER, exist_ok=True)

def capture_face(multiple=False, num_photos=5):
    """Capture face(s) from webcam."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Cannot access the webcam.")
        return None

    print("Press 's' to capture face, 'q' to quit.")

    captured_faces = []
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to read from webcam.")
            break

        cv2.imshow("Face Capture", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            captured_faces.append(frame.copy())
            count += 1
            print(f"📸 Captured photo {count}/{num_photos}")
            if multiple and count >= num_photos:
                break
            if not multiple:
                break
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if not captured_faces:
        return None

    return captured_faces if multiple else captured_faces[0]

def save_faces(images, user_name):
    """Save multiple captured face images."""
    if isinstance(images, list):
        for idx, img in enumerate(images):
            filepath = os.path.join(FACES_FOLDER, f"{user_name}_{idx+1}.jpg")
            cv2.imwrite(filepath, img)
            print(f"✅ Saved {filepath}")
    else:
        filepath = os.path.join(FACES_FOLDER, f"{user_name}.jpg")
        cv2.imwrite(filepath, images)
        print(f"✅ Saved {filepath}")

def recognize_face(image):
    """Compare captured image with saved faces."""
    temp_capture_path = "temp_capture.jpg"
    cv2.imwrite(temp_capture_path, image)

    for filename in os.listdir(FACES_FOLDER):
        known_face_path = os.path.join(FACES_FOLDER, filename)

        try:
            result = DeepFace.verify(img1_path=temp_capture_path, img2_path=known_face_path, enforce_detection=False)

            if result["verified"]:
                # Extract username (before underscore if exists)
                user_name = os.path.splitext(filename)[0].split("_")[0]
                print(f"✅ Face recognized as: {user_name}")
                os.remove(temp_capture_path)  # Clean up temporary file
                return user_name
        except Exception as e:
            print(f"⚠️ Error verifying {filename}: {e}")

    print("❌ Face not recognized.")
    os.remove(temp_capture_path)
    return None

def main():
    mode = input("Is this your first time? (y/n): ").strip().lower()

    if mode == 'y':
        user_name = input("Enter your username: ").strip()
        print(f"📸 Please move your head slowly left, right, up, down while capturing photos...")
        captured_faces = capture_face(multiple=True, num_photos=NUM_PHOTOS)
        if captured_faces:
            save_faces(captured_faces, user_name)
        else:
            print("❌ No face captured.")

    elif mode == 'n':
        captured_face = capture_face(multiple=False)
        if captured_face is not None:
            recognize_face(captured_face)
        else:
            print("❌ No face captured.")

    else:
        print("❌ Invalid input. Please type 'y' or 'n'.")

if __name__ == "__main__":
    main()
