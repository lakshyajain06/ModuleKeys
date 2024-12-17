import time
import fluidsynth


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


def playNote(player, noteStr, duration, volume):
    offset = ord(noteStr[0]) - ord('a')
    pitch = (int(noteStr[1]) * 12)
    noteNum = offset + pitch + 12
    print(offset)
    print(pitch)
    print(noteNum)

    player.noteon(0, noteNum, volume)
    time.sleep(duration)
    player.noteoff(0, noteNum)
    


fs = fluidsynth.Synth()
fs.start()

sfid = fs.sfload("example.sf2")
fs.program_select(0, sfid, 0, 0)

playNote(fs, 'a4', 0.5, 127)
playNote(fs, 'a4', 0.5, 127)
playNote(fs, 'c4', 0.5, 127)
playNote(fs, 'e4', 0.5, 127)
playNote(fs, 'a4', 0.5, 127)
playNote(fs, 'e4', 0.5, 127)
playNote(fs, 'c4', 0.5, 127)
playNote(fs, 'h3', 0.5, 127)
playNote(fs, 'a4', 0.5, 127)
playNote(fs, 'a4', 0.5, 127)
playNote(fs, 'c4', 0.5, 127)
playNote(fs, 'e4', 0.5, 127)
playNote(fs, 'a4', 1.0, 127)
playNote(fs, 'l3', 0.5, 127)
playNote(fs, 'h3', 0.5, 127)
playNote(fs, 'a4', 0.5, 127)
playNote(fs, 'a4', 0.5, 127)
playNote(fs, 'c4', 0.5, 127)
playNote(fs, 'e4', 0.5, 127)
playNote(fs, 'f4', 0.5, 127)
playNote(fs, 'e4', 0.5, 127)
playNote(fs, 'c4', 0.5, 127)
playNote(fs, 'a4', 0.5, 127)
playNote(fs, 'l3', 0.5, 127)
playNote(fs, 'h3', 0.5, 127)
playNote(fs, 'j3', 0.5, 127)
playNote(fs, 'l3', 0.5, 127)
playNote(fs, 'a4', 1.0, 127)
playNote(fs, 'a4', 1.0, 127)

fs.delete()
