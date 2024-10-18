import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load YOLO model
net = cv2.dnn.readNet("{path}.weights",
                      "{path}.cfg")

# Manually define some class names (optional)
classes = ["class1", "class2", "class3"]  # Add custom class names if known, or leave empty for no labels

# Setup input MP4 file
input_video_path = "{mp4filepath}.mp4"  # Path to your input video file
cap = cv2.VideoCapture(input_video_path)

# Get the width, height, and frames per second of the input video stream
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define codec and create VideoWriter object for output
output_video_path = "cam_output_video.mp4"  # Path to save the output video
video_out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Prepare the frame for YOLO
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    yolo_outs = net.forward(net.getUnconnectedOutLayersNames())

    # Initialize lists to hold the detected bounding boxes, confidences, and class IDs
    boxes = []
    confidences = []
    class_ids = []

    for detection_out in yolo_outs:
        for detection in detection_out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # Set a threshold to filter out weak detections
                center_x = int(detection[0] * frame_width)
                center_y = int(detection[1] * frame_height)
                w = int(detection[2] * frame_width)
                h = int(detection[3] * frame_height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply Non-Max Suppression
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Draw bounding boxes on the frame
    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]]) if classes else f"ID {class_ids[i]}"
            confidence = confidences[i]
            color = (0, 255, 0)  # Choose a color for the bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{label} {confidence:.2f}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Write the processed frame to the output file
    video_out.write(frame)

    # Convert the frame from BGR to RGB for displaying with matplotlib (Optional)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    plt.imshow(frame_rgb)
    plt.show(block=False)
    plt.pause(0.001)
    plt.clf()

    # Optional: Uncomment to display the frame with OpenCV (if GUI support is enabled)
    # cv2.imshow('Frame', frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release resources
cap.release()
video_out.release()
cv2.destroyAllWindows()
