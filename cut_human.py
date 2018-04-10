# coding:utf-8
import cv2


# parameter specification
#   human_path:         path to the human's photo which is newly uploaded
#   cut_human_path:     path where saves the human photo cut
#   face_cascade_human: training data set of human
def cut_human(human_path, cut_human_path, face_cascade_human):
    img = cv2.imread(human_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade_human.detectMultiScale(
        gray,
        scaleFactor=1.14,
        minNeighbors=5,
        minSize=(5, 5),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for(x, y, w, h) in faces:
        crop_img = img[y:y+h, x:x+w]
        res = cv2.resize(crop_img, (128, 128), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(cut_human_path, res)
        cv2.rectangle(img, (x, y), (x+w, y+w), (0, 255, 0), 2)
