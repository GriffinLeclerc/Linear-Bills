import sys
from pydub import AudioSegment

outputPath = "target/linear-bill.mp3"

if len(sys.argv) != 2:
    print("Usage: repeatBill <bills>")
    exit(0)

repeat = int(sys.argv[1])

intro = AudioSegment.from_mp3("res/intro.mp3")

bill = AudioSegment.from_mp3("res/bill.mp3")

remaining = AudioSegment.from_mp3("res/remaining.mp3")

billder = intro

print("Concatenating Bills.")

for i in range(repeat):
    print("Bill!")
    billder = billder + bill

billder = billder + remaining

print("Writing output file.")
billder.export(outputPath, format = "mp3")