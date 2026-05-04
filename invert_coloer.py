import numpy as np
import os
from PIL import Image

# 1. تحديد المسارات
input_folder = 'Outputs/Enhanced_Photos'
output_folder = 'Outputs/Final_Photos'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 2. جيب كل الصور
images = os.listdir(input_folder)

for img_name in images:
    if not img_name.endswith('.jpg'):
        continue

    img_path = f'{input_folder}/{img_name}'
    img = Image.open(img_path)
    img_array = np.array(img)

    # 3. Invert الألوان (سبورة سوداء → خلفية بيضاء)
    inverted = np.invert(img_array)

    # 4. ضبط التباين
    inverted = np.clip(inverted * 1.5, 0, 255).astype(np.uint8)

    # 5. حفظ الصورة النهائية
    final_img = Image.fromarray(inverted)
    save_path = f'{output_folder}/final_{img_name}'
    final_img.save(save_path)

    print(f"Archived: {img_name}")

print("Done!")