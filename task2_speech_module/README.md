# WeNet - 一个简单易用的语音识别体验项目

[![License](https://img.shields.io/badge/License-Apache%202.0-brightgreen.svg)](https://opensource.org/licenses/Apache-2.0)

本项目基于业界领先的 WeNet 语音识别工具包，旨在为初学者提供一个简单、直接的自动语音识别（ASR）技术体验。你不需要了解复杂的算法细节，只需按照以下步骤，即可将一段中文音频文件转换成文字。

## 主要功能

*   **开箱即用**: 无需训练，直接使用强大的预训练中文模型。
*   **简单明了**: 仅需几行代码即可完成一次语音识别任务。
*   **体验核心技术**: 直观感受业界领先的语音识别技术是如何工作的。

---

## 目录

*   [环境配置](#环境配置)
*   [准备数据](#准备数据)
*   [运行演示](#运行演示)
*   [更多使用方式](#更多使用方式)
*   [致谢](#致谢)

---

## 环境配置

为了运行这个项目，你需要配置好 Python 环境并安装一些必要的库。我们强烈推荐使用 Conda 来管理环境，这样可以避免与你电脑上其他的 Python 项目产生冲突。

**第 1 步：安装 Conda**

如果你还没有安装 Conda，请根据你的操作系统（Windows, macOS, Linux）从官网下载并安装。推荐安装 Miniconda，它是一个轻量级的 Conda 版本。
*   [Miniconda 安装教程](https://docs.conda.io/en/latest/miniconda.html)

**第 2 步：创建并激活 Conda 环境**

打开你的终端（在 Windows 上是 "Anaconda Prompt" 或 "终端"，在 macOS/Linux 上是 "终端"）。

```bash
# 创建一个名为 "wenet_env" 的新环境，并指定使用 Python 3.10
# WeNet 的新版本使用了 Python 3.10+ 的语法特性，请确保版本正确
conda create -n wenet_env python=3.10

# 激活刚刚创建的环境
conda activate wenet_env
```
激活环境后，你会看到终端提示符前面多了 `(wenet_env)` 的字样，这表示你现在正处于这个独立的环境中。

**第 3 步：安装 PyTorch 和 WeNet**

请确保你已经激活了 `wenet_env` 环境，然后分步运行以下命令来安装核心的库。

```bash
# 1. 安装 PyTorch
# 注意：PyTorch 库比较大，下载和安装可能需要一些时间。
pip install torch

# 2. 安装 WeNet
# 这会直接从 WeNet 的 GitHub 仓库安装最新的版本。
pip install git+https://github.com/wenet-e2e/wenet.git
```

安装完成后，你的环境就配置好了！

---

## 准备数据

本项目需要一个音频文件来进行识别。由于音频文件通常较大，不适合直接放在代码仓库中。

你需要从网盘链接下载测试数据包 `test_asr_data.zip`。

**下载完成后，请执行以下操作：**

1.  解压 `test_asr_data.zip` 文件，你会得到一个名为 `test_asr_data` 的文件夹。
2.  将整个 `test_asr_data` 文件夹移动到 `task2_speech_module` 目录下。

完成后，你的项目目录结构应该如下所示：

```
Tencent Multi Modality/
└── task2_speech_module/
    ├── src/
    │   └── asr_demo.py
    ├── README.md
    └── test_asr_data/
        └── test.wav  <-- 这是你下载并解压后的音频文件
```

---

## 运行演示

确保你已经完成了 **环境配置** 和 **数据准备** 的所有步骤。

**特别说明：** 本项目**不需要**图形处理器（GPU），普通的电脑 CPU 即可成功运行。请放心体验。

在终端中，首先确认你已经激活了 Conda 环境 `(wenet_env)`，然后确保你的路径位于 `task2_speech_module` 文件夹内。

运行以下命令来启动我们为你准备好的演示脚本：

```bash
python src/asr_demo.py
```

程序启动后，你会看到以下输出：

1.  程序会提示开始加载模型。**初次运行**时，它会从网上自动下载预训练模型（约几百MB），这可能需要几分钟时间，请耐心等待。下载完成后，模型会缓存到本地，下次运行就会非常快。
2.  模型加载成功后，程序会开始识别 `test_asr_data/test.wav` 文件。
3.  几秒钟后，程序会在终端中打印出识别出的文字。

---

## 更多使用方式

除了运行 `src/asr_demo.py`，WeNet 包本身也提供了更直接的调用方式。下面介绍两种进阶用法。

### 1. 命令行方式 (Command-line usage)

安装好 WeNet 包之后，你的环境里就会有一个 `wenet` 命令。你可以用它来直接识别音频文件。

```bash
# --language chinese 指定使用中文模型
# 后面跟上你的音频文件路径
wenet --language chinese test_asr_data/test.wav
```
运行后，它会直接输出识别出的文本。这种方式非常快捷，适合快速验证。

### 2. Python 编程方式 (Python programming usage)

如果你想在自己的 Python 代码中集成语音识别功能，代码也非常简单。

```python
import wenet

# 1. 加载中文预训练模型
model = wenet.load_model('chinese')

# 2. 调用 transcribe 方法进行识别
result = model.transcribe('test_asr_data/test.wav')

# 3. 打印结果
print(result['text'])
```
这几行代码是实现语音识别功能的核心。

> **我们为什么推荐 `src/asr_demo.py`？**
> 对于初学者来说，我们编写的 `src/asr_demo.py` 脚本是最好的起点。因为它不仅包含了上述核心代码，还增加了许多对新手友好的功能，比如：
> *   **路径检查**：如果找不到音频文件，会给出清晰的提示。
> *   **加载提示**：在下载和加载模型时，会告诉你程序正在做什么。
> *   **格式化输出**：结果的呈现更清晰、易读。
>
> 当你熟悉了基本流程后，可以尝试用上面的两种方式来使用 WeNet！

---

## 致谢

本项目的实现和文档很大程度上参考了 WeNet 开源社区的成果。
*   Referred @https://github.com/wenet-e2e/wenet/blob/main/README.md 