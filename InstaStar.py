from PyRender.pyrender import PyRender
from insta_automation.instand import instand
import time


def main():
    while True :
        p = PyRender()
        i = instand()
        p.run_animation()
        i.automate()
        time.sleep(60 * 10)
        del(p)
        del(i)


if __name__ == '__name__':
    main()