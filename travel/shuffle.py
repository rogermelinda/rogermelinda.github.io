import os
# from glob import glob
import re
from numpy.random import choice
# jpgs = glob("*.jpg")

print(os.listdir('.'))

files = [f for f in os.listdir('.') if re.match(r'^[0-9]*(.jpg|.JPG)', f)]
# lst = choice(range(1, len(files)+1), len(files), replace=False)

# for f, num in zip(files, lst):
#     os.rename(f, str(10000+num)+".jpg")

# files = [f for f in os.listdir('.') if re.match(r'^[0-9]*(.jpg|.JPG)', f)]
# lst = choice(range(1, len(files)+1), len(files), replace=False)

# for f in files:
#     os.rename(f, str(int(f[:5])-10000)+".jpg")