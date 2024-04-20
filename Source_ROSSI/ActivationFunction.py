from manim import *
from math import *

class ActivationFunction(Scene):
    def construct(self):
        point_tracker = ValueTracker(2)

        ax = Axes(
            x_range=[-4, 4, .67],
            y_range=[0, 1, .2],
            y_length=5)
        
        ax.shift(DOWN * .5)

        axes_label = ax.get_axis_labels(
            Tex("x").scale(0.7), Tex("y").scale(0.7)
        )

        sigmoid_graph = ax.plot(lambda x: sigmoid(x))
        sigmoid_graph.set_color(RED)
        
        dot = always_redraw(lambda: Dot(point = ax.c2p(point_tracker.get_value(), sigmoid(point_tracker.get_value()))))
        
        y_projection = always_redraw(lambda: ax.get_vertical_line(point=ax.c2p(point_tracker.get_value(), sigmoid(point_tracker.get_value())), line_func=DashedLine))
        x_projection = always_redraw(lambda: ax.get_horizontal_line(point=ax.c2p(point_tracker.get_value(), sigmoid(point_tracker.get_value())), line_func=DashedLine))

        sigmoid_header = Tex(r"\textsc{Sigmoid}")
        sigmoid_header.shift(UP * 3).set_color(RED)

        def draw_label():
            point = ax.p2c(point=[point_tracker.get_value(), sigmoid(point_tracker.get_value()), 0])
            return Text("P = ({:.2f}, {:.2f})".format(point[0], point[1]))

        label = always_redraw(lambda: draw_label().scale(.4))
        
        def label_updater(obj):
            obj.next_to(dot, UL)

        label.add_updater(label_updater)

        my_tex_template = TexTemplate()
        my_tex_template.add_to_preamble(r"\usepackage{amsmath}")
        
        text_label = MathTex(r"P = (neurone,\ f(neurone))", 
                             substrings_to_isolate = ["neurone", "f"], 
                             tex_template = my_tex_template)
        
        text_label.set_color_by_tex("neurone", GREEN)
        text_label.set_color_by_tex("f", RED)
        text_label.set_color_by_tex("output", BLUE)
        text_label.shift(LEFT * 4.5 + UP).scale(.7)

        self.play(Write(label), 
                  Write(text_label), 
                  Write(sigmoid_header), 
                  Create(ax), 
                  Write(axes_label), 
                  Create(sigmoid_graph), 
                  Create(dot), 
                  Create(y_projection), 
                  Create(x_projection))
        
        self.play(point_tracker.animate.set_value(-2), run_time=7)
        self.play(label.animate.next_to(dot, UL))
        self.wait(5)
        self.play(Unwrite(label), 
                  RemoveTextLetterByLetter(text_label), 
                  Unwrite(sigmoid_header), 
                  Uncreate(ax), 
                  Unwrite(axes_label), 
                  Uncreate(sigmoid_graph), 
                  Uncreate(dot), 
                  Uncreate(y_projection), 
                  Uncreate(x_projection))