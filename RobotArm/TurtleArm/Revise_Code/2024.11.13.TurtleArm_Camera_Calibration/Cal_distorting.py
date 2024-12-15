import cv2
import numpy as np
import glob

# Camera matrix and distortion coefficients from your calibration
mtx = np.array([[310.93505147, 0., 305.1882977 ],
                [0., 311.02060429, 238.72764315],
                [0., 0., 1.]])  # Camera matrix

dist = np.array([-3.42750945e-01,  1.49543845e-01,  2.39640046e-04,  4.72473300e-04, -3.54611271e-02])  # Distortion coefficients

# Path to your images
image_path = '/home/pi/Revise_Code/2024.11.13.TurtleArm_Camera_Calibration/captured_image_*.jpg'  # Adjust the path if needed

# Get a list of all image files matching the pattern
images = glob.glob(image_path)
print(f"Found {len(images)} images.")

# Loop through each image, apply undistortion, and display or save the results
for fname in images:
    img = cv2.imread(fname)  # Load the image
    
    # Get image size (height, width)
    h, w = img.shape[:2]

    # Get the optimal camera matrix to reduce the distortion
    new_camera_mtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

    # Undistort the image
    undistorted_img = cv2.undistort(img, mtx, dist, None, new_camera_mtx)

    # Optionally crop the image to remove black borders (if any)
    x, y, w, h = roi
    undistorted_img_cropped = undistorted_img[y:y+h, x:x+w]

    # Display both the original and undistorted images side by side (optional)
    cv2.imshow(f'Original - {fname}', img)
    cv2.imshow(f'Undistorted - {fname}', undistorted_img_cropped)

    # Save the undistorted image (optional)
    output_filename = f"undistorted_{fname.split('/')[-1]}"  # Save with a prefix "undistorted_"
    cv2.imwrite(output_filename, undistorted_img_cropped)

    # Wait for a key press to move to the next image
    cv2.waitKey(500)  # Adjust the delay to your preference

cv2.destroyAllWindows()  # Close all windows
