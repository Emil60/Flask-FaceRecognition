import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from time import sleep
from flskfaceapp.models import User, Images
from flskfaceapp import app, db
from flskfaceapp.forms import imageForm
from PIL import Image
from flask import flash




# def get_encoded_faces():
#     encoded = {}

#     for dirpath, dnames, fnames in os.walk("./flskfaceapp/photos"):
#         #print(fnames)
#         for f in fnames:
#             if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg"):
#                 face = fr.load_image_file("./flskfaceapp/photos/" + f)
#                 encoding = fr.face_encodings(face)[0]
#                 print(encoding,'\n','-------------------')
#                 user = Images.query.filter_by(photo_location = f).first()
#                 encoded[user.user_id] = encoding
#                 #print('encoded: ',encoded)
#     #print(encoding)
#     return encoded


def classify_face(im):
    faces_encoded = []
    known_face_names = []
    image = Images.query.all()
    for i in image:
        print('---------------\n',i.user_id)
        faces_encoded.append(i.photo_location)
        known_face_names.append(i.user_id)

    print(faces_encoded,'\n--------------------')
    img = cv2.imread(im, 1)

    face_locations = face_recognition.face_locations(img)
    print(face_locations)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)
    print("------------------------")
    print(unknown_face_encodings)
    print("-----------------------")
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"
        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        print(face_distances)
        #print(face_distances,faces_encoded, face_encoding, sep='\n')
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
    if name == "Unknown":
        form = imageForm()
        user = User(name = form.name.data)
        db.session.add(user)
        db.session.commit()
        face = fr.load_image_file(im)
        encoding = fr.face_encodings(face)[0]
        face_land_marks = list(encoding)
        image = Images(photo_location =  face_land_marks, user_id = user.user_id)
        db.session.add(image)
        db.session.commit()
        flash("your photo inserted to Database successfully")
    return name


def classify_face_with_cam():
    faces_encoded = []
    known_face_names = []
    image = Images.query.all()
    for i in image:
        print('---------------\n', i.user_id)
        faces_encoded.append(i.photo_location)
        known_face_names.append(i.user_id)

    print(faces_encoded,'\n--------------------')
    ramp_frames = 30
    camera = cv2.VideoCapture(0)

    def get_image():
        retval, im = camera.read()
        return im
    # Ramp the camera - these frames will be discarded and are only used to allow v4l2
    # to adjust light levels, if necessary
    for i in range(ramp_frames):
        temp = get_image()
    print("Taking image...")
    camera_capture = get_image()
    file = "./flskfaceapp/temp/temp.jpg"

    cv2.imwrite(file, camera_capture)

    del(camera)
    img = cv2.imread("./flskfaceapp/temp/temp.jpg", 1)

    face_locations = face_recognition.face_locations(img)
    print(face_locations)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)
    print("------------------------")
    print(unknown_face_encodings)
    print("-----------------------")
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"
        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        print(face_distances)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
    if name == "Unknown":
        form = imageForm()
        user = User(name = form.name.data)
        db.session.add(user)
        db.session.commit()
        face = fr.load_image_file("./flskfaceapp/temp/temp.jpg")
        encoding = fr.face_encodings(face)[0]
        face_land_marks = list(encoding)
        image = Images(photo_location =  face_land_marks, user_id = user.user_id)
        db.session.add(image)
        db.session.commit()
        flash("your photo inserted to Database successfully")
    return name
