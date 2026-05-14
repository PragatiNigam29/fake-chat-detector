# 🔍 Fake Chat Screenshot Detector

An AI-powered web application that analyzes screenshots and detects possible manipulation using Error Level Analysis (ELA).

Built using Python, Django, and OpenCV.

---

## 🚀 Features

- Upload screenshots for analysis
- Generate ELA (Error Level Analysis) output
- Detect compression inconsistencies
- Calculate fake probability score
- Smart verdict system:
  - Likely Real ✅
  - Suspicious ⚠️
  - Highly Manipulated ❌
- Modern responsive UI

---

## 🧠 How It Works

The system performs Error Level Analysis (ELA) on uploaded images.

ELA highlights differences in image compression levels. Manipulated regions often show different compression patterns compared to untouched areas.

The application:
1. Uploads image
2. Generates ELA image
3. Analyzes pixel intensity
4. Calculates manipulation probability
5. Displays verdict

---

## 🛠️ Tech Stack

- Python
- Django
- OpenCV
- NumPy
- Pillow
- HTML
- Tailwind CSS

---



## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/fake-chat-detector.git
```

### 2. Move into project folder

```bash
cd fake-chat-detector
```

### 3. Create virtual environment

```bash
python -m venv venv
```

### 4. Activate virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run server

```bash
python manage.py runserver
```

---

## 🌍 Deployment

Deployed using Render.

---

## 📌 Future Improvements

- CNN-based deep learning detection
- Highlight suspicious regions automatically
- Drag-and-drop uploads
- OCR-based chat analysis
- Real-time detection API

---

