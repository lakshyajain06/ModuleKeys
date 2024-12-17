import fluidsynth

from PianoGUI import PianoGUI
from SerialCommunicator import SerialCommunicator


fs = fluidsynth.Synth()
fs.start()

sfid = fs.sfload("SteinGrandPiano.SF2")
fs.program_select(0, sfid, 0, 0)

gui = PianoGUI(5)
serialCom = SerialCommunicator()


#converts inputted command to a note number in the sf2 file (ex: pa1 --> 12)
def convertCommandToKey(command):
    offset = ord(command[1]) - ord('a')
    pitch = (int(command[2]) * 12)
    noteNum = offset + pitch + 12

    return noteNum

def playNote(note):
    key = convertCommandToKey(note)
    fs.noteon(0, key, 127)
    gui.pressNote(note)

def stopNote(note):
    key = convertCommandToKey(note)
    fs.noteoff(0, key)
    gui.releaseNote(note)

while True:
    command = serialCom.readSerial()

    if command:
        if command[0] == 'p':
            playNote(command)
        elif command[0] == 'r':
            stopNote(command)
        else:
            print(command, "is an invalid command")



    gui.refresh()