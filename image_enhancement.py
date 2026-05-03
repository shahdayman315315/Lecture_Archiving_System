import cv2
import os
import numpy as np

# 1. Path Settings
input_folder = 'Outputs/Captured_Photos' 
output_folder = 'Outputs/Enhanced_Photos'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg'))]
print(f"--- Starting Color Enhancement for {len(image_files)} images ---")

# Loop through each image file in the input folder and apply enhancement steps
for filename in image_files:
    img_path = os.path.join(input_folder, filename)
    img = cv2.imread(img_path) 

    if img is None:
        continue

    # --- STEP 1: Denoising (Median Blur) ---
    # Remove salt-and-pepper noise , especially important for marker text
    # 3 is the kernel size, which determines the area of pixels considered for median calculation
    denoised = cv2.medianBlur(img, 3)

    # --- STEP 2: Contrast & Brightness (Normalization ) ---
   # Normalize pixel values to enhance contrast, making marker text more distinguishable
    enhanced_color = cv2.normalize(denoised, None, 0, 255, cv2.NORM_MINMAX)

    # --- STEP 3: Image Sharpening (Filter) ---Sharpen the image  
    # This 3x3 matrix is a High-Pass Filter The sum of elements equals 1 to maintain the overall brightness.
    kernel = np.array([[-1,-1,-1], 
                       [-1, 9,-1], 
                       [-1,-1,-1]])
    # filter2D performs 'Convolution' between the image and the kernel
    sharpened = cv2.filter2D(enhanced_color, -1, kernel)

    # --- STEP 4: Resizing ---
     # Standardizing image size for better consistency in further processing
    height, width = sharpened.shape[:2]
    target_width = 1280
    aspect_ratio = target_width / float(width)
    final_img = cv2.resize(sharpened, (target_width, int(height * aspect_ratio)), interpolation=cv2.INTER_AREA)

    # --- STEP 5: Saving Output ---
    output_path = os.path.join(output_folder, f"enhanced_{filename}")
    cv2.imwrite(output_path, final_img)
    
    print(f"Processed Color Image: {filename}")

print("--- Color Enhancement Completed ---")