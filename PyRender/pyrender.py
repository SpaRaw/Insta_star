from PyRender.python_files import spiro_animation
from PyRender.python_files import frame_manipulation
import os


class PyRender:
    def __init__(self):
        self.spiro = spiro_animation.SpiroAnimation()

    def run_animation(self):

        """Führt alle nätigen Funktionen aus um die Animation zu Erstellen"""
        self.generate_png()
        self.generate_animation()
        self.clear_dir()

    def run_picture(self):
        self.generate_png()
        self.clear_dir()

    def generate_png(self, path_to_frames=r'\PyRender\temp_animation\frames'):

        """Jeder Frame der Animation wird  berechnet, erstellt und anschließend in einem Directory zwischen gespeichert"""
        path = os.getcwd()
        print(path)
        path += path_to_frames
        self.spiro.generate_picture_of_frames(path=path)

    def generate_animation(self, target_fps=30, target_length=30, path_to_destination="/user/contend/post"):

        """Läd alle Frames und fügt diese zu einem Mp4 Datei zusammen"""
        path = os.getcwd()
        path += path_to_destination
        frame_manipulation.animation(target_fps=target_fps, targe_length=target_length, path_to_destination=path)

    def clear_dir(self, path_to_dir='/PyRender/temp_animation/frames/'):

        """Löscht alle nun nicht mehr benötigten Daten"""
        path = os.getcwd()
        path += path_to_dir
        for element in os.listdir(path):
            if element.endswith(".png"):
                os.unlink(path + element)


