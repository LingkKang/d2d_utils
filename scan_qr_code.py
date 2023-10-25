import sys

from cv2 import imread
from pyzbar.pyzbar import decode


def read_qr_code(image_path):
    image = imread(image_path)
    decoded_objects = decode(image)
    if decoded_objects:
        for objects in decoded_objects:
            data = objects.data.decode("utf-8")
            print(data)
            return data
    else:
        print("QR Code not detected")
        return None


if __name__ == "__main__":
    if read_qr_code(sys.argv[1]):
        sys.exit(0)
    else:
        sys.exit(1)
