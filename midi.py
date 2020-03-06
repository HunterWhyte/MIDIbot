import time
import rtmidi
import os
midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

scalekey = {
    'major': 1,
    'Major': 1,
    'maj': 1,
    'Maj': 1,

    'minor': 2,
    'Minor': 2,
    'min': 2,
    'Min': 2,
}
#majorkey & minorkey is the interval of the root note of the chord to the tonic
majorkey = {
    'I': 0,
    'i': 0,
    'II': 2,
    'ii': 2,
    'III': 4,
    'iii': 4,
    'IV': 5,
    'iv': 5,
    'V': 7,
    'v': 7,
    'VI': 9,
    'vi': 9,
    'VII': 11,
    'vii': 11,
}
#majorchords is the dictionary that stores the type of chord. used to determine which formula to apply and the intervals present in each chord
#major  = 1 minor = 2 dim = 3

majorchords = {
    'I': 1,
    'i': 1,
    'II': 2,
    'ii': 2,
    'III': 2,
    'iii': 2,
    'IV': 1,
    'iv': 1,
    'V': 1,
    'v': 1,
    'VI': 2,
    'vi': 2,
    'VII': 3,
    'vii': 3,

}

minorkey = {
    'I': 0,
    'i': 0,
    'II': 2,
    'ii': 2,
    'III': 3,
    'iii': 3,
    'IV': 5,
    'iv': 5,
    'V': 7,
    'v': 7,
    'VI': 8,
    'vi': 8,
    'VII': 10,
    'vii': 10,
}

minorchords = {
    'I': 2,
    'i': 2,
    'II': 3,
    'ii': 3,
    'III': 1,
    'iii': 1,
    'IV': 2,
    'iv': 2,
    'V': 2,
    'v': 2,
    'VI': 1,
    'vi': 1,
    'VII': 1,
    'vii': 1,

}
midikey = {
    'B': 59,
    'A#': 58,
    'Bb': 58,
    'A': 57,
    'G#': 56,
    'Ab': 56,
    'G': 55,
    'F#': 54,
    'Gb': 54,
    'F': 53,
    'E': 52,
    'D#': 51,
    'Eb': 51,
    'D': 50,
    'C#': 49,
    'Db': 49,
    'C': 48,

    'G10': 127,
    'F#10': 126,
    'Gb10': 126,
    'F10': 125,
    'E10': 124,
    'D#10': 123,
    'Eb10': 123,
    'D10': 122,
    'C#10': 121,
    'Db10': 121,
    'C10': 120,
    'B9': 119,
    'A#9': 118,
    'Bb9': 118,
    'A9': 117,
    'G#9': 116,
    'Ab9': 116,
    'G9': 115,
    'F#9': 114,
    'Gb9': 114,
    'F9': 113,
    'E9': 112,
    'D#9': 111,
    'Eb9': 111,
    'D9': 110,
    'C#9': 109,
    'Db9': 109,
    'C9': 108,
    'B8': 107,
    'A#8': 106,
    'Bb8': 106,
    'A8': 105,
    'G#8': 104,
    'Ab8': 104,
    'G8': 103,
    'F#8': 102,
    'Gb8': 102,
    'F8': 101,
    'E8': 100,
    'D#8': 99,
    'Eb8': 99,
    'D8': 98,
    'C#8': 97,
    'Db8': 97,
    'C8': 96,
    'B7': 95,
    'A#7': 94,
    'Bb7': 94,
    'A7': 93,
    'G#7': 92,
    'Ab7': 92,
    'G7': 91,
    'F#7': 90,
    'Gb7': 90,
    'F7': 89,
    'E7': 88,
    'D#7': 87,
    'Eb7': 87,
    'D7': 86,
    'C#7': 85,
    'Db7': 85,
    'C7': 84,
    'B6': 83,
    'A#6': 82,
    'Bb6': 82,
    'A6': 81,
    'G#6': 80,
    'Ab6': 80,
    'G6': 79,
    'F#6': 78,
    'Gb6': 78,
    'F6': 77,
    'E6': 76,
    'D#6': 75,
    'Eb6': 75,
    'D6': 74,
    'C#6': 73,
    'Db6': 73,
    'C6': 72,
    'B5': 71,
    'A#5': 70,
    'Bb5': 70,
    'A5': 69,
    'G#5': 68,
    'Ab5': 68,
    'G5': 67,
    'F#5': 66,
    'Gb5': 66,
    'F5': 65,
    'E5': 64,
    'D#5': 63,
    'Eb5': 63,
    'D5': 62,
    'C#5': 61,
    'Db5': 61,
    'C5': 60,
    'B4': 59,
    'A#4': 58,
    'Bb4': 58,
    'A4': 57,
    'G#4': 56,
    'Ab4': 56,
    'G4': 55,
    'F#4': 54,
    'Gb4': 54,
    'F4': 53,
    'E4': 52,
    'D#4': 51,
    'Eb4': 51,
    'D4': 50,
    'C#4': 49,
    'Db4': 49,
    'C4': 48,
    'B3': 47,
    'A#3': 46,
    'Bb3': 46,
    'A3': 45,
    'G#3': 44,
    'Ab3': 44,
    'G3': 43,
    'F#3': 42,
    'Gb3': 42,
    'F3': 41,
    'E3': 40,
    'D#3': 39,
    'Eb3': 39,
    'D3': 38,
    'C#3': 37,
    'Db3': 37,
    'C3': 36,
    'B2': 35,
    'A#2': 34,
    'Bb2': 34,
    'A2': 33,
    'G#2': 32,
    'Ab2': 32,
    'G2': 31,
    'F#2': 30,
    'Gb2': 30,
    'F2': 29,
    'E2': 28,
    'D#2': 27,
    'Eb2': 27,
    'D2': 26,
    'C#2': 25,
    'Db2': 25,
    'C2': 24,
    'B1': 23,
    'A#1': 22,
    'Bb1': 22,
    'A1': 21,
    'Ab1':20,
    'G#1':20,
    'G1':19,
    'Gb1':18,
    'F#1':18,
    'F1':17,
    'E1':16,
    'Eb1':15,
    'D#1':15,
    'D1':14,
    'Db1':13,
    'C#1':13,
    'C1':12,
    'B0': 11,
    'A#0': 10,
    'Bb0': 10,
    'A0': 9,
    'Ab0':8,
    'G#0':8,
    'G0':7,
    'Gb0':6,
    'F#0':6,
    'F0':5,
    'E0':4,
    'Eb0':3,
    'D#0':3,
    'D0':2,
    'Db0':1,
    'C#0':1,
    'C0':0,



}

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if available_ports:
    midiout.open_port(2)
