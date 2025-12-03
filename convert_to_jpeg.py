import os
from PIL import Image
import pillow_heif

# Register HEIF opener with Pillow
pillow_heif.register_heif_opener()

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Find all HEIC files
heic_files = [f for f in os.listdir(script_dir) if f.lower().endswith('.heic')]

print(f"Found {len(heic_files)} HEIC files to convert")

for heic_file in heic_files:
    heic_path = os.path.join(script_dir, heic_file)
    jpeg_file = os.path.splitext(heic_file)[0] + '.jpg'
    jpeg_path = os.path.join(script_dir, jpeg_file)
    
    try:
        # Open and convert
        img = Image.open(heic_path)
        # Convert to RGB if necessary (HEIC can have alpha channel)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        # Save as JPEG with high quality
        img.save(jpeg_path, 'JPEG', quality=95)
        print(f"Converted: {heic_file} -> {jpeg_file}")
    except Exception as e:
        print(f"Error converting {heic_file}: {e}")

print("\nConversion complete!")

