from PIL import Image
from StegSolve import common as com
import re
from textwrap import wrap

defaultOrders = [
    ['R','G','B'],
    ['B','G','R'],
    ['G','B','R'],
    ['R','B','G'],
    ['G','R','B'],
    ['B','R','G'],
    ['R','G'],
    ['G','R'],
    ['R','B'],
    ['B','R'],
    ['B','G'],
    ['G','B'],
    ['R'],
    ['G'],
    ['B']
]



# ==> decodeImageBinaryByOrder <==
# Description: fonction qui decode l'image en fonction de l'ordre de pixel choisi
# IN: 
#   - liste des pixels (array de tuple) [DEFAULT: ["R","G","B"]]
# OUT: 
#   - string ==> string du binaire decoder (ex: "01000010100010")
def decodeImageBinaryByOrder(picPixelsList,order = ["R","G","B"]):
    string = ""

    nbMinStringSize = 8
    start = 0
    end = len(picPixelsList)
    end = 150
    idx = 0
    for pixel in picPixelsList[start:end]:
        R = pixel[0]
        G = pixel[1]
        B = pixel[2]

        for c in order:
            if c == "R":
                string += str(R%2)
            elif c == "G":
                string += str(G%2)
            elif c == "B":
                string += str(B%2)

    return string

# ==> decodeImageBinaryByOrder <==
# Description: fonction qui convertie un string de binaire en string de char
# IN: 
#   - string de binaire ("0100101000")
# OUT: 
#   - totalstring ==> string contenant le texte en char (ex: "BSI_BG_CYBER")
def binaryToText(binaryString):
    totalString = ""
    for idx in range(0,len(binaryString),8):
        octectString = binaryString[int(idx):(int(idx)+8)]
        octectInt = int(octectString,2)
        char = chr(octectInt)
        totalString += char
    return totalString


# ==> findText <==
# Description: fonction qui recherche une suite alphanumerique logique
# IN: 
#   - text ==> string contenanent la chaine ASCII
# OUT: 
#   - mdp ==>
def findText(text):
    mdp = re.findall(r"[a-zA-Z1-9ç'\"_(){}.!,)]{10,}",text)
    for match in mdp:
        print(match)
    return mdp

# ==> decodeAll <==
# Description: fonction qui decode l'image avec tout les ordres de pixels choisi
# IN: 
#   - liste des pixels (array de tuple) [DEFAULT: ["R","G","B"]]
# OUT: 
#   - mdp possible

def decodeAll(picPixelsList):
    for order in defaultOrders:
        binaryString = decodeImageBinaryByOrder(picPixelsList,order)
        tempString = binaryToText(binaryString)
        print(f"{order} ==> {tempString}")

# ==> decodeOne <==
# Description: fonction qui decode l'image avec tout l'ordre de pixels choisi
# IN: 
#   - liste des pixels (array de tuple) 
#   - choix de l'ordre [DEFAULT: ["R","G","B"]]
# OUT: 
#   - mdp possibles

def decodeOne(picPixelsList,order = ["R","G","B"]):
    binaryString = decodeImageBinaryByOrder(picPixelsList,order)
    tempString = binaryToText(binaryString)
    finalString = findText(tempString)
    #print(finalString)