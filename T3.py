import os
import cv2
import numpy as np

def overlay_images(input_directory, overlay_image_path, output_directory):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Read the overlay image
    overlay_image = cv2.imread(overlay_image_path, cv2.IMREAD_UNCHANGED)

    # Loop through the images in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".png"):
            # Read the input image
            input_image_path = os.path.join(input_directory, filename)
            input_image = cv2.imread(input_image_path, cv2.IMREAD_UNCHANGED)

            # Resize the overlay image to match the input image dimensions
            overlay_image_resized = cv2.resize(overlay_image, (input_image.shape[1], input_image.shape[0]))

            # Extract the alpha channel from the overlay image
            overlay_alpha = overlay_image_resized[:, :, 3]

            # Normalize the overlay alpha channel to the range [0, 1]
            overlay_alpha_norm = overlay_alpha / 255.0

            # Expand dimensions of alpha to match the shape of the input image
            overlay_alpha_norm = overlay_alpha_norm[:, :, np.newaxis]

            # Perform the overlay operation while preserving transparency
            output_image = np.uint8(input_image * (1 - overlay_alpha_norm) + overlay_image_resized[:, :, :3] * overlay_alpha_norm)

            # Save the overlaid image to the output directory
            output_image_path = os.path.join(output_directory, filename)
            cv2.imwrite(output_image_path, output_image)

    print("Overlay complete.")


# Define the paths
input_directory = "../imagesoppepe/"
overlay_image_path = "../opepen.png"
output_directory = "../imagesoppepedone/"

# Call the overlay_images function
overlay_images(input_directory, overlay_image_path, output_directory)
