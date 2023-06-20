import cv2
import numpy as np
original_image = cv2.imread("C:/Users/Raja/OneDrive/Documents/computer vision/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg")
watermark_image = cv2.imread("C:/Users/Raja/OneDrive/Documents/computer vision/watermark-styles.jpg", cv2.IMREAD_UNCHANGED)
resized_watermark = cv2.resize(watermark_image, (100, 100))
x_pos = original_image.shape[1] - resized_watermark.shape[1] - 10
y_pos = original_image.shape[0] - resized_watermark.shape[0] - 10
overlay = np.zeros_like(original_image)
overlay[y_pos:y_pos+resized_watermark.shape[0], x_pos:x_pos+resized_watermark.shape[1]] = resized_watermark
alpha = 0.6
watermarked_image = cv2.addWeighted(original_image, 1, overlay, alpha, 0)
cv2.imshow("Watermarked Image", watermarked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
