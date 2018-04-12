# coding:utf-8
import cv2
import cut_human as human

x = range(30)
cut_cat_path = 'dist/cut_cat.jpg'
faceCascade_cat = cv2.CascadeClassifier('classify/haarcascade_frontalcatface.xml')
faceCascade_human = cv2.CascadeClassifier('classify/haarcascade_frontalface_default.xml')


# 计算方差
def get_ss(list):
    avg = sum(list) / len(list)  # 计算平均值
    ss = 0  # 定义方差变量ss，初值为0
    # 计算方差
    for l in list:
        ss += (l - avg) * (l - avg) / len(list)
    return ss  # 返回方差


# 获取每行像素平均值
def get_diff(img):
    side_length = 30  # 定义边长
    img = cv2.resize(img, (side_length, side_length), interpolation=cv2.INTER_CUBIC)  # 缩放图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度处理
    avg_list = []  # avg_list列表保存每行像素平均值
    # 计算每行均值，保存到avg_list列表
    for i in range(side_length):
        avg = sum(gray[i]) / len(gray[i])
        avg_list.append(avg)
    return avg_list  # 返回avg_list平均值


def get_avg(diff1, diff11):
        diff_list = []
        for i in range(30):
            avg1 = diff1[i]-diff11[i]
            diff_list.append(avg1)
        return diff_list


# parameter specification
#   human_path:         path to the human's photo which is newly uploaded
#   cut_human_path:     path where saves the human photo cut
# return specification
#   return 1: success
#   return 0: fail to calculate the similarity
def calculate_similarity(human_path, cut_human_path):
    result = human.cut_human(human_path, cut_human_path, faceCascade_human)
    if result == 0:
        return 0
    else:
        img_cat = cv2.imread(cut_cat_path)
        img_human = cv2.imread(cut_human_path)

        # 读取测试图片 for human
        diff_human = get_diff(img_human)
        print('img_human:', get_ss(diff_human))

        # 读取测试图片  for cat
        diff_cat = get_diff(img_cat)
        print('img_cat:', get_ss(diff_cat))

        result_value = get_avg(diff_human, diff_cat)
        print('similarity', get_ss(result_value))

        return 1



