FROM resin/rpi-raspbian:stretch
# FROM arm32v7/ubuntu:16.04

ARG ADDITIONAL_PACKAGE
ARG CV_VERSION="4.1.0"
ARG NUM_PROC=4

RUN apt-get update && apt-get upgrade && \
    apt-get install -y --no-install-recommends \                              
        software-properties-common build-essential checkinstall cmake pkg-config yasm \
        libjpeg-dev libtiff5-dev libjasper-dev libpng-dev \
        libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
        libxvidcore-dev libx264-dev \
        libgdk-pixbuf2.0-dev \
        libfontconfig1-dev \
        libcairo2-dev \
        libpango1.0-dev \
        libgdk-pixbuf2.0-dev \
        libpango1.0-dev \
        libxft-dev \
        libfreetype6-dev \
        libpng-dev \
        libgtk2.0-dev \                                                                                                                                   
        libgtk-3-dev \
        libatlas-base-dev gfortran \ 
        python3-dev \
        python3-setuptools \ 
        python3-pip \ 
        python3-wheel \ 
        python3-software-properties \ 
        curl \
        git gfortran

RUN curl -sSL https://github.com/openfaas/faas/releases/download/0.13.0/fwatchdog-armhf > /usr/bin/fwatchdog && \ 
    chmod +x /usr/bin/fwatchdog

WORKDIR /home/app/function/
# Create directory for installation
RUN mkdir installation && \ 
    mkdir installation/OpenCV-${CV_VERSION}

WORKDIR /home/app/function/installation/OpenCV-${CV_VERSION}

RUN pip3 install --upgrade pip && \
    pip install numpy 

RUN git clone https://github.com/opencv/opencv.git && \ 
    cd opencv && \ 
    git checkout ${CV_VERSION} && \ 
    cd ..
 
RUN git clone https://github.com/opencv/opencv_contrib.git && \ 
    cd opencv_contrib && \ 
    git checkout ${CV_VERSION} && \ 
    cd ..

RUN cd opencv && \ 
    mkdir build 

WORKDIR /home/app/function/installation/OpenCV-${CV_VERSION}/opencv/build/
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \
        -D CMAKE_INSTALL_PREFIX=/usr/local \
        -D INSTALL_C_EXAMPLES=OFF \
        -D INSTALL_PYTHON_EXAMPLES=ON \
        -D WITH_TBB=ON \
        -D WITH_V4L=ON \
        -D OPENCV_PYTHON3_INSTALL_PATH=/usr/lib/python3.5/site-packages \
        -D WITH_QT=OFF \
        -D BUILD_opencv_ts=OFF \
        -D BUILD_PERF_TESTS=OFF \
        -D INSTALL_C_EXAMPLES=OFF \
        -D WITH_OPENGL=OFF \
        -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
        -D BUILD_EXAMPLES=OFF ..

RUN make -j${NUM_PROC} && \ 
    make install
RUN ldconfig && \
    rm -rf ../../opencv-3.4.2 ../../opencv_contrib-3.4.2

RUN useradd -ms /bin/bash app
RUN chown app /home/app

WORKDIR /home/app/
USER app
ENV PATH=$PATH:/home/app/.local/bin
COPY index.py           .
COPY requirements.txt   .
RUN pip install --user -r requirements.txt

RUN mkdir -p function
RUN touch function/__init__.py

WORKDIR /home/app/function/
COPY function/requirements.txt	.
RUN pip install --user -r requirements.txt

WORKDIR /home/app/
COPY function           function

ENV fprocess="python3 index.py"
EXPOSE 8080

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
