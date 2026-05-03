#  Smart Lecture Archiving System

An automated pipeline designed to transform long, noisy lecture videos into organized, high-quality study materials.  
This project applies **Digital Signal Processing (DSP)** and **Image Processing** techniques to convert raw lecture recordings into useful study resources.

---

##  Project Overview

Lecture videos often suffer from:
- Poor video quality
- Background noise
- Long duration and repeated frames
- Difficult note extraction

This system processes lecture videos and automatically generates:

✅ Clean whiteboard images  
✅ Noise-free lecture audio  
✅ Searchable lecture transcript  

---

## 🎯 Project Objectives

The system converts a lecture video into three study-friendly outputs:

1. **Enhanced Board Images**
   - Clear high-contrast board screenshots
   - Saved only when content changes

2. **Clean Audio**
   - Background noise removal
   - Better speech clarity

3. **Speech Transcript**
   - Text version of lecture audio
   - Searchable keywords with timestamps

---

## 1️⃣ Video Management & Frame Extraction
**Responsible for:** Video preprocessing

### Tasks
- Read lecture video using OpenCV
- Extract:
  - Frame width
  - Frame height
  - FPS
- Add timestamp to each frame

### Smart Feature
Uses **NumPy frame comparison** to detect board changes and save frames only when new writing appears.

### Output
- Raw board frames
- Video metadata report

---

## 2️⃣ Audio Denoising Expert
**Responsible for:** Audio enhancement

### Tasks
- Extract audio from video
- Apply **STFT (Short-Time Fourier Transform)**
- Estimate background noise
- Subtract noise from signal
- Reconstruct clean signal using **ISTFT**

### Extra Feature
Plot waveform before and after denoising.

### Output
- `cleaned_audio.wav`

---

## 3️⃣ Speech-to-Text Documentation
**Responsible for:** Lecture transcription

### Tasks
- Convert cleaned audio to text
- Use Speech Recognition library

### Smart Feature
Keyword detection system:
- Important
- Exam
- Quiz
- Assignment

Each detected keyword is linked to its timestamp.

### Output
- `lecture_transcript.txt`

---

## 4️⃣ Image Enhancement Specialist
**Responsible for:** Board cleaning

### Tasks
- Convert images to grayscale
- Apply thresholding
- Remove noise
- Resize images

### Processing Techniques
- Grayscale conversion
- Thresholding
- Binarization
- Resize

### Output
- Enhanced readable board images

---

## 5️⃣ Archiving & Final Report
**Responsible for:** Final formatting and archive generation

### Tasks
- Adjust contrast
- Invert colors (optional dark board support)
- Extract image metadata using Pillow

### Final Report Includes
- Image size
- Image mode
- Number of extracted frames
- Generated files summary

### Output
- Final archive report

---

## 🛠️ Technologies Used

- **Python 3**
- **OpenCV**
- **NumPy**
- **Pillow (PIL)**
- **Matplotlib**
- **SpeechRecognition**
- **SciPy**

---

## 📊 Expected Outputs

After running the project, you should get:

- Clean board images
- Noise-free audio
- Lecture transcript
- Final report

---

##  Future Improvements

- OCR for extracting handwritten text from board images
- PDF notes generation
- Lecture summarization using NLP
- GUI desktop application

---

##  Academic Concepts Applied

This project applies concepts from:

- Digital Signal Processing
- Image Processing
- Frequency Analysis
- Audio Filtering
- Thresholding
- Frame Differencing

---

##  Final Goal

Transform long, noisy lecture recordings into a **smart digital study archive** for students.
