import random
import sonicConnection
# user_input = input("What chord is this? ")

keys = {1:":C", 2:":Db", 3:":D", 4:":Eb", 5:":E", 6:":F", 7:":Gb", 8:":G", 9:":Ab", 10:":A", 11:":Bb", 12:":B"}

chords = {
  "Major 5th": "M", 
  "Minor 5th": "m", 
  "Dominant 7th": "dom7",
  "Diminished 7th": "dim7",
  "Major 7th": "M7",
  "Minor 7th": "m7"
}
#play(chord(C4, 'maj9'))

def get_chord(): 
  pi_root = random.choice(list(keys.items()))[1] #choose a random key out of the dictionnary
  chord = random.choice(list(chords.items()))
  return (pi_root, chord)