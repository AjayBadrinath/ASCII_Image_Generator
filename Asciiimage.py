import numpy as np

from PIL import Image

im=Image.open(r"E:/krsna.png")
h=480
ar=(im.height/im.width)*im.width*0.7
im=im.resize((int(ar),h))
k=np.array(im)
height=im.height
width=im.width

for i in range(im.height):
    for j in range(im.width):
        s=np.average(k[i][j])
        k[i][j][:-1]=s
#im.convert('L')
d=Image.fromarray(k)
d.save(r'E:/dsup1.png')
#lvl='''$&S@B%8&WM#*o2ahkbdpqwmAZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.'''#thanks to http://paulbourke.net/dataformats/asciiart/
lvl="&.."
f=open("dip.txt","w")
s=""
with open('ascii1.txt','w')as f:
    for i in range(height):
            for j in range(width):
                    s+=lvl[int(k[i][j][0]*2/255)]#s+=lvl[int(k[i][j][0]*72/255)]
            #print(s)
            #print('\n')
            s+='\n'
            f.write(s)
            
            s=''
