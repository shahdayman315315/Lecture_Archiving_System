import numpy as np
import scipy.io.wavfile as wav
import scipy.signal as signal
import os
from moviepy import VideoFileClip

# 1. تحديد المسارات
video_path = 'Input/Alpha beta pruning in artificial intelligence with example. - Crack Concepts (360p, h264).mp4'
output_folder = 'Outputs'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

raw_audio_path = f'{output_folder}/raw_audio.wav'
cleaned_audio_path = f'{output_folder}/cleaned_audio.wav'

# 2. فصل الصوت من الفيديو
video = VideoFileClip(video_path)
video.audio.write_audiofile(raw_audio_path, fps=16000)
print(" Audio extracted!")

# 3. قراءة الصوت
sample_rate, audio_data = wav.read(raw_audio_path)

# لو Stereo حوله لـ Mono
if len(audio_data.shape) > 1:
    audio_data = audio_data[:, 0]

audio_float = audio_data.astype(np.float32)

# 4. تقسيم الصوت لأجزاء صغيرة (30 ثانية كل جزء)
chunk_size = sample_rate * 30
chunks = [audio_float[i:i+chunk_size] for i in range(0, len(audio_float), chunk_size)]

print(f" Processing {len(chunks)} chunks...")

cleaned_chunks = []

for idx, chunk in enumerate(chunks):
    # STFT
    _, _, spectrogram = signal.stft(chunk, fs=sample_rate, nperseg=512)

    # تنظيف الضوضاء
    noise_profile = np.mean(np.abs(spectrogram[:, :10]), axis=1, keepdims=True)
    cleaned_spec = np.maximum(np.abs(spectrogram) - noise_profile, 0)
    phase = np.angle(spectrogram)
    cleaned_complex = cleaned_spec * np.exp(1j * phase)

    # ISTFT
    _, cleaned_chunk = signal.istft(cleaned_complex, fs=sample_rate, nperseg=512)
    cleaned_chunks.append(cleaned_chunk)

    print(f" Chunk {idx+1}/{len(chunks)} done!")

# 5. دمج الأجزاء
cleaned_audio = np.concatenate(cleaned_chunks)

# 6. حفظ الملف النقي
cleaned_audio_int = np.int16(cleaned_audio / np.max(np.abs(cleaned_audio)) * 32767)
wav.write(cleaned_audio_path, sample_rate, cleaned_audio_int)
# حذف الملف المؤقت
os.remove(raw_audio_path)
print(" Temp file removed!")

print(f"Done! Cleaned audio saved: {cleaned_audio_path}")
