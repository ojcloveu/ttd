from moviepy.editor import VideoFileClip, vfx
import numpy as np
import cv2
import os
import shutil

# Define the functions for enhancements
def apply_sepia(frame):
    sepia_filter = np.array([[1.2, 0.1, 0.1],
                             [0.1, 1.2, 0.1],
                             [0.1, 0.1, 1.2]])
    sepia_frame = np.dot(frame, sepia_filter.T)
    sepia_frame = np.clip(sepia_frame, 0, 255).astype(np.uint8)
    return sepia_frame

def enhance_brightness_contrast(frame):
    alpha = 0.9  # Brightness factor
    beta = 10    # Contrast factor
    enhanced_frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
    return enhanced_frame


# Input and output directories
input_folder = 'downloads'
output_folder = 'output'
achieve_folder = "achieve"

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List all image files in the input folder
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.mp4', '.jpg', '.jpeg'))]

for image_file in image_files:
    # Load the image    
    input_path = os.path.join(input_folder, image_file)
    output_path = os.path.join(output_folder, image_file)
    achieve_path = os.path.join(achieve_folder, image_file)
    print(input_path)

    # Load the video clip
    clip = VideoFileClip(input_path)

    # Flip the video horizontally
    flipped_clip = clip.fx(vfx.mirror_x)

    # Apply sepia filter
    sepia_flipped_clip = flipped_clip.fl_image(apply_sepia)

    # Enhance brightness and contrast
    enhanced_clip = sepia_flipped_clip.fl_image(enhance_brightness_contrast)

    # Speed up the video
    speed_factor = 1.2
    final_clip = enhanced_clip.fx(vfx.speedx, speed_factor)

    # Write the final video
    final_clip.write_videofile(output_path, codec='libx264')

    #move file
    shutil.move(input_path, achieve_path)

