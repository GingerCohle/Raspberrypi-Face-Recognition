import face_recognition
import cv2
import numpy as np
import time
import os

# Confidence threshold
threshold = 0.4
# The size of image rescaling capture by cam
scale = 1
# set camera : 0->picamera, 1-> usb camera
video_capture = cv2.VideoCapture(0)
#load name set
known_facelist_txt = open('file_name_list.txt')
known_face_names = list(known_facelist_txt.read().split('\n')[:-1])
# load feature set
known_face_encodings = np.load('feature_list.npy')
# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    # Resize frame of video to 1/2 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=1/scale, fy=1/scale)
    # Convert the image from BGR color (which OpenCV uses) to Gray for faster face location (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    gray_small_frame = cv2.cvtColor(rgb_small_frame, cv2.COLOR_RGB2GRAY)
    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(gray_small_frame)
        # Extract feature from all faces
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            # Use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            print(face_distances)
            face_distances_1 = face_distances < threshold
            best_match_index = np.argmax(face_distances_1)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
        
    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/2 size
        top *= scale
        right *= scale
        bottom *= scale
        left *= scale

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
