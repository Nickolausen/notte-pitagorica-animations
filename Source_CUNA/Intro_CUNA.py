from manim import *
from random import randint, random

class Intro(Scene):
    def construct(self):
        pres_title = Tex(r"\textsc{Emotional Waves}").scale_to_fit_width(self.camera.frame_width - 3)
        subtitle = Tex(r"\textbf{Giuseppe Cuna} \textit{- a.k.a 'azelbeatbox', \\ Human Beatboxer, ex studente @ I.T.T. 'Blaise Pascal'}")
        subtitle.next_to(pres_title, DOWN).scale(.7)

        texts = VGroup(pres_title, subtitle).move_to(ORIGIN)

        circles = VGroup()
        for i in range(0, 9):
            new_circ = Circle(radius=randint(3, 7), color=random_color())
            new_circ.set_x(randint(-int((14 + 2/9) / 2), int((14 + 2/9) / 2)))
            new_circ.set_y(randint(-int(8/2), int(8/2)))
            new_circ.set_opacity(random() % .41).set_stroke(width=0)
            new_circ.scale(random() % 1.1)
            circles.add(new_circ)

        circles.set_z_index(-1)

        self.play(FadeIn(pres_title), run_time=5)
        self.play(AddTextLetterByLetter(subtitle))
        self.play(ApplyWave(pres_title), run_time=3)

        for circle in circles:
            self.play(FadeIn(circle), run_time=randint(3, 5))
        
        directions = [UP, DOWN, LEFT, RIGHT]
        for circle in circles:
            self.play(circle.animate.shift(directions[randint(0, 3)] * randint(1, 3) + directions[randint(0, 3)] * randint(0, 2)), run_time=randint(5, 7))

        self.wait(4)
        self.play(FadeOut(*self.mobjects))
        