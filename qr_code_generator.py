import qrcode 
import os 
link_start = 'https://madsljensen.github.io/qr_redirects/'

def generate_codes():
    # List subdirectories
    subdirectories = [d for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.')]
    print("Subdirectories:", subdirectories)
    for subdir in subdirectories:
        img = qrcode.make(link_start + subdir)
        img.save(os.path.join(subdir,f"{subdir}_qr.png"))

if __name__ == "__main__":
    generate_codes()

