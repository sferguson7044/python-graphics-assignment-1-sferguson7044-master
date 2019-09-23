#Python Graphics Program

# Sierra Ferguson
# draws an archery target, diglett, and a winter scene
# now with added squares and a checker board


import graphics
import tkinter

def main():
  #archery(100,100,17)
  #face(95,100,100)
  #winter()
  dice(100,100,diceWin)
  #square(100)
  #checkers(900,25)
  tkinter.mainloop()


# this definition draws a target
def archery(cx,cy,r):
  archeryWin = graphics.GraphWin()
  p=graphics.Point(cx,cy)

  archeryWin.setBackground("grey")

  #draws large, outer white ring
  whiteCircle = graphics.Circle(p , 5*r)
  whiteCircle.setFill("white")
  whiteCircle.draw(archeryWin)

#draws black circle
  blackCircle = graphics.Circle(p, 4*r)
  blackCircle.setFill("black")
  blackCircle.draw(archeryWin)

#draws blue circle
  blueCircle = graphics.Circle(p, 3 * r)
  blueCircle.setFill("blue")
  blueCircle.draw(archeryWin)

#draws red circle
  redCircle = graphics.Circle(p, 2 * r)
  redCircle.setFill("red")
  redCircle.draw(archeryWin)

#draws yellow circle
  yellowCircle = graphics.Circle(p, 1 * r)
  yellowCircle.setFill("yellow")
  yellowCircle.draw(archeryWin)


# Draws a face
def face(r,cx,cy):
  faceWin = graphics.GraphWin()

  head=graphics.Circle(graphics.Point(cx,cy),r)
  head.setFill("tan")
  head.draw(faceWin)

# oval eyes
  p1 = graphics.Point(cx-.5*cx, cy-.5*cy)
  p2 = graphics.Point(cx-(3/10)*cx, cy)
  eye1 = graphics.Oval(p1, p2)
  eye1.setFill("black")
  eye1.draw(faceWin)

  p3 = graphics.Point((63/100)*cx, (60/100*cy))
  eye1dot = graphics.Circle(p3, (5/100)*r)
  eye1dot.setFill("white")
  eye1dot.draw(faceWin)

  eye2 = eye1.clone()
  eye2.move((7/10*cx),0)
  eye2.draw(faceWin)

  eye2dot = eye1dot.clone()
  eye2dot.move((7/10)*cx,0)
  eye2dot.draw(faceWin)

  mp1=graphics.Point((65/100)*cx,(11/10)*cy)
  mp2 = graphics.Point((135/100)*cx,(14/10)*cy)
  mouth= graphics.Oval(mp1,mp2)
  mouth.setFill("pink")
  mouth.draw(faceWin)

# Draws a winter scene
def winter():
  winterWin = graphics.GraphWin()

#background
  winterWin.setBackground("white")
  p1 = graphics.Point(-1,150)
  p2 = graphics.Point(201,201)
  snow = graphics.Rectangle(p1,p2)
  snow.setFill("light blue")
  snow.draw(winterWin)

  def snowman(cx,cy,r):
    p1 = graphics.Point(cx,cy)
    snowman1 = graphics.Circle(p1,r)
    snowman1.setFill("white")
    snowman1.draw(winterWin)

    p2 = graphics.Point(cx,(115/150)*cy)
    snowman2 = graphics.Circle(p2,(25/35)*r)
    snowman2.setFill("white")
    snowman2.draw(winterWin)

    p3 = graphics.Point(cx, (85/150)*cy)
    snowman3 = graphics.Circle(p3,(15/35)*r)
    snowman3.setFill("white")
    snowman3.draw(winterWin)

  snowman(150, 150, 35)

  def tree():
    def stump(cx,cy,cx2,cy2):
      p1 = graphics.Point(cx,cy)
      p2 = graphics.Point(cx2,cy2)
      treeBase = graphics.Rectangle(p1,p2)
      treeBase.setFill("tan")
      treeBase.draw(winterWin)

    def top(p1x,p1y,p2x,p23y,p3x):
      p1 = graphics.Point(p1x,p1y)
      p2 = graphics.Point(p2x,p23y)
      p3 = graphics.Point(p3x,p23y)
      tree1 = graphics.Polygon(p1,p2,p3,p1)
      tree1.setFill("green")
      tree1.setOutline("green")
      tree1.draw(winterWin)

      p1.move(0,-30/75*p1y)
      p2.move(5/23*p2x,-30/135*p23y)
      p3.move(-5/103*p3x,-30/135*p23y)
      tree2 = graphics.Polygon(p1,p2,p3,p1)
      tree2.setFill("green")
      tree2.setOutline("green")
      tree2.draw(winterWin)

      p1.move(0, -30/75*p1y)
      p2.move(5/23*p2x, -30/135*p23y)
      p3.move(-5/103*p3x, -30/135*p23y)
      tree3 = graphics.Polygon(p1, p2, p3, p1)
      tree3.setFill("green")
      tree3.setOutline("green")
      tree3.draw(winterWin)

    stump(55, 125, 70, 160)
    top(63, 75, 23, 135, 103)

  tree()


diceWin = graphics.GraphWin("dice", 750, 500)
def dice(x,y,window):
  dice1((100/100)*x, (150/100)*y, window)
  dice2((350/100)*x, (150/100)*y, window)
  dice3((600/100)*x, (150/100)*y, window)
  dice4((100/100)*x, (400/100)*y, window)
  dice5((350/100)*x, (400/100)*y, window)
  dice6((600/100)*x, (400/100)*y, window)

