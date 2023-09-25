import cv2
import pickle

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Load the face recognizer and the trained data into the program
recognise = cv2.face.LBPHFaceRecognizer_create()
recognise.read("trainner.yml")

labels = {}  # Dictionary

# Opening labels.pickle file and creating a dictionary containing the label ID and the name
with open("labels.pickle", 'rb') as f:
    og_label = pickle.load(f)
    labels = {v: k for k, v in og_label.items()}
    print(labels)

unrecognized_count = 0

while True:
    check, frame = video.read()

    # Check if the frame is valid
    if not check:
        break

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    for x, y, w, h in face:
        face_save = gray[y:y + h, x:x + w]

        # Predicting the face identified
        ID, conf = recognise.predict(face_save)
        if conf >= 65 and conf <= 115:
            print(ID)
            print(labels[ID].title())
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 4)
        else:
            label = "Unrecognized"
            print("Unrecognize")  # Add this line to print "Unrecognize" for unrecognized faces
            unrecognized_count += 1
            print("Total Unrecognized Faces:", unrecognized_count)
        cv2.putText(frame, labels[ID], (x - 10, y - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (18, 5, 255), 2, cv2.LINE_AA)


    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if unrecognized_count == 5:
        break

video.release()
cv2.destroyAllWindows()
