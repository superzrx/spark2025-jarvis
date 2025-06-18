# 环境识别demo
<img src="https://github.com/openvinotoolkit/openvino_notebooks/assets/29454499/c4dee890-6a18-4c45-8423-809653c85cb0" width=300>


## 主要内容
本项目旨在通过计算机视觉技术，实现对图像内容的场景理解，并对场景中的关键物体进行精准的检测与分类。

## 环境配置（这个damo与task1中使用的环境一致，如果你已经安装过task1中的环境，可直接跳到第五步）
**第1步：安装 Conda**

如果你还没有安装 Conda，请根据你的操作系统（Windows, macOS, Linux）从官网下载并安装。
* [conda下载地址](https://www.anaconda.com/download)

**第2步：打开Anaconda Powershell Prompt**
![alt text](image-1.png)
在应用中的Anaconda3下面找到Anaconda Powershell Prompt并打开

**第3步：创建新的conda环境并激活**
```bash
conda create -n openvino_env python=3.8
conda activate openvino_env
```
**第4步:安装依赖库**
```bash
python -m pip install --upgrade pip==21.3.*
pip install -r requirements.txt
```
**第5步：启动jupyter notebook**
```bash
jupyter lab detectron2.ipynb
```

## 试着找些素材来测试一下吧！
可选素材网站：[pexels](https://www.pexels.com/)