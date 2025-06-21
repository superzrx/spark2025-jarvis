# Task4 Face Emotion Recognition
识别人脸表情

## Installation
conda配置和pip配置可以问gpt
```bash
conda create -n test_face_emotion python=3.8
conda activate test_face_emotion
pip3 install mtcnn opencv-python numpy pandas tensorflow keras keras_vggface imageio
```

## Test
* 摄像头测试，需要先从网盘下载trained_vggface.h5
```bash
python emotion_webcam_demo.py
```

## Acknowledgement
Codes copied from [Github-travistangvh/emotion-detection-in-real-time]https://github.com/travistangvh/emotion-detection-in-real-time.
Please visit for more information and examples.