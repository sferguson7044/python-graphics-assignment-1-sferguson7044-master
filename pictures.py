#Python Graphics Program

# Sierra Ferguson
# draws an archery target, diglett, and a winter scene
# now with added squares and a checker board


import graphics
import tkinter

def main():
  archery(100,100,17)
  face(95,100,100)
  winter(150,150,35)
  dice(100,100,100)
  square(100)
  checkers(900,25)
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
win = graphics.GraphWin()
def winter(scx,scy,sr):
#scx= snowman center, x coord
#scy= snowman center, y coord
#sr= snowman radius

#background
  win.setBackground("white")
  p1 = graphics.Point(-1,150)
  p2 = graphics.Point(201,201)
  snow = graphics.Rectangle(p1,p2)
  snow.setFill("light blue")
  snow.draw(win)

  snowman(scx, scy, sr)
  stump(55, 125, 70, 160)
  top(63, 75, 23, 135, 103)

def snowman(scx,scy,sr):

  p1 = graphics.Point(scx,scy)
  snowman1 = graphics.Circle(p1,sr)
  snowman1.setFill("white")
  snowman1.draw(win)

  p2 = graphics.Point(scx,(115/150)*scy)
  snowman2 = graphics.Circle(p2,(25/35)*sr)
  snowman2.setFill("white")
  snowman2.draw(win)

  p3 = graphics.Point(scx, (85/150)*scy)
  snowman3 = graphics.Circle(p3,(15/35)*sr)
  snowman3.setFill("white")
  snowman3.draw(win)

def stump(cx,cy,cx2,cy2):
  p1 = graphics.Point(cx,cy)
  p2 = graphics.Point(cx2,cy2)
  treeBase = graphics.Rectangle(p1,p2)
  treeBase.setFill("tan")
  treeBase.draw(win)

def top(p1x,p1y,p2x,p23y,p3x):
  p1 = graphics.Point(p1x,p1y)
  p2 = graphics.Point(p2x,p23y)
  p3 = graphics.Point(p3x,p23y)
  tree1 = graphics.Polygon(p1,p2,p3,p1)
  tree1.setFill("green")
  tree1.setOutline("green")
  tree1.draw(win)

  p1.move(0,-30/75*p1y)
  p2.move(5/23*p2x,-30/135*p23y)
  p3.move(-5/103*p3x,-30/135*p23y)
  tree2 = graphics.Polygon(p1,p2,p3,p1)
  tree2.setFill("green")
  tree2.setOutline("green")
  tree2.draw(win)

  p1.move(0, -30/75*p1y)
  p2.move(5/23*p2x, -30/135*p23y)
  p3.move(-5/103*p3x, -30/135*p23y)
  tree3 = graphics.Polygon(p1, p2, p3, p1)
  tree3.setFill("green")
  tree3.setOutline("green")
  tree3.draw(win)



#calls all of the dice functions in different windows since i dont know how to make it die(num)(other parameters)
def dice(size,cx,cy):
  die1(size,cx,cy)
  die2(size,cx,cy)
  die3(size, cx, cy)
  die4(size, cx, cy)
  die5(size, cx, cy)
  die6(size, cx, cy)

#a function to draw a dice with 1 dot
def die1(size,cx,cy):
  diceWin = graphics.GraphWin("dice",200,200)
  center = graphics.Point(cx,cy)
  base = graphics.Rectangle(graphics.Point(cx-(1/2)*size,cy-(1/2)*size),graphics.Point(cx+(1/2)*size,cy+(1/2)*size))
  base.draw(diceWin)

  pt1 = graphics.Circle(center, (1/10)*size)
  pt1.setFill("black")
  pt1.draw(diceWin)

#a function to draw a dice with 2 dots
def die2(size,cx,cy):
  diceWin = graphics.GraphWin("dice", 200, 200)
  base = graphics.Rectangle(graphics.Point(cx - (1 / 2) * size, cy - (1 / 2) * size),
                            graphics.Point(cx + (1 / 2) * size, cy + (1 / 2) * size))
  base.draw(diceWin)

  leftBottompt = graphics.Point(cx - (1/3)*size, cy + (1/3)*size)
  leftBottom = graphics.Circle(leftBottompt, (1/10)*size)
  leftBottom.setFill("black")
  leftBottom.draw(diceWin)

  rightToppt = graphics.Point(cx + (1/3)*size, cy - (1/3)*size)
  rightTop = graphics.Circle(rightToppt, (1/10)*size)
  rightTop.setFill("black")
  rightTop.draw(diceWin)

#a function to draw a dice with 3 dots
def die3(size,cx,cy):
  diceWin = graphics.GraphWin("dice", 200, 200)
  center = graphics.Point(cx, cy)
  base = graphics.Rectangle(graphics.Point(cx - (1 / 2) * size, cy - (1 / 2) * size),
                            graphics.Point(cx + (1 / 2) * size, cy + (1 / 2) * size))
  base.draw(diceWin)

  leftBottompt = graphics.Point(cx - (1/3)*size, cy + (1/3)*size)
  leftBottom = graphics.Circle(leftBottompt, (1/10)*size)
  leftBottom.setFill("black")
  leftBottom.draw(diceWin)

  rightToppt = graphics.Point(cx + (1/3)*size, cy - (1/3)*size)
  rightTop = graphics.Circle(rightToppt, (1/10)*size)
  rightTop.setFill("black")
  rightTop.draw(diceWin)

  pt1 = graphics.Circle(center, (1 / 10) * size)
  pt1.setFill("black")
  pt1.draw(diceWin)

