import qrcode 
import os 
link_start = 'https://madsljensen.github.io/qr_redirects/'

def generate_codes():
    # List subdirectories
    subdirectories = [d for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.')]
    subdirs_no_qr = [d for d in subdirectories if not os.path.exists(os.path.join(d,f"{d}_qr.png"))]
    for subdir in subdirs_no_qr:
        img = qrcode.make(link_start + subdir)
        img.save(os.path.join(subdir,f"{subdir}_qr.png"))

generate_codes()

