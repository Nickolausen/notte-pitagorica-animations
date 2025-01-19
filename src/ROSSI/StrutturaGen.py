from manim import *

class Versione1(Scene): 
    def construct(self):
        distance = 3

        # Input layer
        input_layer_heading = Tex("Input layer")
        input_layer = VGroup()
        for i in range(0, 3):
            input_layer.add(Circle(color=RED, radius=.5))

        input_layer.arrange_in_grid(cols=1, buff=.5).shift(LEFT * distance)
        input_layer_heading.move_to(input_layer[0]).shift(UP)

        # Hidden Layer
        hidden_layer_heading = Tex("Hidden layer")
        hidden_layer = VGroup()
        for i in range(0, 4):
            hidden_layer.add(Circle(color=BLUE, radius=.5))

        hidden_layer.arrange_in_grid(cols=1, buff=.5)
        hidden_layer_heading.move_to(hidden_layer[0]).shift(UP)

        # Output layer
        output_layer_heading = Tex("Output layer")
        output_layer = VGroup()
        for i in range(0, 2):
            output_layer.add(Circle(color=GREEN, radius=.5))

        output_layer.arrange_in_grid(cols=1, buff=.5).shift(RIGHT * distance)
        output_layer_heading.move_to(output_layer[0]).shift(UP)

        # Input to Hidden links
        i_to_h_links = VGroup()
        for input_neuron in input_layer:
            for hidden_neuron in hidden_layer:
                link = Line(end=hidden_neuron, start=input_neuron)
                link.set_stroke(width=.7)
                i_to_h_links.add(link)

        # Hidden to Output links
        h_to_o_links = VGroup()
        for hidden_neuron in hidden_layer:
            for out_neuron in output_layer:
                link = Line(start=hidden_neuron, end=out_neuron)
                link.set_stroke(width=.7)
                h_to_o_links.add(link)

        self.play(Write(input_layer_heading))
        self.play(AnimationGroup(*[Create(neuron) for neuron in input_layer], lag_ratio=.7, run_time=.8))
        self.wait(.5)
        self.play(Write(hidden_layer_heading))
        self.play(AnimationGroup(*[Create(neuron) for neuron in hidden_layer], lag_ratio=.7, run_time=1))
        self.wait(.5)
        self.play(Write(output_layer_heading))
        self.play(AnimationGroup(*[Create(neuron) for neuron in output_layer], lag_ratio=.7, run_time=.7))
        self.wait(.5)
        self.play(AnimationGroup(*[Create(link) for link in i_to_h_links],
                                 *[Create(link) for link in h_to_o_links],
                                 lag_ratio=.5,
                                 run_time=3))
        self.wait(5)
        self.play(FadeOut(*self.mobjects))  