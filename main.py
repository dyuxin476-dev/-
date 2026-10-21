"""新生计算机入门实践：一个简单的图片处理程序。"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw


def create_demo_image(path: Path) -> None:
    """没有输入图片时生成一张简单的示例图片。"""
    image = Image.new("RGB", (640, 400), (235, 242, 250))
    draw = ImageDraw.Draw(image)
    draw.rectangle((80, 80, 560, 320), fill=(79, 129, 189), outline=(30, 60, 100), width=5)
    draw.ellipse((220, 120, 420, 280), fill=(244, 180, 80), outline=(120, 70, 20), width=5)
    draw.text((238, 185), "Hello GitHub", fill=(40, 40, 40))
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path)


def apply_filter(image: Image.Image, mode: str) -> Image.Image:
    if mode == "gray":
        return ImageOps.grayscale(image).convert("RGB")
    if mode == "blur":
        return image.filter(ImageFilter.GaussianBlur(radius=4))
    if mode == "brighten":
        return ImageEnhance.Brightness(image).enhance(1.35)
    raise ValueError(f"不支持的处理模式：{mode}")


def main() -> None:
    parser = argparse.ArgumentParser(description="对图片进行简单处理")
    parser.add_argument("--input", default="images/demo_input.png", help="输入图片路径")
    parser.add_argument("--output", default="images/demo_output.png", help="输出图片路径")
    parser.add_argument(
        "--mode",
        choices=("gray", "blur", "brighten"),
        default="gray",
        help="处理模式",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    if not input_path.exists():
        print(f"未找到输入图片，正在生成示例图片：{input_path}")
        create_demo_image(input_path)

    with Image.open(input_path) as image:
        result = apply_filter(image.convert("RGB"), args.mode)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        result.save(output_path)

    print(f"处理完成：{output_path}")


if __name__ == "__main__":
    main()

