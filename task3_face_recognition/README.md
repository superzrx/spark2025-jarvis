# Task3 Face Recognition
尝试注册和识别人脸

## Installation
conda配置和pip配置可以问gpt
```bash
conda create -n test_face_rec python=3.8
conda activate test_face_rec
pip3 install face_recognition opencv-python
```

## Test
* 图片测试
```bash
python3 test_image.py 
```

* 摄像头测试，需要先替换 your_face_image.png
```bash
python3 test_camera.py
```


## Acknowledgement
Most codes copied from [Github-ageitgey/face_recognition]https://github.com/ageitgey/face_recognition.
Please visit for more information and examples.