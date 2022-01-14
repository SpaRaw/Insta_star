import math
import os

import cv2

def generate_animation(list, frameRate, out_put_destination="C:/Users/Korbinian/Desktop/Git_official/Insta_star/PyRender"):
    frameSize = (600, 600)

    out = cv2.VideoWriter(out_put_destination + "/" + 'post.mp4', cv2.VideoWriter_fourcc(*'H264'), frameRate, frameSize)
    n = 0
    for i in list:
        print("%i %i" % (n, len(list)))
        img = cv2.imread(i)
        out.write(img)
        n +=1

    out.release()

def rescale_input(target_amount, path="C:/Users/Korbinian/Desktop/Git_official/Insta_star/PyRender/temp_animation/frames"):
    """
    :param target_amount: Die Gewünschte Anzahl an Frame
    :param return: Eine Liste mit den Namen der Benätigten Frames um die Anzhal auf die Gewünschte Menge zu Skalieren

        Es werden zunächst die Anzahl an vorhandenen Frames Herausgefunden. Dannach wird ein Vielfaches von der Anzahl an Frames und der Gewünschten Anzahl an Frames bestimmt.
        Das erste und letzte Frame stehte Fest.
        Die Schleife durchlauft Die Anzahl an Frames Anzahl Frames * Gewünschte Anzahl mit der Schrittweite der Aktuellen Anzahl an Frames
        Daraufhin wird die Aktuelle Frame nummer durch die Gewünshe ANzahl geteil und auf eine Ganze Zahl gerundet

    """
    return_list = []
    l = len(os.listdir(path))
    t = target_amount
    return_list.append(0)
    for i in range(0 + l, l * t - l - 2, l - 2):
        return_list.append(int(i / t))

    return_list.append(l)
    return return_list


def load_required_files(list, path="C:/Users/Korbinian/Desktop/Git_official/Insta_star/PyRender/temp_animation/frames"):

    """erstellt eine Lilste mit Den zu Ladenden Frames"""
    elements = []

    for element in list:
        elements.append(path + "/" + str(element) + ".png")

    return elements

def animation(target_fps, targe_length, path_to_destination):
    generate_animation(list=load_required_files(rescale_input(target_fps * targe_length)), frameRate=target_fps, out_put_destination=path_to_destination)