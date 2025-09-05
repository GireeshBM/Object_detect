#!/bin/bash

CAM_IP="ip-addreess"
IPT="sudo iptables"

add_rules() {
  echo "🚫 Blocking traffic to/from $CAM_IP"
  $IPT -I DOCKER-USER 1 -s $CAM_IP -p udp -j DROP
  $IPT -I DOCKER-USER 1 -d $CAM_IP -p udp -j DROP
  $IPT -I DOCKER-USER 1 -s $CAM_IP -p tcp -j DROP
  $IPT -I DOCKER-USER 1 -d $CAM_IP -p tcp -j DROP
}

remove_rules() {
  echo "✅ Unblocking traffic to/from $CAM_IP"
  $IPT -D DOCKER-USER -s $CAM_IP -p udp -j DROP 2>/dev/null
  $IPT -D DOCKER-USER -d $CAM_IP -p udp -j DROP 2>/dev/null
  $IPT -D DOCKER-USER -s $CAM_IP -p tcp -j DROP 2>/dev/null
  $IPT -D DOCKER-USER -d $CAM_IP -p tcp -j DROP 2>/dev/null
}

trap 'echo "🛑 Exiting..."; remove_rules; exit 0' INT TERM

# Run forever: Block for 5s, unblock for 5s
while true; do
  add_rules
  sleep 0.1

  remove_rules
 sleep 0.1
done
