import speech_recognition as sr
import os

# 1. تحديد المسارات
cleaned_audio_path = 'Outputs/cleaned_audio.wav'
output_folder = 'Outputs/Audio_speech'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

transcript_path = f'{output_folder}/transcript.txt'

# 2. إعداد الـ Recognizer
recognizer = sr.Recognizer()
full_text = ""
found_keywords = []
keywords = ['important', 'exam', 'مهم', 'امتحان']

# 3. معالجة الصوت (أول دقيقة فقط)
print("Loading and processing the first 60 seconds of audio...")

try:
    with sr.AudioFile(cleaned_audio_path) as source:


        process_duration = min(450, int(source.DURATION))
        print(f"Processing duration: {process_duration} seconds")

        chunk_size = 5
        for i in range(0, process_duration, chunk_size):
            # تسجيل الجزء الحالي
            audio_chunk = recognizer.record(source, duration=chunk_size)

            try:
                print(f" Converting chunk {i} to {i + chunk_size} seconds...")
                chunk_text = recognizer.recognize_google(audio_chunk, language='en-US')
                full_text += chunk_text + " "
            except sr.UnknownValueError:
                print(f" [Skipped] Chunk at {i}s: Could not understand audio.")
                continue
            except sr.RequestError as e:
                print(f" [API Error] Chunk at {i}s: {e}")
                continue

    # التأكد من النتائج
    if not full_text.strip():
        text = "[Could not understand the first minute of audio]"
    else:
        text = full_text.strip()

    # 4. البحث عن الكلمات المهمة
    for word in keywords:
        if word.lower() in text.lower():
            found_keywords.append(word)

    # 5. حفظ النص في ملف
    with open(transcript_path, 'w', encoding='utf-8') as f:
        f.write("=" * 50 + "\n")
        f.write(" Lecture Transcript (First 60 Seconds Test)\n")
        f.write("=" * 50 + "\n\n")
        f.write(text)
        f.write("\n\n" + "=" * 50 + "\n")
        f.write(" Important Keywords Found:\n")
        if found_keywords:
            for kw in found_keywords:
                f.write(f"- {kw}\n")
        else:
            f.write("  No keywords found.\n")

    print(f"\nTest Done! Transcript saved: {transcript_path}")
    if found_keywords:
        print(f" Keywords found in first minute: {found_keywords}")

except FileNotFoundError:
    print(f"Error: The file {cleaned_audio_path} was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")