#a function to draw a dice with 4 dots
def die4(size,cx,cy):
  diceWin = graphics.GraphWin("dice", 200, 200)
  base = graphics.Rectangle(graphics.Point(cx - (1 / 2) * size, cy - (1 / 2) * size),
                            graphics.Point(cx + (1 / 2) * size, cy + (1 / 2) * size))
  base.draw(diceWin)

  leftBottompt = graphics.Point(cx - (1/3)*size, cy + (1/3)*size)
  leftBottom = graphics.Circle(leftBottompt, (1/10)*size)
  leftBottom.setFill("black")
  leftBottom.draw(diceWin)

  rightToppt = graphics.Point(cx + (1/3)*size, cy - (1/3)*size)
  rightTop = graphics.Circle(rightToppt, (1/10)*size)
  rightTop.setFill("black")
  rightTop.draw(diceWin)

  leftToppt = graphics.Point(cx - (1/3)*size, cy - (1/3)*size)
  leftTop = graphics.Circle(leftToppt, (1/10)*size)
  leftTop.setFill("black")
  leftTop.draw(diceWin)

  rightBottompt = graphics.Point(cx + (1/3)*size, cy + (1/3)*size)
  rightBottom = graphics.Circle(rightBottompt, (1/10)*size)
  rightBottom.setFill("black")
  rightBottom.draw(diceWin)

#a function to draw a dice with 5 dots
def die5(size,cx,cy):
  diceWin = graphics.GraphWin("dice", 200, 200)
  center = graphics.Point(cx, cy)
  base = graphics.Rectangle(graphics.Point(cx - (1 / 2) * size, cy - (1 / 2) * size),
                            graphics.Point(cx + (1 / 2) * size, cy + (1 / 2) * size))
  base.draw(diceWin)

  leftBottompt = graphics.Point(cx - (1/3)*size, cy + (1/3)*size)
  leftBottom = graphics.Circle(leftBottompt, (1/10)*size)
  leftBottom.setFill("black")
  leftBottom.draw(diceWin)

  rightToppt = graphics.Point(cx + (1/3)*size, cy - (1/3)*size)
  rightTop = graphics.Circle(rightToppt, (1/10)*size)
  rightTop.setFill("black")
  rightTop.draw(diceWin)

  leftToppt = graphics.Point(cx - (1/3)*size, cy - (1/3)*size)
  leftTop = graphics.Circle(leftToppt, (1/10)*size)
  leftTop.setFill("black")
  leftTop.draw(diceWin)

  rightBottompt = graphics.Point(cx + (1/3)*size, cy + (1/3)*size)
  rightBottom = graphics.Circle(rightBottompt, (1/10)*size)
  rightBottom.setFill("black")
  rightBottom.draw(diceWin)

  pt1 = graphics.Circle(center, (1 / 10) * size)
  pt1.setFill("black")
  pt1.draw(diceWin)

#a function to draw a dice with 6 dots
def die6(size, cx, cy):
  diceWin = graphics.GraphWin("dice", 200, 200)
  base = graphics.Rectangle(graphics.Point(cx - (1 / 2) * size, cy - (1 / 2) * size),
                            graphics.Point(cx + (1 / 2) * size, cy + (1 / 2) * size))
  base.draw(diceWin)

  leftBottompt = graphics.Point(cx - (1 / 3) * size, cy + (1 / 3) * size)
  leftBottom = graphics.Circle(leftBottompt, (1 / 10) * size)
  leftBottom.setFill("black")
  leftBottom.draw(diceWin)

  rightToppt = graphics.Point(cx + (1 / 3) * size, cy - (1 / 3) * size)
  rightTop = graphics.Circle(rightToppt, (1 / 10) * size)
  rightTop.setFill("black")
  rightTop.draw(diceWin)

  leftToppt = graphics.Point(cx - (1 / 3) * size, cy - (1 / 3) * size)
  leftTop = graphics.Circle(leftToppt, (1 / 10) * size)
  leftTop.setFill("black")
  leftTop.draw(diceWin)

  rightBottompt = graphics.Point(cx + (1 / 3) * size, cy + (1 / 3) * size)
  rightBottom = graphics.Circle(rightBottompt, (1 / 10) * size)
  rightBottom.setFill("black")
  rightBottom.draw(diceWin)

  leftMiddlept = graphics.Point(cx - (1 / 3) * size, cy)
  leftMiddle = graphics.Circle(leftMiddlept, (1 / 10) * size)
  leftMiddle.setFill("black")
  leftMiddle.draw(diceWin)

  rightMiddlept = graphics.Point(cx + (1 / 3) * size, cy)
  rightMiddle = graphics.Circle(rightMiddlept, (1 / 10) * size)
  rightMiddle.setFill("black")
  rightMiddle.draw(diceWin)



#draws the abstract squares based on size
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



#draws a checker board based on how many squares and how big the squares are
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