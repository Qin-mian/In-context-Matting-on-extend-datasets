import os
from PIL import Image

def convert_png_to_jpg(folder_path):
    # 获取文件夹中所有PNG文件
    png_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]

    for png_file in png_files:
        png_path = os.path.join(folder_path, png_file)
        jpg_path = os.path.splitext(png_path)[0] + '.jpg'

        # 加载PNG图像
        img = Image.open(png_path)

        # 将图像转换为JPEG格式
        img.convert('RGB').save(jpg_path, 'JPEG')

        # 删除原PNG文件
        os.remove(png_path)

        print(f"Converted and replaced {png_file} with {os.path.basename(jpg_path)}")

if __name__ == "__main__":
    folder_path = 'image/image'  # 替换为你的文件夹路径
    convert_png_to_jpg(folder_path)