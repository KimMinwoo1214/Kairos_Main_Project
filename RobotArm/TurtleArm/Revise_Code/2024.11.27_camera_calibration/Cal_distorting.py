import cv2
import numpy as np
import glob

# Camera matrix and distortion coefficients from your calibration
mtx = np.array([[317.05966638, 0., 287.9901831 ],
                [0., 317.21510719, 232.81085565],
                [0., 0., 1.]])  # Camera matrix

dist = np.array([-0.3063854, 0.10224856,  0.00108754, -0.00063471, -0.01660539])  # Distortion coefficients

# Path to your images
image_path = '/home/pi/Revise_Code/2024.11.27_camera_calibration/captured_image_*.jpg'  # Adjust the path if needed

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
