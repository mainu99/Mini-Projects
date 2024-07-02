'''
    To convert a JPEG image to PNG image.
    Script: JPEGtoPNGConverter.py pokedex new
'''
import sys
from pathlib import Path
from PIL import Image

first = sys.argv[1]
second = sys.argv[2]
print(first, second)

p = Path(first)
destination = Path(second)
if not destination.exists():
    destination.mkdir(parents=True, exist_ok=True)

try:
    for jpeg in p.glob('*.jpg'):
        img = Image.open(jpeg)
        filename = jpeg.stem       #get filename without extension
        # pdb.set_trace()
        new_filename = destination / (filename + '.png')
        img.save(new_filename, 'PNG')
except Exception as e:
    raise e




