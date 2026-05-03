import speech_recognition as sr
import os

# 1. تحديد المسارات
cleaned_audio_path = 'Outputs/cleaned_audio.wav'
output_folder = 'Outputs/Audio_speech'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

transcript_path = f'{output_folder}/transcript.txt'

# 2. تحميل الصوت
recognizer = sr.Recognizer()

with sr.AudioFile(cleaned_audio_path) as source:
    print("Loading audio...")
    audio_data = recognizer.record(source)

# 3. تحويل الصوت لنص
print("Converting speech to text...")
try:
    text = recognizer.recognize_google(audio_data, language='ar-EG')
except sr.UnknownValueError:
    text = "[Could not understand audio]"
except sr.RequestError as e:
    text = f"[API Error: {e}]"

# 4. البحث عن الكلمات المهمة
keywords = ['important', 'exam', 'مهم', 'امتحان']
found_keywords = []

for word in keywords:
    if word.lower() in text.lower():
        found_keywords.append(word)

# 5. حفظ النص في ملف
with open(transcript_path, 'w', encoding='utf-8') as f:
    f.write("=" * 50 + "\n")
    f.write(" Lecture Transcript\n")
    f.write("=" * 50 + "\n\n")
    f.write(text)
    f.write("\n\n" + "=" * 50 + "\n")
    f.write(" Important Keywords Found:\n")
    if found_keywords:
        for kw in found_keywords:
            f.write(f"{kw}'\n")
    else:
        f.write("  No keywords found.\n")

print(f"Done! Transcript saved: {transcript_path}")
if found_keywords:
    print(f" Keywords found: {found_keywords}")
