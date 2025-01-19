from manim import *
from random import randint, random
import cv2

class Intro(Scene):
    def construct(self):
        pres_title = Tex(r"\textsc{One Million Dollar Bees}").scale_to_fit_width(self.camera.frame_width - 3)
        subtitle = Tex(r"\textbf{Eric Aquilotti} \textit{- studente di Ingegneria e Scienze Informatiche\\ @ Università di Bologna}")
        subtitle.next_to(pres_title, DOWN).scale(.7)

        texts = VGroup(pres_title, subtitle).move_to(ORIGIN)
        cap = cv2.VideoCapture("api_background.mp4")
        flag = True
        frame_imgs = []

        while flag:
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame)
                frame_img.fade(.4).set_z_index(-1)
                frame_imgs.append(frame_img)
        cap.release()

        for i in [0, 1, 3, 4, 5, 6, 7, 8]:
            for frame_img in frame_imgs:
                self.add(frame_img)
                self.wait(0.04)
                self.remove(frame_img)
                if texts not in self.mobjects:
                    self.add(texts)