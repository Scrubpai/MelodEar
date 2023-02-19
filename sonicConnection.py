from pythonosc import osc_message_builder
from pythonosc import udp_client
import time 
sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
def play_sound(init_note, chord):
  sender.send_message('/trigger/piano', [init_note, chord, 2])  
#sender.send_message('/trigger/piano', ["C4", "9+5", 2])
def user_sound(pitch):
  sender.send_message('/user', pitch)  
