from PIL import Image

# ==> GetImg <==
# Description: fonction qui récupere les information de l'image
# IN: 
#   - chemin de l'image (string)
#   - rangeMin , min pixel 
#   - rangeMax , max pixel 
# OUT: 
#   - pixellist ==> liste des pixels de l'image (array of tuple)
#   - pic.width ==> largeur de l'image en pixel (number)
#   - pic.height ==> hauteur de l'image en pixel (number)
def Fnc_GetImg(img,rangeMin = 0 ,rangeMax = -1 ):
    pixelsList = []
    
    pic = Image.open(img)
    for y in range(0,pic.height):
        for x in range(0,pic.width):
            r,g,b = pic.getpixel((x,y))
            rgb = [r,g,b]
            pixelsList.append(rgb)
    if (rangeMax <= 0):
        rangeMax = len(pixelsList)
    return pixelsList, pic.width, pic.height