import tkinter as tk
from tkinter import simpledialog
import cv2
import os
from datetime import datetime
import pandas as pd

# Initialize an empty DataFrame to store face records
face_records = pd.DataFrame(columns=['Name', 'Action', 'Timestamp', 'Images Folder'])

def save_to_excel():
    """Saves the face records DataFrame to an Excel file."""
    face_records.to_excel('face_records.xlsx', index=False, engine='openpyxl')

def capture_and_save_images(name):
    """Captures 500 images of the user's face, saves them in a dedicated folder, and shows live feed."""
    base_directory = "faces"
    person_directory = os.path.join(base_directory, name)
    
    if not os.path.exists(person_directory):
        os.makedirs(person_directory)

    video_capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    count = 0

    while count < 500:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to capture frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, f'{name}: {count+1}/500', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)
        
        cv2.imshow('Capture Faces', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        img_path = os.path.join(person_directory, f"{name}_{count}_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg")
        cv2.imwrite(img_path, frame)
        count += 1

    video_capture.release()
    cv2.destroyAllWindows()
    # Log the folder containing all images for the person
    global face_records
    new_record = pd.DataFrame({'Name': [name], 'Action': ['Captured 500 Images'], 'Timestamp': [datetime.now()], 'Images Folder': [person_directory]})
    face_records = pd.concat([face_records, new_record], ignore_index=True)
    save_to_excel()
    print(f"Captured 500 images for {name}. Folder: {person_directory}")

def add_face():
    """Triggers the image capture process for a new face."""
    name = simpledialog.askstring("Input", "Enter your name", parent=root)
    if name:
        capture_and_save_images(name)

# Set up the main application window
root = tk.Tk()
root.title("Face Recognition Database")
root.geometry("300x150")

# Add Face button
add_face_button = tk.Button(root, text="Add Face", command=add_face)
add_face_button.pack(pady=20)

root.mainloop()
