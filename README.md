# Flask-FaceRecognition
##Warning 
The project can only be run in linux platforms.

## About
In this project I have implemented ML technology (Face recognition) in Web Programming
Face Recognition technology helps us to identify the person from different photos. It gets the locations and outlines of each person’s eyes, nose, mouth and chin and recognises who appears in each photo.

##Web Side
In the simple layout user needs to fill the textbox and press the button and his web cam will take a photo. Then face recognition will find landmarks of the face and it will look to the similar landmarks in the database(sqlite). If the person has data (face landmarks) in our database small label will going to appear on the screen, otherwise his landmarks will be inserted to the DB. 
(with small changes in project also user can upload a photo from his device also)
This small project can be upgraded and can be used in log in or register with face recognition purposes in professional web sites.

##Requirements
For Face Recognition part libraries need to be installed:
`python open cv`
`python face recognition`
`cmake`
`numpy`
`PIL`