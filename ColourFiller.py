from PIL import Image, ImageDraw
import os

black = (0, 0, 0)
white = (255,255,255)

for file in os.listdir("./to_colour/"):
    image = Image.open("to_colour/{}".format(file))
    image = image.convert("L")
    imgdata = image.getdata()

    newdata = []

    for pixelvalue in imgdata:
        if int(pixelvalue) > 200:
            newdata.append(white)
        else:
            newdata.append(black)

    newimage = Image.new("RGB", image.size)
    newimage.putdata(newdata)

    imgdata = newimage.getdata()

    horiz = -1
    verti = 0
    count = -1

    red = (235, 56, 7)
    green = (15, 212, 67)
    blue = (7, 216, 227)
    yellow = (234, 237, 33)
    purple = (224, 22, 224)
    orange = (252, 160, 0)

    colours = [blue,green,red,yellow,purple,orange]

    for unit in range(newimage.width*newimage.height):
        horiz += 1
        count += 1
        pixlvalue = newimage.getpixel((horiz,verti))
        if pixlvalue == white:
            ImageDraw.floodfill(newimage,(horiz,verti),colours[count],thresh=50)

        if horiz == newimage.width - 1:
            horiz = -1
            verti += 1

        if count == 5:
            count = -1

    newimage.save("coloured/{}_coloured{}".format(os.path.splitext(file)[0],os.path.splitext(file)[1]))
    newimage.show()
