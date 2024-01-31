from PIL import Image, ImageDraw, ImageFont

ASCII_CHARS = '@%#*+=-:. '

def scale_image(image, new_width=100):
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image

def grayscale_image(image):
    return image.convert("L")

def map_pixels_to_ascii(image, range_width=25):
    pixels = image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[(pixel_value//range_width) % len(ASCII_CHARS)]
    return ascii_str

def convert_image_to_ascii(image_path):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    image = scale_image(image)
    image = grayscale_image(image)

    ascii_str = map_pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    return ascii_img

def create_image_from_ascii(ascii_img, font_size=10):
    ascii_lines = ascii_img.split("\n")
    image = Image.new(mode='L', size=(font_size*len(ascii_lines[0]), font_size*len(ascii_lines)), color=255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("cour.ttf", font_size)
    for i, line in enumerate(ascii_lines):
        draw.text((0, i*font_size), line, fill=0, font=font)
    return image

def main(image_path):
    ascii_img = convert_image_to_ascii(image_path)
    print(ascii_img)
    image = create_image_from_ascii(ascii_img)
    image.save('output.jpg')

image_path = r'path'
main(image_path)
