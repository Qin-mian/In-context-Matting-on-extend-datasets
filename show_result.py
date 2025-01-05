import os
import matplotlib.pyplot as plt
from PIL import Image


def load_image(path, mode='RGB'):
    """加载图像，可指定模式"""
    return Image.open(path).convert(mode)


def plot_images(origin_folder, target_folder, pred_folder, file_name):
    # 构建文件路径
    origin_path = os.path.join(origin_folder, file_name + '.jpg')
    target_path = os.path.join(target_folder, file_name + '.png')
    pred_path = os.path.join(pred_folder, file_name + '.png')

    if os.path.exists(origin_path) and os.path.exists(target_path) and os.path.exists(pred_path):
        # 加载图像
        origin_img = load_image(origin_path, mode='RGB')
        target_img = load_image(target_path, mode='L')  # 灰度图
        pred_img = load_image(pred_path, mode='L')  # 灰度图

        # 获取图像尺寸
        origin_width, origin_height = origin_img.size
        target_width, target_height = target_img.size
        pred_width, pred_height = pred_img.size

        # 计算最大宽度和高度
        max_width = max(origin_width, target_width, pred_width)
        max_height = max(origin_height, target_height, pred_height)

        # 绘制图像
        fig, axes = plt.subplots(1, 3, figsize=(max_width / 100, max_height / 100))
        axes[0].imshow(origin_img)
        axes[0].set_title('Origin')
        axes[0].axis('off')

        axes[1].imshow(target_img, cmap='gray')
        axes[1].set_title('Target')
        axes[1].axis('off')

        axes[2].imshow(pred_img, cmap='gray')
        axes[2].set_title('Pred')
        axes[2].axis('off')

        plt.tight_layout()
        plt.show()
    else:
        print(f"One or more files not found: {file_name}")


if __name__ == "__main__":
    origin_folder = 'ICM57/ICM57/image'
    target_folder = 'ICM57/ICM57/alpha'
    pred_folder = 'ICM57/ICM57/extend_results'

    # 用户输入图片名称（不带后缀）
    file_name = input("Enter the image name (without extension): ")
    plot_images(origin_folder, target_folder, pred_folder, file_name)