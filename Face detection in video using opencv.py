import cv2

def FaceDetection(video, name):
    currentFrame = 0

    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    while(True):
        ret, frame = video.read()

        if frame is not None:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor = 1.05,
                minNeighbors = 18,
                minSize = (65, 65)
            )

        if ret:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                name2 = 'C:\\Users\\Felip\\Videos\\data\\' + name + '-' + str(currentFrame) + '.jpg'

                currentFrame += 1

                cv2.imwrite(name2, frame)
        else:
            return True


def Exec():
    cam = cv2.VideoCapture('C:\\Users\\Felip\\Videos\\videos testes\\VideoTeste.mp4')

    FaceDetection(cam, 'opencv')


Exec()
