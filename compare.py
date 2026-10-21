"""使用 Matplotlib 生成原图和处理结果的对比图。"""

from pathlib import Path

import matplotlib.pyplot as plt
from PIL import Image


INPUT_PATH = Path("images/input.jpg")
OUTPUT_PATH = Path("images/output.jpg")
COMPARE_PATH = Path("images/comparison.png")


def main() -> None:
    original = Image.open(INPUT_PATH)
    result = Image.open(OUTPUT_PATH)

    figure, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].imshow(original)
    axes[0].set_title("Original")
    axes[1].imshow(result)
    axes[1].set_title("Processed")

    for axis in axes:
        axis.axis("off")

    figure.tight_layout()
    figure.savefig(COMPARE_PATH, dpi=150)
    plt.close(figure)
    print(f"对比图已保存：{COMPARE_PATH}")


if __name__ == "__main__":
    main()

