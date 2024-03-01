# AlterEgo

The Alter Ego project is a Python-based AI robot designed to run on Raspberry Pi and Arduino. It is structured to handle a variety of tasks, making it a versatile and comprehensive solution for robotics enthusiasts and developers.



# Project Structure

```plaintext
alterego/
│
├── main.py
│
├── movement/
│   ├── __init__.py
│   ├── motors.py
│   └── sensors.py
│
├── device_control/
│   ├── __init__.py
│   ├── devices.py
│   └── controllers.py
│
├── audio_recognition/
│   ├── __init__.py
│   ├── microphone.py
│   └── audio_processing.py
│
├── vision_recognition/
│   ├── __init__.py
│   ├── camera.py
│   └── image_processing.py
│
└── tests/
    ├── __init__.py
    ├── test_movement.py
    ├── test_device_control.py
    ├── test_audio_recognition.py
    └── test_vision_recognition.py