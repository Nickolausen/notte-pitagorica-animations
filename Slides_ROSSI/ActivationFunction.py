from manim import *
from _General import *
from math import *

class ActivationFunction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_CLR
        point_tracker = ValueTracker(2)

        ax = Axes(
            x_range=[-4, 4],
            y_range=[0, 1, .2],
            y_length=5,
            axis_config={
                "include_numbers": True})

        sigmoid_graph = ax.plot(lambda x: sigmoid(x))
        sigmoid_graph.set_color(GREEN)
        
        dot = always_redraw(lambda: Dot(point = ax.c2p(point_tracker.get_value(), sigmoid(point_tracker.get_value()))))
        
        y_projection = always_redraw(lambda: ax.get_vertical_line(point=ax.c2p(point_tracker.get_value(), sigmoid(point_tracker.get_value())), line_func=DashedLine))
        x_projection = always_redraw(lambda: ax.get_horizontal_line(point=ax.c2p(point_tracker.get_value(), sigmoid(point_tracker.get_value())), line_func=DashedLine))

        sigmoid_header = Tex(r"\textsc{Sigmoid}")
        sigmoid_header.shift(UP * 3)

        def draw_label():
            point = ax.c2p(point_tracker.get_value(), sigmoid(point_tracker.get_value()))
            return Text("({:.2f}, {:.2f})".format(point[0], point[1]))

        label = always_redraw(lambda: draw_label().shift(UP * 1.5 + LEFT * 4.5).scale(.5))

        self.play(Write(label), Write(sigmoid_header), Create(ax), Create(sigmoid_graph), Create(dot), Create(y_projection), Create(x_projection))
        self.play(point_tracker.animate.set_value(-2), run_time=4)
        self.wait(2)