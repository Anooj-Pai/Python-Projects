from PIL import Image

def getwidth(img):
    ratio = 256/img.height
    return ratio

im1 = Image.open('1.jpg')
im1 = im1.resize((int(im1.width*getwidth(im1)), 256))
im2 = Image.open('2.jpg')
im2 = im2.resize((int(im2.width*getwidth(im2)), 256))
im3 = Image.open('3.jpg')
im3 = im3.resize((int(im3.width*getwidth(im3)), 256))
im4 = Image.open('4.jpg')
im4 = im4.resize((int(im4.width*getwidth(im4)), 256))
im5 = Image.open('5.jpg')
im5 = im5.resize((int(im5.width*getwidth(im5)), 256))
im6 = Image.open('6.jpg')
im6 = im6.resize((int(im6.width*getwidth(im6)), 256))

im = Image.new('RGB', (1000,360), 'white')
im.paste(im1, (31,20))
im.paste(im2, ((im1.width+41),60))
im.paste(im3, (((im1.width+41)+im2.width+10),20))
im.paste(im4, ((((im1.width+41)+im2.width+10)+im3.width+10),60))
im.paste(im5, (((((im1.width+41)+im2.width+10)+im3.width+10)+im4.width+10),20))
im.paste(im6, ((((((im1.width+41)+im2.width+10)+im3.width+10)+im4.width+10)+im5.width+10),60))
im.show()