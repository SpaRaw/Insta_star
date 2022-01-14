import cv2

def generate_animation(list, frameRate, out_put_destination="C:/Users/Korbinian/Desktop/Git_official/Insta_star/alt"):

    """
    :param list: Eine Liste mit Namen der Einzelnen Bilder
    :param frameRate: Die Angepeilte frmaerate für das Video
    :param out_put_destination: Pfad an dem der Output gespeichrt werden soll
    """
    frameSize = (1080, 1350)

    out = cv2.VideoWriter(out_put_destination + "/" + 'post.mp4', cv2.VideoWriter_fourcc(*'mp4v'), frameRate, frameSize)
    n = 0
    for i in list:
        print("%i %i" % (n, len(list)))
        img = cv2.imread(i)
        out.write(img)
        n +=1

    out.release()