# coding:utf-8
import cv2
faceCascade = cv2.CascadeClassifier('classify/haarcascade_frontalcatface.xml')


# parameter specification
#   cat_path:         path to the cat's photo which is ready to be compared
#   cut_cat_path:     path where saves the cat photo cut
#   face_cascade_cat: training data set of cat
def cut_cat(cat_path='upload/cut_cat.jpg', cut_cat_path='dist/cut_cat.jpg', face_cascade_cat=faceCascade):
    img = cv2.imread(cat_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade_cat.detectMultiScale(
        gray,
        scaleFactor=1.10,
        minNeighbors=3,
        minSize=(5, 5),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for(x, y, w, h) in faces:
        crop_img = img[y:y+h, x:x+w]
        res = cv2.resize(crop_img, (128, 128), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(cut_cat_path, res)
        cv2.rectangle(img, (x, y), (x+w, y+w), (0, 255, 0), 2)

