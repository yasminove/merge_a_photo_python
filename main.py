from PIL import Image

img = Image.open('baby.jpeg')

r, g, b = img.split()

new_image = Image.merge('RGB', (r, g, b))

new_image.show()
