# 新生计算机入门实践

这是一个面向新生的简单 Python 图片处理项目，用来熟悉项目文件、Python 程序、GitHub 项目和图片处理的基本概念。

## 一、任务目标

本次附加项只需要大家按照步骤把程序运行起来，看到图片处理结果即可：

1. 下载项目到电脑；
2. 找到项目所在的文件夹；
3. 安装项目依赖；
4. 运行图片处理程序；
5. 查看处理后的图片；
6. 尝试更换一种处理效果。

不要求编写复杂算法，也不要求提交代码、创建分支或发起 Pull Request。

## 二、项目结构

```text
新生计算机入门实践/
├── README.md
├── main.py
├── compare.py
├── requirements.txt
└── images/
    ├── input.jpg
    └── output.jpg
```

## 三、基础概念说明

### 1. 什么是项目文件夹

一个计算机项目通常由多个文件组成。代码文件负责运行程序，依赖文件记录需要安装的工具，说明文件告诉别人如何使用项目。

### 2. 什么是 Python

Python 是一种编程语言。`main.py` 是本项目的主程序，运行它就会读取图片、进行处理，并保存处理结果。

### 3. 什么是第三方库

Python 自带一些基础功能，但图片处理需要额外工具。本项目使用的 Pillow 是一个图片处理库，可以帮助程序打开、修改和保存图片。

### 4. `requirements.txt` 是做什么的

`requirements.txt` 是项目的依赖清单。本项目基础功能使用 Pillow，拓展功能还使用 NumPy 和 Matplotlib：

```text
Pillow>=10.0.0
numpy>=1.24.0
matplotlib>=3.7.0
```

安装命令如下：

```bash
pip install -r requirements.txt
```

### 5. 什么是 GitHub

GitHub 是一个用于保存和分享项目的网站。可以先把它理解为“别人把项目放在网上，我们把项目下载下来使用”。本次任务不要求提交代码。

### 6. 什么是 Git 和 Clone

Git 是一个记录项目修改历史的工具。Clone 的意思是把 GitHub 上的项目下载到自己的电脑。

```bash
git clone 项目地址
```

分支、提交和 Pull Request 属于后续协作内容，大家了解名称即可。

## 四、运行方法

以下步骤请按顺序执行。建议使用 Python 3.9 或更高版本。

### 第一步：下载项目

在 GitHub 项目页面点击绿色的 **Code** 按钮，选择 **Download ZIP**，下载后解压。

也可以使用命令下载：

```bash
git clone 项目地址
```

### 第二步：打开项目文件夹

打开刚才解压出来的项目文件夹，在文件夹空白处点击鼠标右键，选择“在终端中打开”。

如果使用命令行，也可以输入：

```bash
cd 项目文件夹名称
```

如果已经在项目文件夹中打开终端，这一步可以跳过。

### 第三步：安装依赖

```bash
pip install -r requirements.txt
```

### 第四步：准备图片

将提供的风景图片放入 `images` 文件夹，并命名为：

```text
input.jpg
```

### 第五步：运行程序

```bash
python main.py
```

程序会读取 `images/input.jpg`，并生成 `images/output.jpg`。

### 第六步：查看结果

打开 `images` 文件夹，查看处理后的图片 `output.jpg`。

## 五、尝试不同效果

```bash
python main.py --mode gray       # 黑白效果
python main.py --mode blur       # 模糊效果
python main.py --mode brighten   # 变亮效果
```

如果暂时没有输入图片，程序会自动生成一张示例图片。

## 六、拓展功能：生成图片对比图

基础程序使用 Pillow 读取和保存图片，NumPy 用来进行像素数组运算，Matplotlib 用来生成原图与处理结果的对比图。

先运行一次图片处理程序：

```bash
python main.py --mode brighten
```

再运行：

```bash
python compare.py
```

程序会在 `images` 文件夹中生成：

```text
images/comparison.png
```

这个拓展功能不是必须完成的，主要用于了解不同 Python 工具在一个项目中如何配合使用。

## 七、Git 命令简单了解

以下命令本次只作了解，不要求大家执行：

```bash
git status              # 查看项目当前状态
git add .               # 准备保存修改
git commit -m "说明"    # 保存一次修改记录
git push                # 上传修改
```

## 八、附加题

请按照“运行方法”完成操作，再回答下面的问题。不会的内容可以查阅资料。

### 题目 1：认识项目文件（2 分）

请说明下面三个文件分别有什么作用：

1. `README.md`
2. `main.py`
3. `requirements.txt`

### 题目 2：完成程序运行（3 分）

将指定图片放入 `images` 文件夹并命名为 `input.jpg`，安装依赖后运行：

```bash
python main.py
```

请提交程序成功运行的截图，并说明处理后的图片保存在哪里。

### 题目 3：比较图片处理效果（2 分）

分别运行下面三条命令：

```bash
python main.py --mode gray
python main.py --mode blur
python main.py --mode brighten
```

请说明三种模式分别对图片产生了什么效果。

### 题目 4：理解基本命令（2 分）

请说明下面两条命令的作用：

```bash
pip install -r requirements.txt
python main.py
```

### 题目 5：GitHub 基础（1 分）

请用自己的话解释：

1. GitHub 是什么？
2. Git 和 GitHub 有什么区别？
3. `git clone` 的作用是什么？

## 八、答题说明

本题不要求修改程序，也不要求创建分支、提交代码或发起 Pull Request。答题时只需要提交：

- 各小题的文字答案；
- 题目 2 的程序运行截图；
- 题目 3 的处理结果截图或简要说明。

重点是了解一个计算机项目如何下载、安装、运行和使用，而不是考察复杂编程能力。

