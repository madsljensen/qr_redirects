import os
import urllib.parse
import requests
import cv2
from pyzbar.pyzbar import decode


def test_qr_generation():
    subdirectories = [d for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.')]
    for subdir in subdirectories:
        # Check if the QR code image exists
        qr_image_path = os.path.join(subdir, f"{subdir}_qr.png")
        assert os.path.exists(qr_image_path)

        qr_data = get_qr_code_data(qr_image_path)
        is_url_well_formed(qr_data)
        is_url_reachable(qr_data)
        get_final_url(qr_data)

def get_qr_code_data(image_path):
    img = cv2.imread(image_path)
    decoded_objects = decode(img)
    for obj in decoded_objects:
        return obj.data.decode('utf-8')
    return None

def is_url_well_formed(url):
    try:
        result = urllib.parse.urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False

def is_url_reachable(url, timeout=5):
    try:
        response = requests.head(url, allow_redirects=True, timeout=timeout)
        return response.status_code < 400
    except Exception:
        return False

def get_final_url(url, timeout=5):
    try:
        response = requests.head(url, allow_redirects=True, timeout=timeout)
        return response.url  # This is the final URL after redirects
    except Exception:
        return None

if __name__ == "__main__":
    test_qr_generation()