Eye Tracking System using OpenCV and MediaPipe


# Overview

This project aims to create a real-time eye tracking system using computer vision techniques. By leveraging the capabilities of OpenCV and MediaPipe libraries, the system detects and tracks the movement of the user's eyes, allowing for intuitive control of the computer mouse cursor and enabling hands-free interaction with the computer.

Key features of the eye tracking system include:

- **Facial Landmark Detection**: The system utilizes the MediaPipe Face Mesh model to accurately detect and locate facial landmarks, including the eyes, eyebrows, and mouth.
  
- **Eye Movement Tracking**: By focusing on the landmarks corresponding to the eyes, the system continuously monitors the movement of the eyes in real-time. The movement of the right eye is mapped to control the horizontal and vertical movement of the cursor on the screen.

- **Blink Detection**: The system identifies blinks of the left eye to simulate mouse clicks. When the user blinks with their left eye, the system interprets it as a mouse click action, allowing for seamless interaction with graphical user interfaces and applications.

- **Customizable Settings**: Users have the option to customize various parameters such as cursor sensitivity, click timing thresholds, and calibration settings to adapt the system to their preferences and specific use cases.

This eye tracking system opens up possibilities for hands-free computer interaction, particularly for individuals with mobility impairments or those seeking alternative input methods. It can be used for a variety of applications including assistive technology, human-computer interaction research, and immersive gaming experiences.

With its intuitive interface and accurate tracking capabilities, the eye tracking system provides a user-friendly solution for controlling the computer mouse cursor and performing mouse click actions using eye movements and blinks.

**Requirements**
Python 3.x
OpenCV 
MediaPipe 
PyAutoGUI 

**Acknowledgments**
MediaPipe: https://mediapipe.dev/
OpenCV: https://opencv.org/
PyAutoGUI: https://pyautogui.readthedocs.io/
