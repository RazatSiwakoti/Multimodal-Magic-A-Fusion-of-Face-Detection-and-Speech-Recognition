import cv2   #using openCV library

# Loading the Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#defining a function that detect images 
def FaceDetection():

    #Opening default webcam of devices to capture images
    #need to change to 1 or 2 to use external webcame device(in my case I used external webcam and the value of 0 was changed to 1)
    cap = cv2.VideoCapture(0)

    print ("Press 'Q' to exit face detection and move to speech recognition anytime")

# To capture frames continuouslu from the webcam and detect faces, we use while loop
    while True:

        ret, frame = cap.read()     #Reading a frame from webcam

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Converting the frame to grayscale for processing

    # Detects faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('Detected Faces', frame)  # Display the processed frame with detected faces

    # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) == ord('q'):
            break
    
# TO Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()



