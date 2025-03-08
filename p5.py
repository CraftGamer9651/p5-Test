#!/bin/python3
from processing import *

class Game:
  size = 21
  width = 16 * size
  height = 9 * size
  sprites = []
g = Game()

class Sprite:
  def __init__(self, img, x=0, y=0, width=g.width/10, height=g.height/10):
    self.direction = 90
    self.x = x
    self.y = y
    self.img = loadImage(img)
    g.sprites.append(self)
    self.width = width
    self.height = height
  def draw(self):
    pushMatrix()
    translate(self.x, self.y)
    rotate(radians(self.direction%360))
    image(self.img, -self.width/2, -self.height/2, self.width, self.height)
    popMatrix()
    
def setup():
  background(0)
  g.bird = Sprite('5e0df231478aa0a331a4718d09dd91a2.png', 20, 40)
  
def draw():
  for sprite in g.sprites:
    sprite.draw()

run()