import cv2

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

group_photo = cv2.imread('group-photo.webp')
gray_photo = cv2.cvtColor(group_photo, cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(gray_photo, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
    cv2.rectangle(group_photo, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('Group Photo', group_photo)

# cv2.imwrite('group-photo-copy.webp', gray_photo)

cv2.waitKey(0)
cv2.destroyAllWindows()