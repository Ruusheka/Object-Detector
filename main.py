import gradio as gr
from PIL import Image,ImageDraw, ImageFont


from transformers import pipeline
model_path="Models/models--facebook--detr-resnet-50/snapshots/1d5f47bd3bdd2c4bbfa585418ffe6da5028b4c0b"

# pipe = pipeline("object-detection", model="facebook/detr-resnet-50")
object_detector = pipeline("object-detection", model=model_path)

def draw_boxes(image, detections):
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    for det in detections:
        box = det['box']
        label = f"{det['label']}:{det['score'] * 100:.1f}%"

        # Draw rectangle
        draw.rectangle([box['xmin'], box['ymin'], box['xmax'], box['ymax']],
                       outline='red', width=3)

        # Prepare label background
        text_bbox = draw.textbbox((box['xmin'], box['ymin']), label, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        draw.rectangle([box['xmin'], box['ymin'] - text_height - 4, box['xmin'] + text_width + 4, box['ymin']],
                       fill='red')

        # Draw label text
        draw.text((box['xmin'] + 2, box['ymin'] - text_height - 2),
                   label, fill='white', font=font)

    return image

def detect_object(image):
    """Process the uploaded image instead of a hardcoded file."""
    detections = object_detector(image)
    processed = draw_boxes(image.copy(), detections)
    return processed

demo = gr.Interface(
    fn=detect_object,
    inputs=[gr.Image(type='pil', label='Select Image')],
    outputs=[gr.Image(type='pil', label='Processed Image')],
    title='OBJECT-DETECTOR',
    description="OBJECT DETECTOR IS AN APPLICATION WHERE YOU CAN UPLOAD AN IMAGE AND IT DETECTS THE OBJECTS FROM THAT IMAGE."
)

demo.launch()