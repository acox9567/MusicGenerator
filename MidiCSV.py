import py_midicsv
import os

open("Midi Data/ptb.train.txt", "w").close
file = open("Midi Data/ptb.train.txt", "a")

for filename in os.listdir("Midi Data/Bach/sonatas/cello/"):
        csv_arr = py_midicsv.midi_to_csv("Midi Data/Bach/sonatas/cello/" + filename)
        csv_str = ""

        for i in range(0, csv_arr.__len__()):
            csv_str += (csv_arr[i])

        csv_str += "\n\n"
        file = open("Midi Data/ptb.train.txt", "a")
        file.write(csv_str)

print("\nDone")