else:
    midiout.open_virtual_port("My virtual output")


try:
    os.mkfifo("play")
except:
    pass
if True:
    count = 0
    file = open("play", "w")
    file.write(str(count))
    file.close()


while True:

    time.sleep(0.5)
    try:
        os.mkfifo("play")
    except:
        pass
    if True:
        file = open("play", "r")
        count = int(file.read())
        #print(count)
    if count == 1:
        try:
            os.mkfifo("notes")
        except:
            pass
        if True:
            file = open("notes", "r")
            unparsed = file.read()
            file.close()


    #--------------------------MIDI CODE-----------------------------------------------------------------------------------
            if len(unparsed.split(" "))> 1:
                if unparsed.split(" ")[0] == "!play":
                    rest = 0.5
                    if len(unparsed.split(" ")) == 3:
                        if is_int(unparsed.split(" ")[2]):
                            bpm = int(unparsed.split(" ")[2])
                            if bpm > 30 and bpm < 400:
                                rest = 60 / bpm
                            print(bpm)
                    datapart = unparsed.split(" ")[1]

                    listed = datapart.split(",")
                    index = 0
                    print(listed)
                    for i in listed:
                        if i in midikey:
                            note_on = [0x90, (midikey.get(i)), 112]
                            note_off = [0x80, (midikey.get(i)), 0]
                            midiout.send_message(note_on)
                            if (index + 1) < len(listed):
                                if "-" in listed[index + 1]:
                                    time.sleep(rest * (len(listed[index + 1])))
                                    midiout.send_message(note_off)
                                else:
                                    time.sleep(rest)
                                    midiout.send_message(note_off)
                            else:
                                time.sleep(rest)
                                midiout.send_message(note_off)

                        elif i == "":
                            time.sleep(rest)
                        index += 1

                    try:
                        os.mkfifo("play")
                    except:
                        pass
                    if True:
                        count = 0
                        file = open("play", "w")
                        file.write(str(count))
                        file.close()
                elif unparsed.split(" ")[0] == "!chords" and len(unparsed.split(" ")) > 1:
                    rest = 4
                    if len(unparsed.split(" ")) == 5:
                        if is_int(unparsed.split(" ")[4]):
                            bpm = int(unparsed.split(" ")[4])
                            if bpm > 30 and bpm < 400:
                                rest = 240 / bpm
                            print(bpm)

                    key = unparsed.split(" ")[1]

                    scale = unparsed.split(" ")[2]
                    if key in midikey and scale in scalekey:
                        datapart = unparsed.split(" ")[3]

                        listed = datapart.split(",")
                        index = 0
                        print(listed)
                        for i in listed:
                            if i in majorkey:
                                if scalekey.get(scale) == 1:
                                    root = midikey.get(key)+ majorkey.get(i)
                                    if majorchords.get(i) == 1:
                                        third = root + 4
                                        fifth = root + 7
                                    elif majorchords.get(i) == 2:
                                        third = root + 3
                                        fifth = root + 7
                                    elif majorchords.get(i) == 3:
                                        third = root + 3
                                        fifth = root + 6
                                elif scalekey.get(scale) == 2:
                                    root = midikey.get(key) + minorkey.get(i)
                                    if minorchords.get(i) == 1:
                                        third = root + 4
                                        fifth = root + 7
                                    elif minorchords.get(i) == 2:
                                        third = root + 3
                                        fifth = root + 7
                                    elif minorchords.get(i) == 3:
                                        third = root + 3
                                        fifth = root + 6

                                root_on = [0x90, root, 112]
                                third_on = [0x90, third, 112]
                                fifth_on = [0x90, fifth, 112]
                                root_off = [0x80, root, 0]
                                third_off = [0x80, third, 0]
                                fifth_off = [0x80, fifth, 0]

                                midiout.send_message(root_on)
                                midiout.send_message(third_on)
                                midiout.send_message(fifth_on)


                                if (index + 1) < len(listed):
                                    if "-" in listed[index + 1]:
                                        time.sleep(rest * (len(listed[index + 1])))
                                        midiout.send_message(root_off)
                                        midiout.send_message(third_off)
                                        midiout.send_message(fifth_off)
                                    else:
                                        time.sleep(rest)
                                        midiout.send_message(root_off)
                                        midiout.send_message(third_off)
                                        midiout.send_message(fifth_off)
                                else:
                                    time.sleep(rest)
                                    midiout.send_message(root_off)
                                    midiout.send_message(third_off)
                                    midiout.send_message(fifth_off)

                            elif i == "":
                                time.sleep(rest)
                            index += 1

                try:
                    os.mkfifo("play")
                except:
                    pass
                if True:
                    count = 0
                    file = open("play", "w")
                    file.write(str(count))
                    file.close()
