import cv2
import numpy as np

img = [[0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,1,0,0,1,0,0],
       [0,0,1,1,1,1,1,0,0,0],
       [0,0,0,1,1,1,1,0,0,0],
       [0,0,1,1,1,1,1,1,1,0],
       [0,0,1,1,1,1,1,1,0,0],
       [0,0,1,1,1,1,0,0,0,0],
       [0,0,1,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0]]
# Load an image
img = cv2.imread(img)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection to find the edges
edges = cv2.Canny(gray, 100, 200)

# Find the contours of the edges
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Calculate the perimeter of each contour using Euclidean distance
perimeters = [cv2.arcLength(contour, True) for contour in contours]

# Print the perimeters of the contours
for i, perimeter in enumerate(perimeters):
    print(f"Contour {i + 1} perimeter: {perimeter}")