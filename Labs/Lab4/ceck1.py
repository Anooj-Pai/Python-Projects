from PIL import Image
import check2

cap = Image.open('ca.jpg')
cap = check2.make_square(cap)
hk = Image.open('hk.jpg')
hk = check2.make_square(hk)
impic = Image.open('im.jpg')
impic = check2.make_square(impic)
bw = Image.open('bw.jpg')
bw = check2.make_square(bw)

im = Image.new('RGB', (0,0), 'white') # use mode 'RGB', color 'white'
im = im.resize((512,512)) # resize to the given width/height passed as a tuple
im.paste(cap, (0,0)) # (x,y) coordinates of upper left corner as a tuple
im.save('2by2.jpg')
im.paste(hk, (256,0)) # (x,y) coordinates of upper left corner as a tuple
im.save('2by2.jpg')
im.paste(impic, (0,256)) # (x,y) coordinates of upper left corner as a tuple
im.save('2by2.jpg')
im.paste(bw, (256,256)) # (x,y) coordinates of upper left corner as a tuple
im.save('2by2.jpg')
im.show()