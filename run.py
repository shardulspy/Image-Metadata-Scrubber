import piexif
from PIL import Image

def remove_exif(input_path, output_path):
    img = Image.open(input_path)
    img.save(output_path, exif=b'')
    print(f"✅ {output_path} saved without EXIF data.")

if __name__ == "__main__":
    remove_exif("input.jpg", "output.jpg")

