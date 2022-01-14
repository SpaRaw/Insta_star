import math
import numpy as np
import random

class Spiro:
    def __init__(self, xc, yc, col, R, r, l):

        #set the step in degree
        self.step = 5

        #set drawing complete flag
        self.drawingComplete = False

        #set parameters
        self.setparams(xc, yc, col, R, r, l)

        # initalize the drawing
        self.restart()

    def setparams(self, xc, yc, col, R, r, l):
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col

        # reduce r/R to its smallest form by dividing with the Greatest Commen Divider
        gcdVal = math.gcd(int(self.r), int(self.R))
        self.nRot = self.r // gcdVal

        # get ratio of radii
        self.k = r / float(R)

        # store the current angle
        self.a = 0

    # restart the drawing
    def restart(self):
        # set the Flag
        self.drawingComplete = False

        R, k, l = self.R, self.k, self.l
        a = 0.0
        x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = R * ((1 - k) * math.sin(a) + l * k * math.sin((1 - k) * a / k))

        self.xc += x,
        self.yc += y

    # update by one step
    def update(self):

        # skip the rest of the steps if done
        if self.drawingComplete:
            return

        # increment the angle
        self.a += self.step

        # draw a stp
        R, k, l = self.R, self.k, self.l

        # set a angle
        a = math.radians(self.a)

        x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = R * ((1 - k) * math.sin(a) + l * k * math.sin((1 - k) * a / k))

        new_x = self.xc + x
        new_y = self.yc + y

        # if drawing is complete set the flag
        if self.a >= 360 * self.nRot:
            self.drawingComplete = True

        self.xc = new_x
        self.yc = new_y


    # draw the whole hing
    def draw(self):

        # draw the rest of the points
        R, k, l = self.R, self.k, self.l

        for i in range(0, 360 * self.nRot + 1, self.step):
            a = math.radians(i)
            x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
            y = R * ((1 - k) * math.sin(a) + l * k * math.sin((1 - k) * a / k))


class SpiroAnimator:

    def __init__(self, N):

        #set timeer value
        self.deltaT = 10

        #create Spiro objects
        self.spiros = []
        for i in range(N):

            #generate random param
            rparams = self.genRandomParams()

            #set spiro parameters
            spiro = Spiro(*rparams)
            self.spiros.append(spiro)

    def update(self):

        #update all spiros
        nComplete = 0

        for spiro in self.spiros:

            #update
            spiro.update()

            #count complete spiros
            if spiro.drawingComplete:
                nComplete +=1

        #restart if all spiros are complete
        if nComplete == len(self.spiros):
            self.restart()

        #call the timer
        turtle.ontimer(self.update, self.deltaT)

    def toggleTurtles(self):
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()


    def genRandomParams(self):
        width, height= self.width, self.height

        R = random.randint(50, min(width, height)//2)
        r = random.randint(10, 9*R//10)
        l = random.uniform(0.1, 0.9)
        xc = random.randint(-width//2, width//2)
        yc = random.randint(-height//2, height//2)

        col = (random.random(),
               random.random(),
               random.random())

        return(xc, yc, col, R, r, l)