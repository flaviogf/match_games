from PIL import Image


def compress_image(image_path):
    image = Image.open(image_path)
    image.thumbnail((300, 300))
    image.save(image_path)
