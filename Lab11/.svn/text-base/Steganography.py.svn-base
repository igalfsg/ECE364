import numpy as np
import scipy
import zlib
import base64
import re
import os.path
import sys
import re
from PySide.QtGui import *
from SteganographyGUI import *

#imread, imsave


class Payload:
    def __init__(self, img =None, compressionLevel = -1 , xml = None):
        if compressionLevel > 9 or compressionLevel < -1:
            raise  ValueError ('wrong compression level')
        if img is None and xml is None:
            raise ValueError ('img and xml cant be empty')
        if type(img) != np.ndarray and img != None:
            raise TypeError ('Wrong type for one of the inputs')
        if type(xml) != str and xml != None:
            raise TypeError ('Wrong type for one of the inputs')
        self.img = img
        self.xml = xml
        if not img is None:
            self.getxml(compressionLevel)
        elif not xml is None:
            self.getimg()

    def getimg(self):
        lines = self.xml.split('\n')
        typeinfo = re.search(
            '[<]{1}[\w\s]+[=]{1}["]{1}([\w]+)["\w\s]+[=]{1}["]{1}([0-9]+)[,]{1}([0-9]+)["\w\s]+[=]{1}["]{1}([\w]+)', lines[1])
        #group(1) type
        #group(2) row
        #group (3) column
        #group(4) compressed
        decoded = base64.b64decode(lines[2])
        if typeinfo.group(4) == "True":
            #decompress the image
            decompressed = zlib.decompress(decoded)
        else:
            decompressed = decoded
        temp_list = list(decompressed)
        #print(len (temp_list))
        if typeinfo.group(1) == 'Color':
            temp = np.empty((int(typeinfo.group(2)), int(typeinfo.group(3)),  3))
            countind = 0
            for colour in range(0,3):
                for row in range(0,int(typeinfo.group(2))):
                    for col in range(0,int(typeinfo.group(3))):
                        temp[row][col][colour] = temp_list [countind]#((colour * (int(typeinfo.group(2)) + int(typeinfo.group(3)))) + col + row)
                        countind += 1
            self.img = temp
        else:
           self.img = np.reshape(temp_list, (int(typeinfo.group(2)),int(typeinfo.group(3))))

    def getxml(self,compressionLevel):
        sizeimg = self.img.shape
        if len(sizeimg) == 3:#asign color
            ptype = 'Color'
            forencr = []
            for c in range(0,sizeimg[2]):
                for row in range(0,sizeimg[0]):
                    for col in range(0,sizeimg[1]):
                        forencr.append(self.img[row][col][c])
        else:
            ptype ='Gray'
            count = 0
            forencr = []
            for row in range(0,sizeimg[0]):
                for col in range(0,sizeimg[1]):
                    forencr.append(self.img[row][col])
        bytearr = bytearray(forencr)
        if compressionLevel != -1: #compress stuff
            img = zlib.compress(bytearr, compressionLevel)
            compre = "True"
        else:
            img = bytearr
            compre = "False"
        encoded = base64.b64encode(img)
        strout = str(encoded)
        strout = strout[2:-1]
        self.xml = '<?xml version="1.0" encoding="UTF-8"?>\n' #49
        self.xml += '<payload type="' + ptype + '" size="' + str(sizeimg[0]) + "," + str(sizeimg[1]) +'" compressed="' + compre + '">\n'
        self.xml += strout
        self.xml += '\n</payload>'
        with open('target.xml', 'w') as myFile:
            myFile.write(self.xml)


