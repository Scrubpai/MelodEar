import pygame
import sys
import sonicConnection
from chords import chords, get_chord

FPS = 60
fpsClock = pygame.time.Clock()

pygame.init()
pygame.font.init()
pygame.mouse.set_visible(True)
pygame.display.set_caption("MelodyEar")
screen = pygame.display.set_mode((1024, 600))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
Font = pygame.font.SysFont('Helvetica', 30)
font = pygame.font.SysFont('Helvetica', 12)

thumbs_up = pygame.image.load("thumbs_up.jpeg")
thumbs_up_img = pygame.transform.scale(thumbs_up, (400, 400))
thumbs_down = pygame.image.load("sad.jpeg")
thumbs_down_img = pygame.transform.scale(thumbs_down, (400, 400))

class PianoTile(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height, note, color):
    pygame.sprite.Sprite.__init__(self)
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.note = note
    self.color = color
    self.selected = False
    
    # self.noteSurface = pygame.Surface((self.width, self.height))
    self.noteRect = pygame.Rect(self.x, self.y, self.width, self.height)
    self.noteText = Font.render(self.note[0], True, (0, 0, 0))
    self.noteBounds1 = self.noteRect
    self.noteBounds2 = self.noteRect
    if self.note == "C1":
      self.noteBounds1 = pygame.Rect(self.x, self.y, 49, 312)
      self.noteBounds2 = pygame.Rect(self.x, self.y+312, 70, 238)
    elif self.note == "D1":
      self.noteBounds1 = pygame.Rect(self.x+21, self.y, 28, 312)
      self.noteBounds2 = pygame.Rect(self.x, self.y+312, 70, 238)
    elif self.note == "E1":
      self.noteBounds1 = pygame.Rect(self.x+21, self.y, 49, 312)
      self.noteBounds2 = pygame.Rect(self.x, self.y+312, 70, 238)
    elif self.note == "F1":
      self.noteBounds1 = pygame.Rect(self.x, self.y, 49, 312)
      self.noteBounds2 = pygame.Rect(self.x, self.y+312, 70, 238)
    elif self.note == "G1":
      self.noteBounds1 = pygame.Rect(self.x+21, self.y, 28, 312)
      self.noteBounds2 = pygame.Rect(self.x, self.y+312, 70, 238)
    elif self.note == "A1":
      self.noteBounds1 = pygame.Rect(self.x+21, self.y, 28, 312)
      self.noteBounds2 = pygame.Rect(self.x, self.y+312, 70, 238)
    elif self.note == "B1":
      self.noteBounds1 = pygame.Rect(self.x+21, self.y, 49, 312)
      self.noteBounds2 = pygame.Rect(self.x, self.y+312, 70, 238)
    elif self.note == "C2":
      self.noteBounds1 = pygame.Rect(self.x, self.y, 49, 312)
      self.noteBounds2 = pygame.Rect(self.x, self.y+312, 70, 238)
    elif self.note == "D2":
      self.noteBounds1 = pygame.Rect(self.x+21, self.y, 28, 312)
      self.noteBounds2 = pygame.Rect(self.x, self.y+312, 70, 238)
    elif self.note == "E2":
      self.noteBounds1 = pygame.Rect(self.x+21, self.y, 49, 312)
      self.noteBounds2 = pygame.Rect(self.x, self.y+312, 70, 238)
    elif self.note == "F2":
      self.noteBounds1 = pygame.Rect(self.x, self.y, 49, 312)
      self.noteBounds2 = pygame.Rect(self.x, self.y+312, 70, 238)
    elif self.note == "G2":
      self.noteBounds1 = pygame.Rect(self.x+21, self.y, 28, 312)
      self.noteBounds2 = pygame.Rect(self.x, self.y+312, 70, 238)
    elif self.note == "A2":
      self.noteBounds1 = pygame.Rect(self.x+21, self.y, 28, 312)
      self.noteBounds2 = pygame.Rect(self.x, self.y+312, 70, 238)
    elif self.note == "B2":
      self.noteBounds1 = pygame.Rect(self.x+21, self.y, 49, 312)
      self.noteBounds2 = pygame.Rect(self.x, self.y+312, 70, 238)
    
    self.fillColors = {}
    if color == (255, 255, 255):
      self.fillColors['normal'] = (255, 255, 255)
      self.fillColors['selected'] = (215, 230, 211, 5)
    elif color == (0, 0, 0):
      self.fillColors['normal'] = (0, 0, 0)
      self.fillColors['selected'] = (184, 110, 136, 5)

  def process(self):
    mousePos = pygame.mouse.get_pos()
    #self.noteSurface.fill(self.fillColors['normal'])
    if self.noteBounds1.collidepoint(mousePos) or self.noteBounds2.collidepoint(mousePos):
      if pygame.mouse.get_pressed(num_buttons=3)[0]:
        if not self.selected:
          self.color = self.fillColors['selected']
          self.selected = True
        else:
          self.color = self.fillColors['normal']
          self.selected = False
        pygame.draw.rect(screen, self.color, self.noteRect)
        if self.height == 600:
          screen.blit(self.noteText, (self.x + 40, 600))
        pygame.time.wait(500)
    
    pygame.draw.rect(screen, self.color, self.noteRect)
    if self.height == 600:
      screen.blit(self.noteText, (self.x + 40, 600))

  def deselect(self):
    self.color = self.fillColors['normal']
    self.selected = False

  def get_selected(self):
    return self.selected

  def get_note(self):
    return self.note

