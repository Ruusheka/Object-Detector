# 🧠 Object Detector

An AI-powered object detection app that identifies and labels objects in any uploaded image using state-of-the-art vision models.

[![Hugging Face Space](https://img.shields.io/badge/Live%20Demo-%F0%9F%94%97-blue?style=for-the-badge)](https://huggingface.co/spaces/Ruusheka/Object-detector)

## 🚀 About

This Gradio-powered app uses a pre-trained object detection model to:
- Detect multiple objects in an image
- Label them with bounding boxes and class names
- Display confidence scores

All in real-time, with just a single image upload!

---

## 🧰 Tech Stack

- 🤗 **Hugging Face Transformers**
- 🖼️ **Computer Vision Model**: `facebook/detr-resnet-50` (DEtection TRansformer)
- 🖥️ **Frontend & UI**: Gradio
- 🌐 Hosted on: Hugging Face Spaces

---

## 📸 Demo

Upload any image, and the app will return the same image with detected objects labeled:

![Demo](https://huggingface.co/spaces/Ruusheka/Object-detector/+/raw/main/demo.png)

> _If no objects are detected, try using a clearer or more diverse image._

---

## 🧪 How It Works

1. **Upload** an image (drag & drop or select from files).
2. The app processes the image using the `facebook/detr-resnet-50` model.
3. Detected objects are returned with bounding boxes, labels, and confidence percentages.

---

## ⚙️ Setup Locally (Optional)

```bash
git clone https://huggingface.co/spaces/Ruusheka/Object-detector
cd Object-detector
pip install -r requirements.txt
python app.py
