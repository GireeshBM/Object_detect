#! /bin/bash
sudo apt-get update
sudo apt-get install cuda-toolkit
sudo apt-get install nvidia-gds
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda
sudo reboot
docker login nvcr.io
