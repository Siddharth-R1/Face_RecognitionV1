# Face_RecognitionV1
Python project using OpenCV and Tkinter to capture and store facial images for recognition. Simple GUI prompts users to add their face; captures 500 images, logs data to Excel

## Features

- **Add Face**: Users can add their face to the database by clicking the "Add Face" button in the GUI.
- **Real-time Face Detection**: The application displays a live feed from the webcam and overlays rectangles on detected faces.
- **Data Storage**: Captured facial images are stored in dedicated folders within a directory named "faces". Information about the captured faces is logged in an Excel file for easy management.
- **Excel Export**: Users can export the logged data to an Excel file named "face_records.xlsx" for further analysis.
- **User Interaction**: The GUI provides a simple interface for users to input their name and initiate the face capture process.

## Prerequisites

Before running the code, make sure you have the following dependencies installed:

- Python 3.x
- OpenCV (opencv-python)
- Pandas
- Tkinter

Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

# Usage
Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/face-recognition-database.git
```

Navigate to the project directory:
```bash
cd face-recognition-database
```
Run the script:
```bash
python main.py
```
Click the "Add Face" button in the GUI and follow the prompts to capture your face.
Once the face capture process is complete, the captured images and relevant data will be stored in the "faces" directory.

# Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Make your changes.
4. Commit your changes (git commit -am 'Add some feature').
5. Push to the branch (git push origin feature/your-feature).
6. Create a new pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for details.
