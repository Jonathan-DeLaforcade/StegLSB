from PIL import Image
from StegSolve import common as com

# ==> GetImg <==
# Description: fonction qui récupere les information de l'image
# IN: chemin de l'image (string)
# OUT: 
#   - pixellist ==> liste des pixels de l'image (array of tuple)
#   - pic.width ==> largeur de l'image en pixel (number)
#   - pic.height ==> hauteur d el'image en pixel (number)
def Fnc_GetImg(img):
    pixelsList = []
    
    pic = Image.open(img)
    picColor = Image.new('RGB',(pic.width, pic.height),(0,0,0))
    
    for y in range(0,pic.height):
        for x in range(0,pic.width):
            r,g,b = pic.getpixel((x,y))
            rgb = [r,g,b]
            pixelsList.append(rgb)
            com.personalLogger(rgb,"ENCODE_IN")

    return pixelsList, pic.width, pic.height

# ==> convertTextToBinary <==
# Description: fonction qui converti mon binaire string ("0100010101000") en 
# IN: chemin de l'image (string)
# OUT: 
#   - pixellist ==> liste des pixels de l'image (array of tuple)
#   - pic.width ==> largeur de l'image en pixel (number)
#   - pic.height ==> hauteur de l'image en pixel (number)
def convertTextToBinary(text):
    res = []
    for c in text: 
        charBin = (bin(ord(c)))[2:].zfill(8)
        res.append(charBin)
    res = "".join(res)  
    print(res)
    return res
    
def Fnc_SaveImage(nom,sufix,width,height,pixels):
    imgName = nom.split(".")[0]
    #imgExt = nom.split(".")[1]
    imgExt = "png"
    imgDest = f"./Out/{imgName}.{imgExt}"
    
    picColor = Image.new('RGB',(width,height),(0,0,0))
    x = y = 0
    
    for pixel in pixels:
        
        pixel = (pixel[0],pixel[1],pixel[2])
        picColor.putpixel((x,y),pixel)
        com.personalLogger(pixel,"ENCODE_OUT")
        x+=1
        if (x >= width):
            x=0
            y+=1
    
    picColor.save(imgDest)

def replaceImg(text,img):
    com.personalLogger("Texte a Encodé","ENCODE_TEXT","Replace")
    com.personalLogger("Pixel avant entré dans encode.py \n","ENCODE_IN","Replace")
    com.personalLogger("Pixel apres entreé dans encode.py \n","ENCODE_OUT","Replace")
    
    print(f"text a encoder (ASCII): {text}\n")
    com.personalLogger(f"text a encoder (ASCII): {text}\n","ENCODE_TEXT")
    idx = 0
    newIMG = []
    pixelList = []
    textToBinary = convertTextToBinary(text)
    print(f"text a encoder (BINAI): {textToBinary}\n")
    com.personalLogger(f"text a encoder (BINAI): {textToBinary}\n","ENCODE_TEXT")
    imgObj = Fnc_GetImg(img)
    imgDecimal = imgObj[0]
    textToBinaryLen = len(textToBinary)
    for rgb in imgDecimal:
        rgbArray = []
        for c in rgb:
            
            if idx < textToBinaryLen:
                if (c%2) != int(textToBinary[idx]): #si le lsb du decimal est different du bit
                    if (c%2) < int(textToBinary[idx]): # si le lsb du decimal est plus petit que le bit
                        c+=1 #alors on ajoute 1
                    else:
                        c-=1 # sinon on enleve 1
            idx+=1
            rgbArray.append(c)
        pixelList.append(rgbArray)
    
    print(f"pixelList ENCODE: {pixelList}")
    Fnc_SaveImage(img,"",imgObj[1],imgObj[2],pixelList)