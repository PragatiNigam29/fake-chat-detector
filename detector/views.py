from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from PIL import Image, ImageChops, ImageEnhance
import os

def ela_image(path):
    original = Image.open(path).convert('RGB')

    temp_path = 'temp.jpg'
    original.save(temp_path, 'JPEG', quality=90)

    compressed = Image.open(temp_path)

    ela = ImageChops.difference(original, compressed)

    extrema = ela.getextrema()
    max_diff = max([ex[1] for ex in extrema])

    scale = 255.0 / max_diff if max_diff != 0 else 1

    ela = ImageEnhance.Brightness(ela).enhance(scale)

    ela_path = path.replace('.', '_ela.')
    ela.save(ela_path)

    return ela_path
import numpy as np
import cv2

def calculate_fake_score(ela_path):
    img = cv2.imread(ela_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Normalize values (0–255)
    mean_intensity = np.mean(gray)

    # Convert to percentage
    fake_score = (mean_intensity / 255) * 100

    return round(fake_score, 2)
def upload_image(request):
    image_url = None
    ela_url = None
    fake_score=None
    reason=None

    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_url = fs.url(filename)

        # ELA processing
        file_path = fs.path(filename)
        ela_path = ela_image(file_path)
        ela_url = fs.url(os.path.basename(ela_path))

        fake_score = calculate_fake_score(ela_path)
        if fake_score < 30:
         verdict = "Likely Real ✅"
         reason = "Low compression differences detected"
        elif fake_score < 60:
         verdict = "Suspicious ⚠️"
         reason = "Moderate inconsistencies found"
        else:
         verdict = "Highly Manipulated ❌"
         reason = "High compression anomalies detected"

    return render(request, 'detector/upload.html', {
        'image_url': image_url,
        'ela_url': ela_url,
        'fake_score': fake_score,
        'reason':reason
    })