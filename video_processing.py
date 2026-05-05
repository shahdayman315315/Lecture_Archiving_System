import cv2
import os
import numpy as np  # ضروري جداً لمقارنة المصفوفات

# 1. تحديد المسارات
video_path = 'Input/Alpha beta pruning in artificial intelligence with example. - Crack Concepts (360p, h264).mp4'
output_folder = 'Outputs/Captured_Photos'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 2. فتح الفيديو
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)

count = 0        #عدد الفريمز ف الفيديو
saved_count = 0    # عدد الصور الى هناخدها من الفيديو
prev_frame = None    # هنا هنخزن الفريم القديم عشان نقارن بيه
threshold_diff = 10.0  # نسبة التغيير اللي بنعتبرها "حاجة جديدة اتكتبت"

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # استخراج فريم كل دقيقه
    if count % (int(fps)*60) == 0:

        # تحويل الفريم لـ Grayscale وتصغيره (عشان المقارنة تكون أسرع وأدق)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)  # تقليل النويز قبل المقارنة

        if prev_frame is not None:
            # حساب الفرق المطلق بين الفريم الحالي والقديم
            frame_diff = cv2.absdiff(prev_frame, gray_frame)
            # حساب متوسط التغيير في بكسلات الصورة
            change_score = np.mean(frame_diff)

            # لو التغيير أكبر من الـ Threshold، يبقى في حاجة جديدة حصلت
            if change_score > threshold_diff:
                frame_name = f"{output_folder}/Cap_frame_{saved_count}.jpg"

                # إضافة التوقيت عشان نعرف التغيير حصل إمتى
                timestamp = f"Change detected at minute {int((int(count / fps))/60)}:00 "
                cv2.putText(frame, timestamp, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

                cv2.imwrite(frame_name, frame)
                saved_count += 1
                print(f"Update detected! Saved: {frame_name} (Score: {change_score:.2f})")

        # تحديث الفريم القديم ليصبح هو الفريم الحالي في اللفة الجاية
        prev_frame = gray_frame

    count += 1

cap.release()
print(f"Finished! Total smart frames saved: {saved_count}")