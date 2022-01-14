from manim import *
import numpy as np
import Spiro as spi
import math

#Aspect Ratio IG post 4:5 1080px x 1350px

class test(Scene):
    R = 3
    r = 1
    def construct(self):
        origin = Dot(ORIGIN)
        center_circ2 = Dot((self.R-self.r, 0, 0))
        x_center_circ = center_circ2.get_coord(dim=0)
        y_center_circ = center_circ2.get_coord(dim=1)

        x_p = x_center_circ + self.r
        y_p = y_center_circ

        pen = Dot((x_p, y_p, 0))

        circ = Circle(radius=self.R)
        circ2 = Circle(radius=self.r)

        circ2.move_to(center_circ2)

        grouped = VGroup(center_circ2, pen, circ2)

        self.add(circ)
        self.add(pen)
        self.add(origin)
        self.add(circ2)
        self.add(center_circ2)

        for i in range(0,10, 0.5):
            trace = TracedPath(pen)
            angle_a = self.calc_radians(i)
            angle_b = (self.R / self.r) * angle_a

            self.play(Rotate(grouped, angle_b, about_point=ORIGIN))
            self.play(Rotate(pen, angle_b, about_point=center_circ2.get_center()))
            self.add(trace)


    def calc_radians(self, angle):
        return math.radians(angle)

class test_other(Scene):

    def construct(self):
        circ = Circle(color=GREEN).shift(4*LEFT)
        dot = Dot(color=BLUE).move_to(circ.get_start())
        rolling_circle = VGroup(circ, dot)
        trace = TracedPath(circ.get_start)
        rolling_circle.add_updater(lambda m : m.rotate(-0.25))
        self.add(trace, rolling_circle)
        self.play(rolling_circle.animate.shift(8*RIGHT), run_time=4, rate_func=linear)


class Spiro_Anim(Scene):

    def construct(self):
        #dot = Dot([-2.5, -1.5, 0])
        #dot2 = Dot([2.5, 1.5, 0])
        #line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        lines = []
        sp = spi.Spiro(R=300, r=100)

        spi_list = sp.return_complete_list()
        listnorm = []

        for element in spi_list:
            listnorm.append(element / np.linalg.norm(element))


        for i in range(0, len(listnorm)):
            xs, ys = listnorm[i]
            if i + 1 == len(listnorm):
                xe, ye = listnorm[0]
            else:
                xe, ye = listnorm[i + 1]

            dot = Dot(xs, ys, stroke_width=0.5)
            self.play(FadeIn(dot))
            print("Dot Nr. %d of %d was drawn" % (i, len(listnorm)-1))
            dot2 = Dot(xe, ye)
            line = Line(dot.get_center(), dot2.get_center())
            #self.add(line)
            #lines.append(line)

        #for r in lines:
            #self.play(MoveAlongPath(do, r), rate_functions=linear)
            #self.add(r)