class Button(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height, text):
    pygame.sprite.Sprite.__init__(self)
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.text = text
    self.selected = False
    self.color = '#cccccc'
    
    self.fillColors = {
      'normal': '#cccccc',
      'hover': '#8bb8c7',
      'selected': '#41a4ba'
    }

    self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
    self.buttonText = font.render(self.text, True, (0, 0, 0))

  def process(self):
    mousePos = pygame.mouse.get_pos()
    if self.x < mousePos[0] < self.x + self.width and self.y < mousePos[1] < self.y + self.height:
      if pygame.mouse.get_pressed(num_buttons=3)[0]:
        if not self.selected:
          self.color = self.fillColors['selected']
          self.selected = True
        else:
          self.color = self.fillColors['normal']
          self.selected = False
        pygame.draw.rect(screen, self.color, self.buttonRect)
        screen.blit(self.buttonText, (self.x + (self.width - self.buttonText.get_width()) / 2, self.y + 17))
        pygame.time.wait(500)
      else:
        self.color = self.fillColors['hover']
    else:
      if self.selected:
        self.color = self.fillColors['selected']
      else:
        self.color = self.fillColors['normal']
    
    pygame.draw.rect(screen, self.color, self.buttonRect)
    screen.blit(self.buttonText, (self.x + (self.width - self.buttonText.get_width()) / 2, self.y + 17))

  def deselect(self):
    self.selected = False
    self.color = self.fillColors['normal']

  def get_selected(self):
    return self.selected

  def get_text(self):
    return self.text

C1 = PianoTile(0, 0, 70, 550, "C1", (255, 255, 255))
D1 = PianoTile(70, 0, 70, 550, "D1", (255, 255, 255))
E1 = PianoTile(140, 0, 70, 550, "E1", (255, 255, 255))
F1 = PianoTile(210, 0, 70, 550, "F1", (255, 255, 255))
G1 = PianoTile(280, 0, 70, 550, "G1", (255, 255, 255))
A1 = PianoTile(350, 0, 70, 550, "A1", (255, 255, 255))
B1 = PianoTile(420, 0, 70, 550, "B1", (255, 255, 255))
C2 = PianoTile(490, 0, 70, 550, "C2", (255, 255, 255))
D2 = PianoTile(560, 0, 70, 550, "D2", (255, 255, 255))
E2 = PianoTile(630, 0, 70, 550, "E2", (255, 255, 255))
F2 = PianoTile(700, 0, 70, 550, "F2", (255, 255, 255))
G2 = PianoTile(770, 0, 70, 550, "G2", (255, 255, 255))
A2 = PianoTile(840, 0, 70, 550, "A2", (255, 255, 255))
B2 = PianoTile(910, 0, 70, 550, "B2", (255, 255, 255))
C1s = PianoTile(49, 0, 42, 312, "C1s", (0, 0, 0))
D1s = PianoTile(119, 0, 42, 312, "D1s", (0, 0, 0))
F1s = PianoTile(259, 0, 42, 312, "F1s", (0, 0, 0))
G1s = PianoTile(329, 0, 42, 312, "G1s", (0, 0, 0))
A1s = PianoTile(399, 0, 42, 312, "A1s", (0, 0, 0))
C2s = PianoTile(539, 0, 42, 312, "C2s", (0, 0, 0))
D2s = PianoTile(609, 0, 42, 312, "D2s", (0, 0, 0))
F2s = PianoTile(749, 0, 42, 312, "F2s", (0, 0, 0))
G2s = PianoTile(819, 0, 42, 312, "G2s", (0, 0, 0))
A2s = PianoTile(889, 0, 42, 312, "A2s", (0, 0, 0))

