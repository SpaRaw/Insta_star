import math
from PyRender.python_files import array_to_avi
from PyRender.python_files import render
import numpy as np
import datetime

WIDTH = 600  # Recomendet Height for Insta
HEIGHT = 750# Recomenset height for Insta

R = 150
r = 100
H = 0.5

COLOR =[
    (116, 189, 203), #Aquamarine #74BDCB
    (255, 163, 132), #Salmon #FFA384
    (239, 231,188)
]



class Spiro:
    def __init__(self, xc=0, yc=0 , R=0, r=1, h=0, random_params=True, color=(221,81,127)):
        self.xc = xc
        self.yc = yc
        self.xp = 0
        self.yp = 0
        self.R = R
        self.r = r
        self.h = h

        if random_params:
            self.set_params()
        self.calculate_pen_position(0)

        self.finished = False
        gcdVal = math.gcd(self.r, self.R)
        nRot = self.r // gcdVal
        self.max_angle = nRot * 360
        self.color = color

    def set_params(self):
        self.xc = np.random.randint(0, HEIGHT)
        self.yc = np.random.randint(0, WIDTH)

        self.R = np.random.randint(50, 300)

        random = np.random.randint(0, 10000)

        if random % 2 == 0:
            self.r = np.random.randint(50, 300)
        else:
            self.r = -np.random.randint(50, 300)

        self.h = 2 * (np.random.randint(0, 100) / 100)




    def draw_spiro(self):
        for i in range(0, 360):
            angle = math.radians(i)
            x_circ_2 = self.xc + int((self.R + self.r) * math.cos(angle))
            y_circ_2 = self.yc + int((self.R + self.r) * math.sin(angle))

            x_pen = x_circ_2 + int(self.h * self.r * math.cos(angle + ((self.R / self.r) * angle)))
            y_pen = y_circ_2 + int(self.h * self.r * math.sin(angle + ((self.R / self.r) * angle)))

    def calculate_pen_position(self, angle):
        angle = math.radians(angle)
        x_circ_2 = self.xc + int((self.R + self.r) * math.cos(angle))
        y_circ_2 = self.yc + int((self.R + self.r) * math.sin(angle))

        self.xp = x_circ_2 + int(self.h * self.r * math.cos(angle + ((self.R / self.r) * angle)))
        self.yp = y_circ_2 + int(self.h * self.r * math.sin(angle + ((self.R / self.r) * angle)))

    def get_pen_position(self):
        return (self.xp, self.yp)






class SpiroAnimation:
    def __init__(self):
        self.render = render.PyRender()
        random_num = np.random.randint(2, 3)

        self.spiros = []
        self.color = COLOR
        self.frames = []

        for i in range(0, random_num):
            s = Spiro(color=self.color[i])
            self.spiros.append(s)

    def draw_one_step(self, angle):
        for element in self.spiros:
            if element.finished == False:
                element.calculate_pen_position(angle)
                x = element.xp
                y = element.yp

                if angle == element.max_angle:
                    element.finished = True

                self.render.add_circle(pos_x=x, pos_y=y, radius=3, color=element.color)

    def save_frame(self, path, name):
        self.render.save_image_as_png(path_to_target_dir=path, name=name)


    def generate_picture_of_frames(self, path='C:/Users/Korbinian/Desktop/Git_official/Insta_star/PyRender/temp_animation/frames'):
        now = datetime.datetime.now()

        """
        list_max = []
        for element in self.spiros:
            list_max.append(element.max_angle)
        """

        num_iteration = 900 #max(list_max)
        for i in range(0, num_iteration):
            print("frame %i of %i was created" % (i, num_iteration))
            self.draw_one_step(i)

            self.render.save_image_as_png(path_to_target_dir=path, name=str(i))
            #self.render.save_image_as_csv(path_to_target_dir='C:/Users/Korbinian/Desktop/Git_official/Insta_star/alt/temp_animation/frames/', name=str(i))

