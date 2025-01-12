ARG PYTHON_VERSION=3.10.0

FROM ubuntu:latest AS base

RUN apt-get update && \
    apt-get -y install python3:${PYTHON_VERSION} && \
    apt-get -y install ffmpeg

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt /app
RUN apt-get -y install yt-dlp


# Copy the application code
COPY downloader_youtube.py /app

# Run downloader_youtube.py when the container launches
CMD ["python3", "downloader_youtube.py"]

# Path: app_python/youtube/requirements.txt

# docker build -t youtube-downloader .
# docker run -it youtube-downloader

