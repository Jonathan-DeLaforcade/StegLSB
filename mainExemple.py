from StegSolve import encode as enc
from StegSolve import decode as dec
from StegSolve import common as com

imgToDecode = "Out/test.png"

pixelsList, picWidth, picHeight = com.getImg(imgToDecode)
dec.decodeAll(pixelsList)
#dec.decodeOne(pixelsList,["B","G","R"])
