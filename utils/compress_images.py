from PIL import Image

def compress_images(image_path, path_to_save):
    foo = Image.open(image_path)
    print(foo.size)
    foo.save(path_to_save, quality=95)
