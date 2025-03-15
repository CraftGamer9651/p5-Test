#!/bin/python3
from processing import *
from time import *

class Game:
  size = 30
  width = 16 * size
  height = 9 * size
  sprites = []
  pipes = []
  pipeDelay = 3
  # lastPipe = time.time()
  fallSpeed = size/90
  paused = False
g = Game()


class Sprite:
  def __init__(self, img, x=g.width/10, y=g.height/2, width=g.width/10, height=g.height/10):
    self.direction = -90
    self.x = x
    self.y = y
    self.img = loadImage(img)
    g.sprites.append(self)
    self.gravity = 0
    self.width = width
    self.height = width
  def draw(self):
    self.y += self.gravity
    pushMatrix()
    translate(self.x, self.y)
    rotate(radians(self.direction%360))
    image(self.img, -self.width/2, -self.height/2, self.width, self.height)
    popMatrix()
    
class Pipe(Sprite):
  def draw(self):
    self.x -= g.width/500
    
class Bird(Sprite):
  def draw(self):
    self.gravity += g.fallSpeed
    self.y += self.gravity
    pushMatrix()
    translate(self.x, self.y)
    rotate(radians(self.direction%360))
    image(self.img, -self.width/2, -self.height/2, self.width, self.height)
    popMatrix()

def setup():
  size(g.width, g.height)
  background(0)
  g.bird = Bird('5e0df231478aa0a331a4718d09dd91a2.png')
  
def draw():
  background(0)
  bird = g.sprites[0]
  bird.direction = bird.gravity*3
  if bird.y < 0:
    bird.y = 0
    bird.gravity = 0
    bird.direction = 90
  if bird.y > g.height:
    textSize(g.width/10)
    text("Game over!", g.width/10, g.height/2)
    g.paused = True
    exit()
  for sprite in g.sprites:
    sprite.draw()
  if len(g.pipes) < 1 or g.pipes[-1].x < g.width/2:
    print("new pipe created")
    newPipe = Pipe("pipe.png")
    g.pipes.append(newPipe)
    
    
def keyPressed():
  print("s")
  bird = g.sprites[0]
  bird.gravity = -1*(g.size/4)
  g.bird
  
run()
