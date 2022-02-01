from PIL import Image

def make_square(im):
    width = im.width
    height = im.height
    if width > height:
        im2 = im.resize((height,height))
        im2.save('resized.jpg')
        return im2
    elif height > width:
        im2 = im.resize((width, width))
        im2.save('resized.jpg')
        return im2
    else:
        print("NO")
im = Image.open('1.jpg')
imsquare = make_square(im)