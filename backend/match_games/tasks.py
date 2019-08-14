from PIL import Image


def compress_image(image_path):
    image = Image.open(image_path)
    image.thumbnail((100, 100))
    image.save(image_path)
