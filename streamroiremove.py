import numpy as np
import cv2


input_video_path = "input.mp4"  
output_video_path = "result.mp4" 
cap = cv2.VideoCapture(input_video_path)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))
while True:
    ret, frame = cap.read()
    if not ret:
        break  
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red_1 = np.array([0, 120, 70])
    upper_red_1 = np.array([10, 255, 255])
    lower_red_2 = np.array([170, 120, 70])
    upper_red_2 = np.array([180, 255, 255])
    mask_red1 = cv2.inRange(hsv_image, lower_red_1, upper_red_1)
    mask_red2 = cv2.inRange(hsv_image, lower_red_2, upper_red_2)
    red_mask = cv2.bitwise_or(mask_red1, mask_red2)
    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
    lower_other = np.array([90, 100, 100])
    upper_other = np.array([140, 255, 255])
    other_mask = cv2.inRange(hsv_image, lower_other, upper_other)
    combined_mask = cv2.bitwise_or(red_mask, green_mask)
    combined_mask = cv2.bitwise_or(combined_mask, other_mask)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, text_mask = cv2.threshold(gray_frame, 180, 255, cv2.THRESH_BINARY)
    full_mask = cv2.bitwise_or(combined_mask, text_mask)
    kernel = np.ones((3, 3), np.uint8)
    full_mask_dilated = cv2.dilate(full_mask, kernel, iterations=2)
    frame_no_boxes_and_text = cv2.inpaint(frame, full_mask_dilated, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
    out.write(frame_no_boxes_and_text)
cap.release()
out.release()

print(f"The video with all boxes and text removed has been saved at: {output_video_path}")
