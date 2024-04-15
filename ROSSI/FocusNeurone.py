from manim import *
from General import BACKGROUND_CLR
from StrutturaGen import *

class Neurone(Scene):
    def construct(self):
        arrow_length = 4
        self.camera.background_color = BACKGROUND_CLR

        neuron = Circle(color=BLUE)

        left_ghost_neuron = VGroup()
        for i in range(0, 3):
            left_ghost_neuron.add(Circle(radius=0))

        left_ghost_neuron.arrange_in_grid(cols=1, buff=2)
        left_ghost_neuron.shift(LEFT * arrow_length)

        inputs = VGroup()
        for circle in left_ghost_neuron:
            link = Line(start=circle, end=neuron)
            link.stroke_width = .7
            inputs.add(link)

        out_neuron = Circle(radius=0)
        out_neuron.shift(RIGHT * arrow_length)
        output_link = Line(start=neuron, end=out_neuron)
        output_link.stroke_width = .7

        self.add(inputs, neuron, output_link)