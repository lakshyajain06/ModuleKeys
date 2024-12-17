from tkinter import *
import fluidsynth

def genKeyRightIndent(offsetx, offsety):
    return canvas.create_polygon(offsetx, offsety, offsetx+35, offsety, offsetx+35, offsety+200, offsetx+50, offsety+200, offsetx+50, offsety+400, offsetx, offsety+400, outline='black')

def genKeyLeftIndent(offsetx, offsety):
    return canvas.create_polygon(offsetx+15, offsety, offsetx+50, offsety, offsetx+50, offsety+400, offsetx, offsety+400, offsetx, offsety+200, offsetx+15, offsety+200, outline='black')

def genKeyDoubleIndent(offsetx, offsety):
    return canvas.create_polygon(offsetx+15, offsety, offsetx+35, offsety, offsetx+35, offsety+200, offsetx+50, offsety+200, offsetx+50, offsety+400, offsetx, offsety+400, offsetx, offsety+200, offsetx+15, offsety+200, outline='black')

def genKeyBlack(offsetx, offsety):
    return canvas.create_rectangle(offsetx+35, offsety, offsetx+64, offsety+199, fill='black', outline='black')

def genKeys(offsetx, offsety):
    keyID = []

    keyID.append(genKeyRightIndent(offsetx, offsety))
    keyID.append(genKeyBlack(offsetx, offsety))
    keyID.append(genKeyDoubleIndent(offsetx+50, offsety))
    keyID.append(genKeyBlack(offsetx+50, offsety))
    keyID.append(genKeyLeftIndent(offsetx+100, offsety))

    keyID.append(genKeyRightIndent(offsetx+150, offsety))
    keyID.append(genKeyBlack(offsetx+150, offsety))
    keyID.append(genKeyDoubleIndent(offsetx+200, offsety))
    keyID.append(genKeyBlack(offsetx+200, offsety))
    keyID.append(genKeyDoubleIndent(offsetx+250, offsety))
    keyID.append(genKeyBlack(offsetx+250, offsety))
    keyID.append(genKeyLeftIndent(offsetx+300, offsety))

    return keyID


#takes in key, note and scale and converts it to midi key number. ex: A0, B1, C4
# a- c
# b- c sharp
# c- d 
# d- d sharp
# e- e
# f- f
# g- f sharp
# h- g
# i- g sharp
# j- a
# k- a sharp
# l- b
def translateMessage(str):
    offset = ord(str[0]) - ord('a')
    pitch = (int(str[1]) * 12)
    noteNum = offset + pitch + 12

    return noteNum

def playNote(note, fs, id):
    canvas.itemconfigure(id, fill='blue')
    print(note)
    key = translateMessage(note)
    fs.noteon(0, key, 127)

def stopNote(note, fs, id):
    if note[0] in 'bdgik':
        canvas.itemconfigure(id, fill='black')
    else:
        canvas.itemconfigure(id, fill='white')
    key = translateMessage(note)
    fs.noteoff(0, key)


def attachKeySound(fs, canvas, keyIDs, startScale):
    for i in range(len(keyIDs)):
        for j in range(len(keyIDs[i])):
            key = keyIDs[i][j]
            noteStr = chr(ord("a") + j) + str(i + startScale)
            canvas.tag_bind(key, "<Button-1>", lambda event, note=noteStr, keystored = key: playNote(note, fs, keystored))
            canvas.tag_bind(key, "<ButtonRelease>", lambda event, note=noteStr, keystored = key: stopNote(note, fs, keystored))

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)



canvas = Canvas(root, width=1500, height=500)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

fs = fluidsynth.Synth()
fs.start()

sfid = fs.sfload("SteinGrandPiano.SF2")
fs.program_select(0, sfid, 0, 0)

keyID = []
for i in range(4):
    keyID.append(genKeys((i*350) + 10, 10))


attachKeySound(fs, canvas, keyID, 1)

#for i in range(12):
#    canvas.tag_bind(keyID[0][i], "<Button-1>", lambda event, xx=i: playNote(chr(ord('a') + xx) + "4", fs, keyID[0][xx]))



root.mainloop()