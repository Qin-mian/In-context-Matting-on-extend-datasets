## 环境依赖

运行环境：ubuntu20.04+cuda11.8

conda env create -f environment.yaml

开源的代码中安装包并不完整，已经补全并上传。

## 运行代码

根据以下步骤，在扩充的ICM57数据集上进行测试:

1. **🚀下载与训练模型:**
   
   从[此链接](https://pan.baidu.com/s/1HPbRRE5ZtPRpOSocm9qOmA?pwd=BA1c)下载预训练模型

2. **💻准备数据集:**
   确认已经下载了扩充的ICM57数据集

3. **📷通过数据集制作tripmap**
   
   运行project下的make_trimap.py

4. **🤗确保已经下载了stable-diffusion-2.1大模型**
   
   [stable-diffusion-2.1](https://huggingface.co/stabilityai/stable-diffusion-2-1)
   
   下载大模型后保存到本地，可通过project.config/eval.yaml更改模型所在文件目录

5. **🤖运行eval.py:**
   
   ```bash
   python eval.py
   ```
   
   可在eval.py中修改默认值或者直接使用命令：
   
   ```bash
   python eval.py --checkpoint PATH_TO_MODEL --save_path results/ --config             config/eval.yaml
   ```

6. **👀可视化结果展示**
    运行show_result.py，并输入图片名称

### 数据集

**扩充的ICM-57数据集**

- 于此处下载: [Extend ICM-57 Dataset](https://pan.baidu.com/s/1U6VvdPgXAR6ntGpodIvObQ?pwd=ysqd)

- **Installation Guide**:
  
  1. 下载完成后，将数据集解压到 project.datasets/ 目录下
  
  2. 确保 dataset 文件夹的结构如下：
     
     ```
     datasets/ICM57/
     ├── image
     └── alpha
     ```

### 联系方式 📇

Q_mian@hust.edu.cn
