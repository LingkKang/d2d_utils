"""
Extract frames from a video file

Required:
    - `opencv-python`

Usage:
    `python video_extract_frames.py video.mp4`
"""

import os
import sys

import cv2

def extract_frames_opencv(input_video, output_pattern, fps=1):
    cap = cv2.VideoCapture(input_video)
    frame_rate = cap.get(cv2.CAP_PROP_FPS)  # Original frame rate of the video
    frame_interval = int(frame_rate / fps)  # Interval between frames to capture

    success, frame_id = True, 0
    while success:
        success, frame = cap.read()
        if success and frame_id % frame_interval == 0:
            filename = output_pattern % (frame_id // frame_interval)
            cv2.imwrite(filename, frame)
        frame_id += 1

    cap.release()

# Usage
extract_frames_opencv('input_video.mp4', 'frame_%04d.png', fps=10)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python video_extract_frames.py video.mp4")
        sys.exit(1)

    input_video = sys.argv[1]
    output_pattern = "frame_%04d.png"
    extract_frames_opencv(input_video, output_pattern, fps=10)
