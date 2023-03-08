from PIL import Image

# get pixel data from image
img = Image.open("sample.jpg")
width = img.size[0]
height = img.size[1]
data = list(img.getdata())

unflattened_data = [[]]
column = 0
for j, el in enumerate(data):
    if j != 0 and j % width == 0:
        column += 1
        unflattened_data.append([])
    unflattened_data[column].append(el)
