#!/bin/bash

# Set backup directory
BACKUP_DIR=~/log_backups/$(date +%F)
mkdir -p "$BACKUP_DIR"

echo "[+] Collecting Docker container logs..."
docker logs -ft service_video_processing_lvep &> "$BACKUP_DIR/lveplogs.txt"
docker logs -ft service_video_processing_psda &> "$BACKUP_DIR/psdalogs.txt"
docker logs -ft service_alarm_manager &> "$BACKUP_DIR/alarmlogs.txt"

echo "[+] Copying syslog and kern.log..."
sudo cp /var/log/syslog "$BACKUP_DIR/syslog" 2>/dev/null
sudo cp /var/log/kern.log "$BACKUP_DIR/kern.log" 2>/dev/null
sudo cp /var/log/messages "$BACKUP_DIR/messages" 2>/dev/null

echo "[+] Archiving full /var/log directory..."
sudo tar -czvf "$BACKUP_DIR/varlog_full.tar.gz" /var/log/ 2>/dev/null

echo "[+] Capturing dmesg output..."
dmesg > "$BACKUP_DIR/dmesg.log"

echo "[+] Capturing Docker daemon logs..."
journalctl -u docker.service > "$BACKUP_DIR/docker_daemon.log"

echo "[+] Capturing NVIDIA persistenced logs (if any)..."
journalctl -u nvidia-persistenced > "$BACKUP_DIR/nvidia_persistenced.log" 2>/dev/null
cp /var/log/nvidia-installer.log "$BACKUP_DIR/nvidia-installer.log" 2>/dev/null || echo "NVIDIA installer log not found."

echo "[+] Capturing NVIDIA-related dmesg logs..."
dmesg | grep -i nvidia > "$BACKUP_DIR/nvidia_dmesg.log"
sudo grep -i nvidia /var/log/syslog > "$BACKUP_DIR/nvidia_syslog.log" 2>/dev/null
sudo grep -i nvidia /var/log/messages > "$BACKUP_DIR/nvidia_messages.log" 2>/dev/null

echo "[+] Capturing V4L2 and video-related logs..."
dmesg | grep -i v4l2 > "$BACKUP_DIR/v4l2_dmesg.log"
dmesg | grep -i video > "$BACKUP_DIR/video_dmesg.log"
dmesg | grep -i camera > "$BACKUP_DIR/camera_dmesg.log"
grep -i v4l2 /var/log/syslog > "$BACKUP_DIR/v4l2_syslog.log" 2>/dev/null
grep -i video /var/log/syslog > "$BACKUP_DIR/video_syslog.log" 2>/dev/null

echo "[+] Checking CUDA-related logs in running containers..."
for cid in $(docker ps -q); do
    cname=$(docker inspect --format '{{.Name}}' "$cid" | sed 's|/||')
    docker logs "$cid" | grep -i cuda > "$BACKUP_DIR/${cname}_cuda.log" 2>/dev/null
done

echo "[✓] All logs saved under: $BACKUP_DIR"

