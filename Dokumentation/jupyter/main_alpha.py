from manim import *
import math
import numpy as np
from math import gcd, log10, pow

class graph(Scene):
    def construct(self):
        R = 3
        r = 1
        gcdVal = self.float_gcd(R, r)
        n_rot= r // gcdVal
        range = np.arange(0, 360 * n_rot, 1)
        points = []
        for a in range:
            xd, yd = self.calc_position(a, r=r, R=R)
            dot = Dot((xd, yd, 0), radius=0.01)
            points.append(dot)

        i= 0
        for p in points:
            print("This was %i of %i Dots that was animated" % (i, len(points)))
            anim_dot = Dot(p.get_center(), color=GREEN)
            self.play(FadeOut(anim_dot, run_time=0.5))
            self.add(p)
            i +=1

    def calc_position(self, angle, R=3, r=1, h=1):
        R= R
        r=r
        h=h
        a = math.radians(angle)

        x = (R - r) * math.cos(a) + h * math.cos(a + ((R / r) * a))
        y = (R - r) * math. sin(a) + h * math.sin(a + ((R / r) * a))

        return x, y

    def float_scale(self,x):
        max_digits = 14
        int_part = int(abs(x))
        magnitude = 1 if int_part == 0 else int (log10(int_part)) + 1

        if magnitude >= max_digits:
            return 0

        frac_part = abs(x) - int_part
        multiplier = 10 ** (max_digits - magnitude)
        frac_digits = multiplier + int(multiplier * frac_part + 0.5)

        while frac_digits % 10 ==0:
            frac_digits /= 10
        return int(log10(frac_digits))

    def float_gcd(self, a, b):
        sc = self.float_scale(a)
        sc_b = self.float_scale(b)
        sc = sc_b if sc_b > sc else sc

        fac = pow(10, sc)

        a = int(round(a * fac))
        b = int(round(b * fac))

        return round(gcd(a, b) / fac, sc)