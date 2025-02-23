# Press Shift+F10

import random
#from playsound import playsound
import threading
from itertools import groupby
import math


# bpm is always an interval of 5, lower and upper limits to be user defined in later version
def bpm():
    _song_bpm = 5 * random.randint(18, 30)
    return _song_bpm


# List of all song key options, simple random choice with major or minor also randomized
def song_keys():
    # song key ab - g#
    keys = ["A", "A Sharp", "B", "C", "C Sharp", "D", "D Sharp", "E", "F", "F Sharp", "G", "G Sharp"]
    return random.choice(keys) + " " + random.choice(["Major", "Minor"])


# List of major/minor chords, to be used with key for actual chord names in later version
def chords():
    _chords = ["I", "ii", "iii", "IV", "V", "vi", "vii^o"]
    return random.choice(_chords)


# optional chord modifiers for more unique progressions
def fancy_chords(basic_chord):
    fancy = ["6", "7", "9", "dim", "sus", "aug"]
    fancy_chord = str(basic_chord) + " " + str(random.choice(fancy))
    return fancy_chord


# basic metronome that follows bpm (currently only works with 4/4 time sig)
# 240 = 60 * 4 - ie seconds per minute * quarter notes
#def ():
#    #sig_multiplier = int(song_time_signature[-1])
#    #_multiplier = sig_multiplier * 60
#
#    threading.Timer(song_bpm/240, ).start()
#    if _on:
#        playsound("E:\Pycharm Projects\Click1.wav")


def time_sig():
    time_signatures = ["4/4", "6/8"]
    return random.choice(time_signatures)


def structure():
    song_structure = []
    song_structure_temp = []
    true_false = ["True", "True", "False"]

    # number of verses; 0 to 4
    num_verses = random.randint(0, 4)
    if num_verses >= 1:
        song_structure_temp.append("verse")
    if num_verses >= 2:
        song_structure_temp.append("verse")
    if num_verses >= 3:
        song_structure_temp.append("verse")
    if num_verses >= 4:
        song_structure_temp.append("verse")

    # number of choruses; 1 to 4
    num_choruses = random.randint(1, 4)
    if num_choruses >= 1:
        song_structure_temp.append("chorus")
    if num_choruses >= 2:
        song_structure_temp.append("chorus")
    if num_choruses >= 3:
        song_structure_temp.append("chorus")
    if num_choruses >= 4:
        song_structure_temp.append("chorus")

    # number of bridges; 0 to 3
    num_choruses = random.randint(0, 3)
    if num_choruses >= 1:
        song_structure_temp.append("bridge")
    if num_choruses >= 2:
        song_structure_temp.append("bridge")
    if num_choruses >= 3:
        song_structure_temp.append("bridge")

    # number of breakdowns; 0 to 2
    num_breakdowns = random.randint(0, 2)
    if num_breakdowns >= 1:
        song_structure_temp.append("breakdown")
    if num_breakdowns >= 2:
        song_structure_temp.append("breakdown")



    # shuffle elements that can appear multiple times
    # ie choruses, verses, breakdowns
    random.shuffle(song_structure_temp)


    # Elements that can only appear once
    # intro yn then append to final structure - intro is always first this way
    intro_yn = random.choice(true_false)
    if intro_yn == "True":
        song_structure.append("Intro")


    song_structure_temp = [i[0] for i in groupby(song_structure_temp)]


    # Songs (technically) cannot start with a bridge
    # if no intro and first shuffled element is bridge, remove it
    if (intro_yn == "False") and (song_structure_temp[0] == "bridge"):
        del song_structure_temp[0]


    # find mid point of song structure, add middle 8
    # middle 8 location will vary depending on intro and outro
    MID = len(song_structure_temp) /2
    #print(math.ceil(MID))
    song_structure_temp.insert((math.ceil(MID)), "Middle 8")


    # optional solo
    solo_position = random.randint(1, len(song_structure_temp)-1)

    # what solo plays over, 0 uses section to left of solo position, 1 uses section to right
    solo_backing = random.randint(0,1)
    if solo_backing == 0:
        print(song_structure_temp[solo_position-1])
        song_structure_temp.insert(song_structure_temp.index(song_structure_temp[solo_position]), str(song_structure_temp[solo_position-1]) + "(solo)")
    if solo_backing == 1:
        print(song_structure_temp[solo_position])
        song_structure_temp.insert(song_structure_temp.index(song_structure_temp[solo_position]), str(song_structure_temp[solo_position]) + "(solo)")



    # append the shuffled sections to final structure
    song_structure.append(song_structure_temp)


    # outro yn, append to final structure - always last
    outro_yn = random.choice(true_false)
    if outro_yn == "True":
        song_structure.append("Outro")

    # Songs (technically) cannot end with a bridge
    # if no outro and final shuffled element is bridge, remove it
    if (outro_yn == "False") and (song_structure_temp[len(song_structure_temp)-1] == "bridge"):
        del song_structure_temp[len(song_structure_temp)-1]


    # optionally insert a pre chorus
    # currently only works on first chorus in structure
    # to be fixed
    if "chorus" in song_structure_temp and song_structure_temp.index("chorus") != 0:
        song_structure_temp.insert(song_structure_temp.index("chorus"), "Pre-Chorus")


    # adds song structure and the shuffled "temp" song structure
    # -1 to remove the shuffled song structure list itself from being counted
    total_sections = (len(song_structure) + len(song_structure_temp)) - 1
    print("Number of Sections: " + str(total_sections))

    song_structure = str(song_structure).replace("[","")
    song_structure = str(song_structure).replace("]","")
    song_structure = str(song_structure).replace("'","")
    #song_structure = str(song_structure).replace(",", "\n")
    return str(song_structure)

### MAIN ###

print("")

song_bpm = bpm()
print("BPM: " + str(bpm()))

song_time_signature = time_sig()
print("Time Signature: " + str(time_sig()))

print("Song structure: " + "\n" + structure())

song_key = song_keys()
print("\n" + "Key: " +  str(song_keys()))

v_chord_1 = chords()
v_chord_2 = chords()
v_chord_3 = chords()
v_chord_4 = chords()

print("")
print("Basic Chord Progression: ")

print(v_chord_1)
print(v_chord_2)
print(v_chord_3)
print(v_chord_4)

print("")
print("Fancy Chord Progression: ")
print(fancy_chords(v_chord_1))
print(fancy_chords(v_chord_2))
print(fancy_chords(v_chord_3))
print(fancy_chords(v_chord_4))

#nome Control
#metro_on = False
#metro()
