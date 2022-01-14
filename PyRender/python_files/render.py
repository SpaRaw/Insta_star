import numpy as np
from PIL import Image
import os
from PyRender.python_files import Circle
import datetime
import pandas as pd

BGCOLOR = (231, 242, 248)  #Baby blue # E7F2F8
C1 = (116, 189, 203) #Aquamarine #74BDCB
C2 = (255, 163, 132) #Salmon #FFA384
C3 = (239, 231,188) # Freesia #EFE7BC

WIDTH = 600  # Recommended Height for Insta
HEIGHT = 600 # Recommended height for Insta

class PyRender:
    def __init__(self, scene_width=WIDTH, scene_height=HEIGHT):
        self.width = scene_width
        self.height = scene_height
        self.frame = np.zeros([self.height, self. width, 3], dtype=np.uint8)
        self.objects = []
        self.frame[:, :] = list(BGCOLOR)

        self.last_frame = self.frame


    def set_pixel(self, pixel_array, color):
        for x, y in pixel_array:
            self.frame[x, y] = color

    def add_circle(self, pos_x, pos_y, radius, color):
        circ = Circle.Circle(radius=radius, pos_x=pos_x, pos_y=pos_y, color=color)
        self.objects.append(circ)
        self.draw_circle(self.frame)


    def draw_circle(self, frame):
        for elements in self.objects:
            for x, y in elements.current_pixel:
                if self.check_coordinate(x, y):
                    frame[x, y] = elements.COLOR
                    self.last_frame = frame

    def check_coordinate(self, x, y):
        return_elem = True
        if x <= 0 or x >= HEIGHT:
            return_elem = False

        if y <= 0 or y >= WIDTH:
            return_elem = False

        return return_elem


    def move_object(self, obj, new_x=0, new_y=0, erase=False):
        obj.move_circle(new_x=new_x, new_y=new_y)

        for x, y in obj.current_pixel:
            self.frame[x, y] = obj.COLOR

        if(erase):
            for x, y in obj.last_pixel:
                self.frame[x, y] = list(BGCOLOR)

    def save_last_frame(self):
        self.frames.append(self.last_frame)

    def return_saved_array_frames(self):
        return self.frames

    def save_image_as_png(self, path_to_target_dir='null', name="null"):
        path = path_to_target_dir
        pic = self.frame
        pic_name = name

        if pic_name == 'null':
            now = datetime.datetime.now()
            pic_name = now.strftime("%Y_%m_%d_%H_%M_%S")

        if path == 'null':
            img = Image.fromarray(pic)
            img.save(pic_name + ".jpg")
        else:
            if not os.path.exists(path):
                os.mkdir(path)

            abs_path = os.path.join(path, name + '.png')
            img = Image.fromarray(pic)
            img.save(abs_path, 'PNG')

    def save_image_as_csv(self, path_to_target_dir='null', name="null"):
        path = path_to_target_dir
        csv = self.frame
        csv_name = name

        if csv_name == 'null':
            now = datetime.datetime.now()
            csv_name = now.strftime("%Y_%m_%d_%H_%M_%S")

        if path == 'null':
            abs_path = os.path.join(name + '.csv')
            df = pd.DataFrame(csv).transpose()

            df.to_csv(abs_path)
        else:
            if not os.path.exists(path):
                os.mkdir(path)

            abs_path = os.path.join(path, name + '.csv')
            df = pd.DataFrame(csv).transpose()

            df.to_csv(abs_path)



