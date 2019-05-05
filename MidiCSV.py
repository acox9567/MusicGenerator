import py_midicsv
import os


def a_bach_keys():
    for filename in os.listdir("Midi Data/Bach/keyboard"):
        csv_arr = py_midicsv.midi_to_csv("Midi Data/Bach/keyboard/" + filename)
        csv_str = ""

        for i in range(0, csv_arr.__len__()):
            csv_str += (csv_arr[i])

        csv_str += "\n\n"

        file = open("Midi Data/MidiCsvData.txt", "a")
        file.write(csv_str)
    return


def initialize():
    open("Midi Data/MidiCsvData.txt", "w").close
    a_bach_keys()
    return


initialize()

print("\nDone")
