import cv2
import numpy as np

def pencil_sketch(image_path, output_path):
    # Read the input image
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_gray_image = cv2.bitwise_not(gray_image)

    # Apply Gaussian blur to the inverted image
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

    # Invert the blurred image
    inverted_blurred_image = cv2.bitwise_not(blurred_image)

    # Create the pencil sketch by dividing the gray image by the inverted blurred image
    pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

    # Save the pencil sketch image
    cv2.imwrite(output_path, pencil_sketch_image)

    # Display the pencil sketch image
    cv2.imshow('Pencil Sketch', pencil_sketch_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Input and output paths
input_image_path = r"C:\Users\ar_ar\Desktop\code\PENCIL SKETCH\image.jpg"
output_image_path = r"C:\Users\ar_ar\Desktop\code\PENCIL SKETCH\pencil_sketch.jpg"

# Run the pencil sketch function
pencil_sketch(input_image_path, output_image_path)
