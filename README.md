# 新生计算机入门实践

这是一个面向新生的简单 Python 图片处理项目，用来熟悉：

- 项目文件和文件夹的基本结构；
- Python 程序的运行方式；
- `requirements.txt` 的作用；
- Git 和 GitHub 的基本操作；
- Markdown 文档和图片展示。

## 一、任务要求

1. Fork 本项目到自己的 GitHub 账号。
2. Clone 项目到本地电脑。
3. 安装项目依赖并运行程序。
4. 使用一张自己的图片进行处理。
5. 将处理后的图片保存到 `images/` 文件夹。
6. 在 `student_submission/` 文件夹中新建自己的实验记录。
7. 提交修改并发起 Pull Request。

本题为入门附加项，不要求编写复杂算法。能够运行程序、保存结果并完成一次 GitHub 提交即可。

## 二、项目结构

```text
新生计算机入门实践/
├── README.md
├── main.py
├── requirements.txt
├── images/
│   ├── input.jpg
│   └── output.jpg
└── student_submission/
    └── example.md
```

## 三、运行方法

建议使用 Python 3.9 或更高版本。

```bash
git clone 项目地址
cd 新生计算机入门实践
pip install -r requirements.txt
python main.py --input images/input.jpg --output images/output.jpg --mode gray
```

如果暂时没有自己的图片，可以先运行：

```bash
python main.py
```

程序会自动生成一张示例图片，并保存处理结果。

## 四、可用的图片处理模式

```bash
python main.py --mode gray       # 黑白效果
python main.py --mode blur       # 模糊效果
python main.py --mode brighten   # 变亮效果
```

## 五、Git 提交示例

```bash
git checkout -b feature/自己的名字
git add .
git commit -m "add: 添加个人实验记录"
git push origin feature/自己的名字
```

然后在 GitHub 页面上发起 Pull Request。

## 六、提交内容

请在 `student_submission/` 文件夹中新建一个以自己名字命名的 Markdown 文件，例如：

```text
student_submission/张三.md
```

内容可以参考 `student_submission/example.md`。

