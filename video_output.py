import cv2
import time
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def scale_image(image, new_width=100): 
    (original_height, original_width) = image.shape[:2] 
    aspect_ratio = original_width/float(original_height) 
    new_height = int(new_width / aspect_ratio)
    dim = (new_width, new_height)
    return cv2.resize(image, dim, interpolation = cv2.INTER_AREA) 

def grayscale_image(image): 
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def ascii_image(image, characters="`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"):
    ascii_width = len(characters)
    ascii_img = ""
    for color in image:
        ascii_img += "".join([characters[int((ascii_width-1)*(color[i]/255))] for i in range(image.shape[1])]) + "\n"

    # Generate image from ASCII
    font = ImageFont.load_default()
    img = Image.new('1',(1,1))
    draw = ImageDraw.Draw(img)
    width, height = draw.textsize_multiline(ascii_img, font=font)
    img = Image.new('RGB', (width, height), color = (0, 0, 0))
    draw = ImageDraw.Draw(img)
    white = (255, 255, 255)
    draw.text((0, 0), ascii_img, fill=white, font=font)

    return np.array(img)

def main(output_path, capture_duration=10): 
    cap = cv2.VideoCapture(0) 
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
    
    ret, frame = cap.read() 
    if not ret: 
        print("Failed to read frame")
        return 

    height, width, _ = frame.shape
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (width, height))

    start_time = time.time() 
    while time.time() - start_time < capture_duration: 
        ret, frame = cap.read() 
        if not ret: 
            break 

        gray_frame = grayscale_image(frame) 
        scaled_frame = scale_image(gray_frame)
        ascii_frame = ascii_image(scaled_frame)
        out.write(ascii_frame)
    
    cap.release() 
    out.release()

if __name__ == '__main__': 
    main('output.mp4')
