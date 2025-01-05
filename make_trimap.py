import os
import cv2
import numpy as np


def dilate_and_erode(mask_data, struc="ELLIPSE", size=(10, 10)):
    """
    膨胀侵蚀作用，得到粗略的trimap图
    :param mask_data: 读取的mask图数据
    :param struc: 结构方式
    :param size: 核大小
    :return:
    """
    if struc == "RECT":
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
    elif struc == "CROSS":  # 注意这里是CROSS，不是CORSS
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, size)
    else:
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, size)

    msk = mask_data / 255

    dilated = cv2.dilate(msk, kernel, iterations=1) * 255
    eroded = cv2.erode(msk, kernel, iterations=1) * 255
    res = dilated.copy()
    res[((dilated == 255) & (eroded == 0))] = 128
    return res


def process_images(input_folder, output_folder, size=10):
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # 检查文件扩展名
            mask_path = os.path.join(input_folder, filename)
            mask_data = cv2.imread(mask_path, 0)
            trimap = dilate_and_erode(mask_data, size=(size, size))
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, trimap)
            print(f"Processed and saved: {output_path}")


# 设置输入和输出文件夹路径
input_folder = "ICM57/ICM57/alpha"  # 假设所有mask都在这个文件夹
output_folder = "ICM57/ICM57/trimap/"  # 处理后的trimap将保存在这个文件夹

# 调用函数处理文件夹中的所有图片
process_images(input_folder, output_folder, size=15)