notes = [C1, D1, E1, F1, G1, A1, B1, C2, D2, E2, F2, G2, A2, B2, C1s, D1s, F1s, G1s, A1s, C2s, D2s, F2s, G2s, A2s]

C = Button(980, 0, 44, 40, "C")
Db = Button(980, 40, 44, 40, "Db")
D = Button(980, 80, 44, 40, "D")
Eb = Button(980, 120, 44, 40, "Eb")
E = Button(980, 160, 44, 40, "E")
F = Button(980, 200, 44, 40, "F")
Gb = Button(980, 240, 44, 40, "Gb")
G = Button(980, 280, 44, 40, "G")
Ab = Button(980, 320, 44, 40, "Ab")
A = Button(980, 360, 44, 40, "A")
Bb = Button(980, 400, 44, 40, "Bb")
B = Button(980, 440, 44, 40, "B")
Play = Button(980, 480, 44, 40, "Play")
Test = Button(980, 520, 44, 40, "Test")
Submit = Button(980, 560, 44, 40, "Submit")

M5 = Button(0, 550, 163, 50, "Major 5th")
m5 = Button(163, 550, 163, 50, "Minor 5th")
D7 = Button(326, 550, 164, 50, "Dominant 7th")
d7 = Button(490, 550, 163, 50, "Diminished 7th")
M3 = Button(653, 550, 164, 50, "Major 7th")
m3 = Button(817, 550, 163, 50, "Minor 7th")

roots = [C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B]
options = [M5, m5, D7, d7, M3, m3]

def draw_piano_tiles(screen):
  for note in notes:
      note.process()

  for i in range(0, 14):
    pygame.draw.line(screen, black, (i*70, 0), (i*70, 600)) 

  for root in roots:
    root.process()

  for option in options:
    option.process()

  Play.process()
  Test.process()
  Submit.process()

def play_chord(pi_root, pi_chord):
  sonicConnection.play_sound(pi_root, pi_chord)
  Play.deselect()

def reset_all():
  for note in notes:
    note.deselect()
  
  for root in roots:
    root.deselect()

  for option in options:
    option.deselect()

  Play.deselect()
  Submit.deselect()
  Test.deselect()

def submit_answer(pi_root, pi_chord_name): 
  for root in roots:
    if root.get_text() == pi_root:
      if not root.get_selected():
        return False
    else:
      if root.get_selected():
        return False

  for option in options:
    if option.get_text() == pi_chord_name:
      if not option.get_selected():
        return False
    else:
      if option.get_selected():
        return False

  return True

def main():
  running = True
  score = 0
  (pi_root, (pi_chord_name, pi_chord)) = get_chord()
  print(pi_root, pi_chord_name)

  while running:
    draw_piano_tiles(screen)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    if Play.get_selected():
      print(pi_chord)
      play_chord(pi_root, pi_chord)

    if Test.get_selected():
      notes_selected = []
      for note in notes:
        if note.get_selected():
          notes_selected.append(":"+note.get_note()[0] + str(int(note.get_note()[1])+2))
      sonicConnection.user_sound(notes_selected)
      Test.deselect()
    
    if Submit.get_selected():
      if submit_answer(pi_root[1:], pi_chord_name):
        score += 1
        print("Correct!")
        print("Score: " + str(score))
        screen.blit(thumbs_up_img, (312, 100))
      else:
        print("Wrong!")
        screen.blit(thumbs_down_img, (312, 100))
      pygame.display.update()
      (pi_root, (pi_chord_name, pi_chord)) = get_chord()
      print(pi_root, pi_chord_name)
      reset_all()
      pygame.time.wait(1000)

    pygame.display.flip()
    fpsClock.tick(FPS)
  pygame.quit()
  sys.exit()
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)

if __name__=="__main__":
    main()