#a function to draw a 3d dice around a center point(x,y)
def die(x,y,window):
  p1 = graphics.Point(x-75,y-75)
  p2 = graphics.Point(x+75,y+75)
  die = graphics.Rectangle(p1,p2)
  die.draw(window)

  pl1 = graphics.Point(x-25,y-125)
  line1 = graphics.Line(p1,pl1)
  line1.draw(window)

  p1l2 = graphics.Point(x+75,y-75)
  p2l2 = graphics.Point(x+125,y-125)
  line2 = graphics.Line(p1l2,p2l2)
  line2.draw(window)

  p1l3 = graphics.Point(x+75,y+75)
  p2l3 = graphics.Point(x+125,y+25)
  line3 = graphics.Line(p1l3,p2l3)
  line3.draw(window)

  p1l4 = graphics.Point(x-25,y-125)
  p2l4 = graphics.Point(x+125,y-125)
  line4 = graphics.Line(p1l4,p2l4)
  line4.draw(window)

  p1l5 = graphics.Point(x+125,y-125)
  p2l5 = graphics.Point(x+125,y+25)
  line5 = graphics.Line(p1l5,p2l5)
  line5.draw(window)

#draws the dot in the direct center of the dice
def centerPoint(x,y,window):
  p1 = graphics.Point(x,y)
  pt1 = graphics.Circle(p1,10)
  pt1.setFill("black")
  pt1.draw(window)
#draws the dots at the top right and the bottom left
def diagonalEnds(x,y,window):
  leftBottompt = graphics.Point(x - 50, y + 50)
  leftBottom = graphics.Circle(leftBottompt,10)
  leftBottom.setFill("black")
  leftBottom.draw(window)
  rightToppt = graphics.Point(x + 50 , y - 50)
  rightTop = graphics.Circle(rightToppt,10)
  rightTop.setFill("black")
  rightTop.draw(window)
#draws the dots at the bottom right and the top left
def diagonalEndsOpp(x,y,window):
  leftToppt = graphics.Point(x - 50 , y - 50)
  leftTop = graphics.Circle(leftToppt,10)
  leftTop.setFill("black")
  leftTop.draw(window)
  rightBottompt = graphics.Point(x + 50, y +50)
  rightBottom = graphics.Circle(rightBottompt,10)
  rightBottom.setFill("black")
  rightBottom.draw(window)
#draws the two points parallel to the center of the dice and perpendicular to the corner dice
def middlePoints(x,y,window):
  leftMiddlept = graphics.Point(x - 50, y)
  leftMiddle = graphics.Circle(leftMiddlept, 10)
  leftMiddle.setFill("black")
  leftMiddle.draw(window)
  rightMiddlept = graphics.Point(x + 50, y)
  rightMiddle = graphics.Circle(rightMiddlept, 10)
  rightMiddle.setFill("black")
  rightMiddle.draw(window)

#draws dice with 1 dot
def dice1(x,y,window):
  die(x,y,window)
  centerPoint(x,y,window)

#draws dice with 2 dots
def dice2(x,y,window):
  die(x,y,window)
  diagonalEnds(x,y,window)

# draws dice with 3 dots
def dice3(x, y,window):
  die(x,y,window)
  centerPoint(x,y,window)
  diagonalEnds(x,y,window)

# draws dice with 4 dots
def dice4(x,y,window):
  die(x,y,window)
  diagonalEnds(x,y,window)
  diagonalEndsOpp(x,y,window)

# draws dice with 5 dots
def dice5(x,y,window):
  die(x,y,window)
  centerPoint(x,y,window)
  diagonalEnds(x,y,window)
  diagonalEndsOpp(x,y,window)

# draws dice with 6 dots
def dice6(x,y,window):
  die(x,y,window)
  diagonalEnds(x,y,window)
  diagonalEndsOpp(x,y,window)
  middlePoints(x,y,window)

def square(r):
  squareWin = graphics.GraphWin("square thing",r*2,r*2)

  bp1 = graphics.Point(0,0)
  bp2 = graphics.Point(r,r)
  blueSquare=graphics.Rectangle(bp1,bp2)
  blueSquare.setFill("blue")
  blueSquare.draw(squareWin)

  blueSquare2 = blueSquare.clone()
  blueSquare2.move(r,r)
  blueSquare2.draw(squareWin)

  redSquare=blueSquare.clone()
  redSquare.setFill("red")
  redSquare.move(r,0)
  redSquare.draw(squareWin)

  redSquare2=redSquare.clone()
  redSquare.move(-r,r)
  redSquare2.draw(squareWin)

  pt1=graphics.Point(1/4*r,1/4*r)
  pt2=graphics.Point(3/4*r,3/4*r)
  smallRed=graphics.Rectangle(pt1, pt2)
  smallRed.setFill("red")
  smallRed.draw(squareWin)

  smallRed2=smallRed.clone()
  smallRed2.move(r,r)
  smallRed2.draw(squareWin)

  smallBlue=smallRed.clone()
  smallBlue.setFill("blue")
  smallBlue.move(0,r)
  smallBlue.draw(squareWin)

  smallBlue2=smallBlue.clone()
  smallBlue2.move(r,-r)
  smallBlue2.draw(squareWin)


def checkers(r,s):
  checkerWin = graphics.GraphWin("checkers",r,r)
  i=r/s
  for row in range(int(i)):
    for col in range(int(i)):
      rect = graphics.Rectangle(graphics.Point(row*(s),col*(s)), graphics.Point(((row+1)*(s)),((col+1)*(s))))
      if (col+row) %2 == 0:
        rect.setFill("white")
        rect.draw(checkerWin)
      else:
        rect.setFill("black")
        rect.draw(checkerWin)


main()




