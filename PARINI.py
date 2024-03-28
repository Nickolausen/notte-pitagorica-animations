from manim import *
from manim_presentation import Slide
from General import BACKGROUND_CLR

class Slide1(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_CLR

        plane = Axes(
            x_range=[0, 10, 1], 
            y_range=[0, 10, 1], 
            tips=True,
            axis_config={
                "tip_shape": StealthTip,
                "include_numbers": True
            }
        )

        graph1 = plane.plot(lambda x: 1.5 * (((3 * np.log( np.exp(x) / ( np.exp(2 * x) + 1 ))) / (x + 1)) + 2.079), x_range=[0, 4*PI])
        graph1.set_color(YELLOW)

        graph2 = plane.plot(lambda x: -1.5 * (((3 * np.log( np.exp(x) / ( np.exp(2 * x) + 1 ))) / (x + 1)) + 2.079), x_range=[0, 4*PI])
        graph2.set_color(RED)

        self.play(
            AnimationGroup(
                Create(plane), 
                Create(graph1),
                Create(graph2), 
                run_time=5, 
                lag_ratio=.8))

        self.pause()