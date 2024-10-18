import cv2
import numpy as np

# Load YOLO model
net = cv2.dnn.readNet("{path}.weights", "{path}.cfg")

# Load the class labels
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Setup RTSP stream
rtsp_url = "rtsp://{ip_address}}:8554/compose-cam1"
cap = cv2.VideoCapture(rtsp_url)

# Get the width, height, and frames per second of the input video stream
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define codec and create VideoWriter object
video_out = cv2.VideoWriter("cam1_output.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

# Debug: Check if 'video_out' is a VideoWriter object
print(type(video_out))

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
            label = str(classes[class_ids[i]])
            confidence = confidences[i]
            color = (0, 255, 0)  # You can choose different colors for different classes
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{label} {confidence:.2f}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Debug: Print the type of 'frame' and check if 'video_out' is still a VideoWriter object
    print(type(frame))
    print(type(video_out))

    # Write the frame to the output file
    video_out.write(frame)  # This is where the frame is saved to the video file

    # (Optional) Display the frame
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
video_out.release()
cv2.destroyAllWindows()
