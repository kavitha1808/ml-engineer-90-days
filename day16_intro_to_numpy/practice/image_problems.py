import numpy as np

# Sample Grayscale Image (3x3)
image = np.array([
    [50, 100, 150],
    [80, 130, 180],
    [120, 170, 220]
])

print("Original Image:\n", image)

# Problem 8: Brightness Adjustment
bright_image = np.clip(image + 40, 0, 255)
print("\nBrightened Image:\n", bright_image)

# Problem 9: Thresholding
thresholded_image = np.where(image > 150, 255, 0)
print("\nThresholded Image:\n", thresholded_image)

# Problem 10: Image Statistics
print("\nBrightest Pixel:", np.max(image))
print("Darkest Pixel:", np.min(image))
print("Average Intensity:", np.mean(image))
