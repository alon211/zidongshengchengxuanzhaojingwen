import snowy
import os
import re

HEIGHT = 2250
WIDTH = 3000


def func(arg):
    pattern = r'(.*\.jpg)$'
    return re.match(pattern, string=arg)


print(func('123.jpg'))
path = os.path.abspath(u'D:/周日敬拜/2017-9-24')
files = os.listdir(path)
imagefile_paths = [os.path.join(path, file).lower() for file in files]
print(imagefile_paths)
for file in imagefile_paths:
    source = snowy.load(file)
    height, width = source.shape[:2]
    if (height != HEIGHT or width != WIDTH):
        new_imagine = snowy.resize(source,width=WIDTH,height=HEIGHT)
        snowy.export(new_imagine,file)
# source = snowy.load(imagefile_paths[0])
# height, width = source.shape[:2]
# newImagine = snowy.resize(source, width=100, height=100)
# snowy.export(newImagine, os.path.join(path, '8.jpg'))
# print(height, width)