class Carrier:
    def __init__(self, img):
        if type(img) != np.ndarray:
            raise TypeError ('Wrong type for one of the inputs')
        self.img = img
        self.sizeimg = self.img.shape

    def embedPayload(self, payload, override = False):
        if type(payload) != Payload or type(override) != bool:
            raise TypeError ("usage (payload, bool)")
        if override == False and self.payloadExists() == True:
            raise Exception ("already has something in it")
        img = self.img.copy()
        if len(self.sizeimg) == 3:#asign color
            count = 0
            if len(payload.xml)* 8 > (self.sizeimg[0] * self.sizeimg[1] * self.sizeimg[2]):
                raise ValueError ('payload is too big')
            bunch = np.zeros((self.sizeimg[0] * self.sizeimg[1] * self.sizeimg[2]))

            for i in  range (0, len(payload.xml)):
                temp = ord(payload.xml[i])
                bunch[count + 7] = temp % 2
                temp = temp >> 1
                bunch[count + 6] = temp % 2
                temp = temp >> 1
                bunch[count + 5] = temp % 2
                temp = temp >> 1
                bunch[count + 4] = temp % 2
                temp = temp >> 1
                bunch[count + 3] = temp % 2
                temp = temp >> 1
                bunch[count + 2] = temp % 2
                temp = temp >> 1
                bunch[count + 1] = temp % 2
                temp = temp >> 1
                bunch[count ] = temp % 2
                count += 8
            #print(bunch[8:16])
            count = 0
            for colour in range (0, 3):
                for row in range(0,self.sizeimg[0]):
                    for col in range(0,self.sizeimg[1]):
                        if count < 8* len(payload.xml):
                            img[row][col][colour] = self.img[row][col][colour] - (self.img[row][col][colour] % 2) + bunch[count]
                        count += 1
        else:
            count = 0
            if len(payload.xml) * 8> (self.sizeimg[0] * self.sizeimg[1]):
                raise ValueError ('payload is too big')
            bunch = np.zeros((self.sizeimg[0] * self.sizeimg[1]))
            for i in  range (0, len(payload.xml)):
                temp = ord(payload.xml[i])
                bunch[count + 7] = temp % 2
                temp = temp >> 1
                bunch[count + 6] = temp % 2
                temp = temp >> 1
                bunch[count + 5] = temp % 2
                temp = temp >> 1
                bunch[count + 4] = temp % 2
                temp = temp >> 1
                bunch[count + 3] = temp % 2
                temp = temp >> 1
                bunch[count + 2] = temp % 2
                temp = temp >> 1
                bunch[count + 1] = temp % 2
                temp = temp >> 1
                bunch[count ] = temp % 2
                count += 8
            #print(bunch[8:16])
            count = 0
            for row in range(0,self.sizeimg[0]):
                for col in range(0,self.sizeimg[1]):
                    if count < 8* len(payload.xml):
                        img[row][col] = self.img[row][col] - (self.img[row][col] % 2) + bunch[count]
                    count += 1



        return img




    def payloadExists(self):
        information = 0
        bytes_list = ""
        if len(self.sizeimg) == 3:#asign color
            row = 0
            col = 0
            for i in range (0, 40):
                information += self.img[row][col][0] % 2
                #print (row, col )
                if (i % 8) == 7:
                    bytes_list += chr(information)
                    information = 0
                col += 1
                information = information << 1
        else:
            row = 0
            col = 0
            for i in range (0, 40):
                information += self.img[row][col] % 2
                #print (row, col )
                if (i % 8) == 7:
                    bytes_list += chr(information)
                    information = 0
                col += 1
                information = information << 1
        if bytes_list == "<?xml":
            return True
        return False

    def extractPayload(self):
        information = 0
        bytes_list = ""
        count = 0
        if self.payloadExists() == False:
            raise Exception("no payload")
        if len(self.sizeimg) == 3:#asign color
            for colour in range (0, 3):
                for row in range(0,self.sizeimg[0]):
                    for col in range(0,self.sizeimg[1]):
                        information += self.img[row][col][colour] % 2
                        if (count % 8) == 7:
                            bytes_list += chr(information)
                            information = 0
                        count += 1
                        information = information << 1
        else:
            for row in range(0,self.sizeimg[0]):
                for col in range(0,self.sizeimg[1]):
                    information += self.img[row][col] % 2
                    if (count % 8) == 7:
                        bytes_list += chr(information)
                        information = 0
                    count += 1
                    information = information << 1
        return Payload(xml = bytes_list)

    def clean(self):
        return np.bitwise_and(self.img, 254)

        return img

