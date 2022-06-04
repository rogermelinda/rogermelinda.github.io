import os
<<<<<<< HEAD
import sys
from glob import glob
import re
from numpy.random import choice

cwd = os.getcwd()

for dir in sys.argv[1:]:
    os.chdir(dir+"/images")
    jpgs = glob('*.jpg')+glob('*.JPG')+glob('*.jpeg')
    jpgs = [jpg for jpg in jpgs if jpg != "overlay.jpg" and jpg != "overlay.JPG"]
    # files = [f for f in os.listdir('.') if re.match(r'^[0-9]*(.jpg|.JPG)', f)]
    lst = choice(range(1, len(jpgs)+1), len(jpgs), replace=False)

    for f, num in zip(jpgs, lst):
        os.rename(f, str(10000+num)+".jpg")

    jpgs = glob('*.jpg')
    jpgs = [jpg for jpg in jpgs if jpg!="overlay.jpg"]

    for f in jpgs:
        os.rename(f, str(int(f[:5])-10000)+".jpg")
    os.chdir(cwd)
=======
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
>>>>>>> ea6b73cce72761356d195bc17b6d697c0636531a
