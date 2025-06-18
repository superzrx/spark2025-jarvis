import wenet
import os

# --- 核心路径配置 ---
# 获取当前脚本文件 (asr_demo.py) 所在的目录的绝对路径 (src 目录)
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 获取 src 目录的上一级目录, 即项目根目录 (task2_speech_module)
_PROJECT_ROOT = os.path.dirname(_SCRIPT_DIR)

# --- 配置 ---
# 数据文件夹位于项目根目录下
TEST_DATA_DIR = os.path.join(_PROJECT_ROOT, "test_asr_data")
# 指定要识别的音频文件名
AUDIO_FILENAME = "01_macbook.wav"

def run_asr_demo():
    """
    运行语音识别演示的主函数。
    """
    print("--- 实时语音识别演示 ---")
    
    # 1. 检查音频文件是否存在
    audio_path = os.path.join(TEST_DATA_DIR, AUDIO_FILENAME)
    if not os.path.exists(audio_path):
        print(f"错误：找不到音频文件 '{audio_path}'。")
        print("请确保你已经从网盘下载了数据，并将其解压到了 'task2_speech_module/test_asr_data' 目录下。")
        return

    # 2. 加载预训练的 WeNet 模型
    try:
        # 使用 'chinese' 别名来加载一个推荐的中文模型
        # wenet.load_model() 会自动从云端下载并缓存模型
        print("正在加载中文模型 'chinese' ...")
        model = wenet.load_model('chinese')
        print("模型加载成功！")
    except Exception as e:
        print(f"模型加载失败: {e}")
        print("请检查你的网络连接。初次运行时需要下载模型文件。")
        return

    # 3. 对指定的音频文件进行语音识别
    try:
        print(f"\n正在识别文件: {audio_path} ...")
        # model.transcribe() 是核心的识别函数
        result = model.transcribe(audio_path)
        
        # 4. 打印识别结果
        print("\n--- 识别结果 ---")
        print(f"音频文件: {AUDIO_FILENAME}")
        # result 字典中 'text' 键对应的值就是识别出的文字
        print(f"识别文本: {result['text']}")
        print("------------------\n")
        
    except Exception as e:
        print(f"语音识别过程中发生错误: {e}")

if __name__ == "__main__":
    run_asr_demo() 