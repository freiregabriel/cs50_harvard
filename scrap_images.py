from bs4 import BeautifulSoup
import requests
from PIL import Image
import json
import os
def extract_images(url):
    print('making request...')
    response = requests.get(url)
    print('done...')
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    print('Beautiful soup finished parsing!')
    img_srcs = [im.get('src') for im in soup.find_all('img')]
    with open('img_srcs.json', 'w') as f:
        print('saving to img_srcs.json...')
        f.write(json.dumps(img_srcs, ensure_ascii=False))
        print('done saving!')

def save_to_folder():
    folder_name = 'image_from_facebook'
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    with open('img_srcs.json', 'r') as f:
        content = json.load(f)
        count = 0
        for im in content:
            if im != None:
                try:                
                    print(" ------------------ ")
                    print(f"Saving {im}...")
                    raw_picture = requests.get(im, stream=True).raw
                    pil_image = Image.open(raw_picture).convert('RGB')
                    pil_image.save(f"{folder_name}/img_{count}.jpeg")
                    count += 1
                    print(" ------------------ ")
                except Exception:
                    print("Something wrong happened... keep going...")
                    continue

# extract_images("https://www.facebook.com/gabrielfreiredev")
save_to_folder()