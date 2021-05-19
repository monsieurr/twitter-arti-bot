from PIL import Image, ImageDraw
import random


def generate_random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color

def generate_simple_art(filename, random_color):
    img = Image.new('RGB', (3000, 3000), random_color)
    img.save(filename)


if __name__=="__main__":
    random_color = generate_random_color()

    size = [1000, 1000]

    generate_simple_art("test.png", random_color)

    random_color = '#%02X%02X%02X' % random_color
    print(random_color)
