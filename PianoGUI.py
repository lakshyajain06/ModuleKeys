from tkinter import *
class PianoGUI:
    def __init__(self, numScales, startScale = 1):
        self.root = Tk()
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.canvas = Canvas(self.root, width=1500, height=1000)
        self.canvas.grid(column=0, row=0, sticky=(N, W, E, S))

        self.keySize = 50
        self.numScales = numScales
        self.startScale = startScale

        self.keyIDs = self.genAllKeys(numScales)

    #calls update method for root to allow it to refresh
    def refresh(self):
        self.root.update_idletasks()
        self.root.update()

    def convertNoteToID(self, note):
        scaleIndex = int(note[2]) - self.startScale
        noteIndex = ord(note[1]) - ord('a')
        print(scaleIndex, noteIndex)

        return self.keyIDs[scaleIndex][noteIndex]


    #changes color of key inputted to blue in displat
    def pressNote(self, note):
        id = self.convertNoteToID(note)
        self.canvas.itemconfigure(id, fill='blue')


    #reverts key display to normal color once called on key
    def releaseNote(self, note):
        id = self.convertNoteToID(note)
        if note[1] in 'bdgik':
            self.canvas.itemconfigure(id, fill='black')
        else:
            self.canvas.itemconfigure(id, fill='white')

    #creates the keys for every scale
    def genAllKeys(self, numScales):
        keyID = []
        if numScales <= 4:
            for i in range(numScales):
                keyID.append(self.genScaleOfKeys((i * self.keySize * 7) + 10, 10))
        else:
            for i in range(4):
                keyID.append(self.genScaleOfKeys((i * self.keySize * 7) + 10, 10))
            for i in range(numScales - 4):
                keyID.append(self.genScaleOfKeys((i * self.keySize * 7) + 10, 20 + (8 * self.keySize)))

        return keyID
    
    #creates and returns id for key with an black key to the right
    def genKeyRightIndent(self, offsetx, offsety):
        return self.canvas.create_polygon(offsetx, offsety, offsetx + ((7 * self.keySize)//10), offsety, offsetx + ((7 * self.keySize)//10), offsety + (4 * self.keySize), offsetx+self.keySize, offsety + (4 * self.keySize), offsetx+self.keySize, offsety + (8 * self.keySize), offsetx, offsety + (8 * self.keySize), outline='black')

    #creates and returns id for key with an black key to the left
    def genKeyLeftIndent(self, offsetx, offsety):
        return self.canvas.create_polygon(offsetx + (3 * self.keySize)//10, offsety, offsetx + self.keySize, offsety, offsetx + self.keySize, offsety + (8 * self.keySize), offsetx, offsety + (8 * self.keySize), offsetx, offsety + (4 * self.keySize), offsetx + (3 * self.keySize)//10, offsety + (4 * self.keySize), outline='black')

    #creates and returns id for key with an black key to the left and right
    def genKeyDoubleIndent(self, offsetx, offsety):
        return self.canvas.create_polygon(offsetx + ((3 * self.keySize)//10), offsety, offsetx + ((7 * self.keySize)//10), offsety, offsetx + ((7 * self.keySize)//10), offsety + (4 * self.keySize), offsetx+self.keySize, offsety + (4 * self.keySize), offsetx+self.keySize, offsety + (8 * self.keySize), offsetx, offsety + (8 * self.keySize), offsetx, offsety + (4 * self.keySize), offsetx + ((3 * self.keySize)//10), offsety + (4 * self.keySize), outline='black')

    #creates and returns id for black key
    def genKeyBlack(self, offsetx, offsety):
        return self.canvas.create_rectangle(offsetx + ((7 * self.keySize)//10), offsety, offsetx + ((13 * self.keySize)//10), offsety + (4 * self.keySize), fill='black', outline='black')
    
    #creates one full set of keys at the given offset coordinates and returns an array with all their ids
    def genScaleOfKeys(self, offsetx, offsety):
        keyID = []

        keyID.append(self.genKeyRightIndent(offsetx, offsety))
        keyID.append(self.genKeyBlack(offsetx, offsety))
        keyID.append(self.genKeyDoubleIndent(offsetx + self.keySize, offsety))
        keyID.append(self.genKeyBlack(offsetx + self.keySize, offsety))
        keyID.append(self.genKeyLeftIndent(offsetx + (self.keySize * 2), offsety))

        keyID.append(self.genKeyRightIndent(offsetx+ (3 * self.keySize), offsety))
        keyID.append(self.genKeyBlack(offsetx + (3 * self.keySize), offsety))
        keyID.append(self.genKeyDoubleIndent(offsetx + (4 * self.keySize), offsety))
        keyID.append(self.genKeyBlack(offsetx + (4 * self.keySize), offsety))
        keyID.append(self.genKeyDoubleIndent(offsetx + (5 * self.keySize), offsety))
        keyID.append(self.genKeyBlack(offsetx + (5 * self.keySize), offsety))
        keyID.append(self.genKeyLeftIndent(offsetx + (6 * self.keySize), offsety))

        return keyID