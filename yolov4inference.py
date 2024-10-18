# import cv2
# import time
# import ntplib

# def calculate_latency(input_rtsp_url, output_rtsp_url):
#     input_cap = cv2.VideoCapture(input_rtsp_url)
#     output_cap = cv2.VideoWriter(output_rtsp_url, cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))

#     ntp_client = ntplib.NTPClient()

#     input_latencies = []
#     output_latencies = []

#     while True:
#         ret, frame = input_cap.read()
#         if not ret:
#             break

#         # Get the timestamp for input stream
#         input_timestamp = ntp_client.request('pool.ntp.org').tx_time

#         # Write the frame to the output stream
#         output_cap.write(frame)

#         # Get the timestamp for output stream
#         output_timestamp = ntp_client.request('pool.ntp.org').tx_time

#         # Calculate latency for both input and output
#         input_latency = time.time() - input_timestamp
#         output_latency = time.time() - output_timestamp

#         input_latencies.append(input_latency)
#         output_latencies.append(output_latency)

#         # Print or store latency for analysis
#         print(f"Input Stream Latency: {input_latency:.2f} seconds")
#         print(f"Output Stream Latency: {output_latency:.2f} seconds")

#     # Release the resources
#     input_cap.release()
#     output_cap.release()

#     # Calculate the average latencies
#     avg_input_latency = sum(input_latencies) / len(input_latencies)
#     avg_output_latency = sum(output_latencies) / len(output_latencies)

#     # Display the average latency values
#     print(f"Average Input Stream Latency: {avg_input_latency:.2f} seconds")
#     print(f"Average Output Stream Latency: {avg_output_latency:.2f} seconds")

# if __name__ == "__main__":
#     input_rtsp_url = "rtsp://192.168.5.10:8554/compose-cam1"
#     output_rtsp_url = "rtsp://192.168.5.10:6000/ds-test1"
#     calculate_latency(input_rtsp_url, output_rtsp_url)
# bcc_recipients: ["gireesh.bm@satyaki.co.in","poojavishal916@gmail.com","pooja.s@satyaki.co.in"]

# host_ip: 192.168.5.10
# server_name: server-01
# shift_time:
#   shift_start: 10:00:00 AM
#   shift_end: 10:00:00 PM
# sender_email: reporting@bluepolicy.de
# sender_password: 5c3150bca64f62fd8b5ef63bfccec1695ce02249bc17d8bd81440c5dc0f1b74f
# receiver_emails:
# - satyakidevteam@gmail.com
# bcc_recipients:
# - gireesh.bm@satyaki.co.in
# - satyaki.arkun@gmail.com
# vision_dns: lvep24-server-1
# log_level: INFO
# Test_mode: true
# EngineType_lvep: 32
# EngineType_psda: 16
# BuildEngine_lvep: false
# BuildEngine_psda: true
# number_of_streams: 2
# DatabseTimeout: 1
# Store_Jammed_Videos: true
# Store-JSON-DB: true
# width: 640
# height: 480
# defaultVisionData:
#   username: root
#   password: admin
#   gpio_id: '1'
#   ip: 172.17.0.1
# roiType: 0
# MIN_CONFIDENCE: 0.5
# MAX_CONFIDENCE: 1.0
# FPS: 5
# JAMMED_TIMEOUT: 3
# Alarm_Environment: 0
# RTSP_OUTPUT_PORT: 6000
# lvep_select: true
# psda_select: false
# lvep_build_complete: true
# psda_build_complete: false
# gcore_ip: 192.168.1.13
# gcore_msg_mode: string
# gcore_port: 13007
# gcore_health_trigger: 60
# gbridge_connection_check: 5000
# lvep_cameras:
#   cam1:
#     cam_global_id: 86
#     inputs: rtsp://172.17.0.1:8554/compose-cam1
#     outputs: rtsp://172.17.0.1:6000/ds-test1
#     category: '0'
#     alarm_url: rtsp://root:root@192.168.1.8:554//axis-media/media.amp?videocodec=h264&streamprofile=satyakiCam
#     belt_stop_timer: 30
#     alarm_end_timer: 5
#     Minimum_Jammed_Boxes: 5
#     Alarm_detection_time: 1
#     roi:
#       x: 394
#       y: 153
#       w: 274
#       h: 442
#   cam2:
#     cam_global_id: 88
#     inputs: rtsp://172.17.0.1:8554/compose-cam2
#     outputs: rtsp://172.17.0.1:6000/ds-test2
#     category: '0'
#     alarm_url: rtsp://root:root@192.168.1.8:554//axis-media/media.amp?videocodec=h264&streamprofile=satyakiCam
#     belt_stop_timer: 30
#     alarm_end_timer: 5
#     Minimum_Jammed_Boxes: 4
#     Alarm_detection_time: 1
#     roi:
#       x: 355
#       y: 131
#       w: 276
#       h: 556
# psda_cameras: {}
# key: 27690bef6c52c56ee3f4b272d67a3f087a60b1f77ec33a4623e29fd2b76435e7
# iv: 53e96107d62df7f85607029f80f30bb0


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load YOLO model
net = cv2.dnn.readNet("/home/satyaki/lvep24/lvep24_default_data/Models/deepstream_lvep/yolo-obj_best.weights",
                      "/home/satyaki/lvep24/lvep24_default_data/Models/deepstream_lvep/yolo-obj.cfg")

# Manually define some class names (optional)
classes = ["class1", "class2", "class3"]  # Add custom class names if known, or leave empty for no labels

# Setup input MP4 file
input_video_path = "/home/satyaki/helper-scripts/rtsp-streamer/Server2-Cam3-Global65__27082024.mp4"  # Path to your input video file
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
