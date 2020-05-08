# Raspberrypi-Face-Recognition
This is a faster and easy recognition for human face recognition based on raspberrypi 4B.
We improve the recognition speed by saving feature extraction process. <br>
It's based on dlib and python3.7. 
'We test it on raspi4B. It's robust for recognizing human face within 3 meters.'
## Raspi Installation <br>
**Basic requirement:**
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    python3-pip \
    zip
sudo apt-get clean
```
**Picamera Installion**<br>
if U use only picamera and proceed the code below
```
sudo apt-get install python3-picamera
sudo pip3 install --upgrade picamera[array]
```
<br>If U use Usb camera, then there is no requirement for Picamera Installion. `python3-opencv` can do the same job as picamera.
