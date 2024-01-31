import os
import time
import cv2
import numpy as np
import PIL.Image

ASCII_CHARS = '@%#*+=-:. '

def scale_image(image, new_width=100):
    (original_width, original_height) = image.shape
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width / 2) 
    dim = (new_width, new_height)
    new_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return new_image

def grayscale_image(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def map_pixels_to_ascii(image):
    pixels = image.flatten()
    ascii_str_lst = [ASCII_CHARS[pixel_value * len(ASCII_CHARS) // 256] for pixel_value in pixels]
    ascii_str = ''.join(ascii_str_lst)
    return ascii_str


def main(video_path):
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = grayscale_image(frame)
        gray = scale_image(gray, 80)
        ascii_str = map_pixels_to_ascii(gray)
        num_chars = gray.shape[1]
        ascii_str_len = len(ascii_str)
        ascii_img=""
        for i in range(0, ascii_str_len, num_chars):
            ascii_img += ascii_str[i:i+num_chars] + "\n"

        os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
        print(ascii_img)
        
        # time.sleep(0.0001)  # Control the speed of refreshing
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

video_path = "path_to_your_video.mp4"  # Replace with your video path
main(0)
