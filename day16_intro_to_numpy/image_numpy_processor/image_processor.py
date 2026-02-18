import numpy as np
from image_data import image

print("Original Image:\n", image)

# Brightness Enhancement
bright = np.clip(image + 40, 0, 255)

# Thresholding
thresholded = np.where(bright > 180, 255, 0)

print("\nBrightened Image:\n", bright)
print("\nThresholded Image:\n", thresholded)

# Image Statistics
print("\nMax Intensity:", np.max(image))
print("Min Intensity:", np.min(image))
print("Average Intensity:", np.mean(image))
