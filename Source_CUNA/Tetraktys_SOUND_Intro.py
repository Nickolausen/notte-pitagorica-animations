from manim import *
from random import randint

WAITING_INTERVAL = .1

class Tetraktys_Sound(Scene):
    def construct(self):
        colors = [MAROON, GREEN, TEAL, ORANGE]
        circles = VGroup()
        
        def flash_triangle():
            self.play(ShowPassingFlash(triangle.copy(), time_width=1), run_time=2)

        for i in range(0, 4):
            layer = VGroup()
            for j in range(0, i + 1):
                new_circ = Circle(color=colors[i])
                new_circ.set_fill(colors[i], opacity=1) 
                layer.add(new_circ)

            layer.arrange_in_grid(rows=1, buff=1)
            circles.add(layer)

        circles.arrange_in_grid(cols=1).move_to(ORIGIN).scale(.5)

        triangle = Polygon(
            circles.get_top(), 
            circles.get_right() + DOWN * 2, 
            circles.get_left() + DOWN * 2).scale(1.35).shift(UP * .35).set_color(MAROON).set_stroke(opacity=.6, width=1.5)
        
        tetraktys = VGroup(circles, triangle).scale(1.1).shift(DOWN * .2)
        
        self.play(GrowFromCenter(tetraktys), run_time=7)
        self.wait(.7)
        flash_triangle()
        self.play(AnimationGroup(*[ApplyWave(circle) for circle in circles], lag_ratio=.5))
        self.wait(.7)
        self.play(FadeOut(circles))

        flash_triangle()
        
        for i in range(0, 8):
            self.play(FadeIn(circles[0][0]), run_time=.1)
            self.wait(WAITING_INTERVAL)
            self.play(FadeOut(circles[0][0]),  run_time=.1)
            self.wait(WAITING_INTERVAL)

        div1 = 2
        for i in range(0, 8):
            self.play(FadeIn(circles[0][0]), run_time=.1)
            self.wait(WAITING_INTERVAL / div1)
            self.play(FadeIn(circles[1][0]), run_time=.1)
            self.wait(WAITING_INTERVAL / div1)
            self.play(FadeOut(circles[0][0]),  run_time=.1)
            self.wait(WAITING_INTERVAL / div1)
            self.play(FadeOut(circles[1][0]), run_time=.1)
            self.wait(WAITING_INTERVAL / div1)

        div2 = 1.8
        for i in range(0, 8):
            self.play(FadeIn(circles[0][0]), run_time=.1)
            self.wait(WAITING_INTERVAL / div2)
            self.play(FadeIn(circles[1][0]), run_time=.1)
            self.wait(WAITING_INTERVAL / div2)
            self.play(FadeIn(circles[1][1]), run_time=.1)
            self.wait(WAITING_INTERVAL / div2)
            self.play(FadeOut(circles[0][0]),  run_time=.1)
            self.wait(WAITING_INTERVAL / div2)
            self.play(FadeOut(circles[1][0]),  run_time=.1)
            self.wait(WAITING_INTERVAL / div2)
            self.play(FadeOut(circles[1][1]),  run_time=.1)
            self.wait(WAITING_INTERVAL / div2)

        div3 = 9
        for i in range(0, 8):
            self.play(FadeIn(circles[0][0]), run_time=.1)
            self.wait(WAITING_INTERVAL * div3)
            self.play(FadeIn(circles[1][0]), run_time=.1)
            self.wait(WAITING_INTERVAL * div3)
            self.play(FadeIn(circles[1][1]), run_time=.1)
            self.wait(WAITING_INTERVAL * div3)
            self.play(FadeIn(circles[2][0]), run_time=.1)
            self.wait(WAITING_INTERVAL * div3)
            self.play(FadeOut(circles[0][0]),  run_time=.1)
            self.wait(WAITING_INTERVAL * div3)
            self.play(FadeOut(circles[1][0]),  run_time=.1)
            self.wait(WAITING_INTERVAL * div3)
            self.play(FadeOut(circles[1][1]),  run_time=.1)
            self.wait(WAITING_INTERVAL * div3)
            self.play(FadeOut(circles[2][0]), run_time=.1)
            self.wait(WAITING_INTERVAL * div3)

        for i in range(0, 8):
            self.play(FadeIn(circles[0][0]), run_time=.1)
            self.wait(WAITING_INTERVAL)
            self.play(FadeIn(circles[1][0]), run_time=.1)
            self.wait(WAITING_INTERVAL)
            self.play(FadeIn(circles[1][1]), run_time=.1)
            self.wait(WAITING_INTERVAL)
            self.play(FadeIn(circles[2][0]), run_time=.1)
            self.wait(WAITING_INTERVAL)
            self.play(FadeIn(circles[2][1]), run_time=.1)
            self.wait(WAITING_INTERVAL)
            self.play(FadeOut(circles[0][0]),  run_time=.1)
            self.wait(WAITING_INTERVAL)
            self.play(FadeOut(circles[1][0]),  run_time=.1)
            self.wait(WAITING_INTERVAL)
            self.play(FadeOut(circles[1][1]),  run_time=.1)
            self.wait(WAITING_INTERVAL)
            self.play(FadeOut(circles[2][0]), run_time=.1)
            self.wait(WAITING_INTERVAL)
            self.play(FadeOut(circles[2][1]), run_time=.1)
            self.wait(WAITING_INTERVAL)

        for i in range(0, 8):
            self.play(FadeIn(circles[0][0]), run_time=.1)
            self.wait(WAITING_INTERVAL)
            self.play(FadeIn(circles[1][0]), run_time=.1)
            self.wait(WAITING_INTERVAL)
            self.play(FadeIn(circles[1][1]), run_time=.1)
            self.wait(WAITING_INTERVAL)
            self.play(FadeIn(circles[2][0]), run_time=.1)
            self.wait(WAITING_INTERVAL)
            self.play(FadeIn(circles[2][1]), run_time=.1)
            self.wait(WAITING_INTERVAL)
            # self.play(
            #     circles[0][0].animate
            # )

        flash_triangle()
        self.wait(1)
        for i in [0, 1, 2, 3]:
            for j in range(0, len([*circles[i]])):
                self.play(FadeIn(circles[i][j]))

        self.play(Wiggle(tetraktys))
        self.wait(1)
        self.play(FadeOut(*self.mobjects), run_time=1)