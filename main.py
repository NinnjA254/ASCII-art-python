from PIL import Image

# get pixel data from image
img = Image.open("sample.jpg")
width = img.size[0]
height = img.size[1]
data = list(img.getdata())
print(data[123])

#compute a single brightness value for each pixel(an RGB tuple) #todo: try out the different "algorithms", perhaps allow the user to
# pick between em
#average: regular average
for j, el in enumerate(data):
    data[j] = (el[0] + el[1] + el[2]) / 3 

# #luminosity: take a weighted average of the R, G and B values to account for human perception 
# for j, el in enumerate(data):
#     data[j] = (0.21 * el[0]) + (0.72 * el[1]) + (0.07 * el[2]) 

# # lightness: average the maximum and minimum values out of R, G and B
# for j, el in enumerate(data):
#     data[j] = (max(el[0], el[1], el[2]) + min(el[0], el[1], el[2])) / 2 
print(data[123])

#unflatten the data
unflattened_data = [[]]
column = 0
for j, el in enumerate(data):
    if j != 0 and j % width == 0:
        column += 1
        unflattened_data.append([])
    unflattened_data[column].append(el)

