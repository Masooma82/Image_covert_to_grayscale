import cv2
image_convert = cv2.imread("C:\\Users\\HP\\Desktop\\Python\\Image_color_to_grey\\bts_v.jpg",cv2.IMREAD_UNCHANGED)
im_gray = cv2.cvtColor(image_convert, cv2.COLOR_BGR2GRAY) # im_gray: This is a grayscale image on which the thresholding operation will be performed. 
# Grayscale images have a single channel representing pixel intensities from black (0) to white (255).
# 170: This is the threshold value. Any pixel value greater than or equal to 170 will be set to 255 (white), while any pixel value below 170 will be set to 0 (black).
# 255: This is the maximum value that a pixel can take after thresholding. Any pixel value greater than or equal to the threshold value (170 in this case) will be set to this maximum value, which is 255 (white).
# cv2.Thresh_Binary: This is the thresholding method being used. In this case, it's using the Binary thresholding method, where pixels are either set to the maximum value (255) or minimum value (0) based on their intensity compared to the threshold.
# thresh variable contains threshold value which is 170 in this case and im_black contains threshold image
thresh, im_black = cv2.threshold(im_gray, 170, 255, cv2.THRESH_BINARY)
cv2.imshow('bts_v.jpg',im_black) #here bts_v.jpg is just the label of the frame that displays when we run the code
# When you run this line of code, it will create and save the grayscale image as a PNG file named "im_grayscale.png" in the current working directory (where the Python script or notebook is located)
cv2.imwrite('im_grayscale.png',im_gray)
#Save im_black image as "image_black.png"
cv2.imwrite('image_black.png',im_black)
# This is a function provided by OpenCV to wait for a key event in this case 0
cv2.waitKey(0)
# to close all OpenCV windows that were opened for displaying images
cv2.destroyAllWindows()


