from PIL import Image
import os

def resize_image(image_path, output_path, base_width=500):
    try:
        img = Image.open(image_path)
        w_percent = (base_width / float(img.size[0]))
        h_size = int((float(img.size[1]) * float(w_percent)))
        img = img.resize((base_width, h_size), Image.Resampling.LANCZOS)
        img.save(output_path)
        print(f"Successfully resized {image_path} to {output_path}")
    except Exception as e:
        print(f"Error resizing image: {e}")

input_path = 'rebirth/assets/images/logo.png'
# Overwrite or save as new? User said "resize and add", I will overwrite to keep it clean for the project.
resize_image(input_path, input_path)
