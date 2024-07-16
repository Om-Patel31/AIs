import cv2

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize webcam
cap = cv2.VideoCapture(0)

# Load known face for face recognition (replace this with your own known face)
known_face = cv2.imread("known_face.jpg", cv2.IMREAD_GRAYSCALE)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Perform face recognition
        face_roi = gray[y:y+h, x:x+w]
        # Compare the detected face with the known face
        # You can use different face recognition techniques here
        
        # Example: Compare histograms
        match = cv2.compareHist(cv2.calcHist([known_face], [0], None, [256], [0, 256]), cv2.calcHist([face_roi], [0], None, [256], [0, 256]), cv2.HISTCMP_CORREL)
        
        # Unlock laptop if the detected face matches the known face
        if match > 0.8:  # Adjust threshold as needed
            print("Face recognized. Opening laptop.")
            # Add code to unlock your laptop here
            # For example, you can simulate pressing the Enter key
            # using pyautogui or similar libraries
            
    # Display the resulting frame
    cv2.imshow('Face Recognition', frame)

    # Break the loop when 'Esc' is pressed
    if cv2.waitKey(1) == 27:
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()