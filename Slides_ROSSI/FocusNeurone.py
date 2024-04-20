from manim import *
from _General import BACKGROUND_CLR
from StrutturaGen import *

class Neurone(Scene):
    def construct(self):
        arrow_length = 4
        self.camera.background_color = BACKGROUND_CLR

        neuron_circle = Circle(color=GREEN)

        left_ghost_neuron = VGroup()
        for i in range(0, 3):
            left_ghost_neuron.add(Circle(radius=0))

        left_ghost_neuron.arrange_in_grid(cols=1, buff=2)
        left_ghost_neuron.shift(LEFT * arrow_length)

        inputs_link = VGroup()
        inputs_text = VGroup()
        for idx, circle in enumerate(left_ghost_neuron):
            link = LabeledLine(start=circle, end=neuron_circle, label="w_{}".format(idx+1), font_size=DEFAULT_FONT_SIZE*.7, label_color=ORANGE)
            link.stroke_width = .7
            inputs_link.add(link)
            
            input_text = Tex("$input_{}$".format(idx+1))
            input_text.move_to(circle.get_center()).scale(.7).shift(LEFT * .7)
            inputs_text.add(input_text)

        out_neuron_circle = Circle()
        out_neuron_circle.shift(RIGHT * arrow_length)
        output_link = Line(start=neuron_circle, end=out_neuron_circle)
        output_link.stroke_width = .7

        neuron_text = MathTex("neurone")
        neuron_text.scale(.75).move_to(neuron_circle.get_center()).set_color(GREEN)

        output_text = MathTex("output")
        output_text.scale(.75).set_color(TEAL).move_to(out_neuron_circle.get_center())
        neuron = VGroup(neuron_text, neuron_circle)

        neuron_formula = VGroup()
        txt = MathTex("neurone =", substrings_to_isolate=["neurone"])
        txt.set_color_by_tex("neurone", color=GREEN)
        neuron_formula.add(txt)
        
        for i in [1, 2, 3]:
            math_string = r"input_{} \times w_{}\ +".format(i, i)
            if (i == 3):
                math_string += r"\dots"
            
            to_add = MathTex(math_string, substrings_to_isolate=["w_{}".format(i)])
            to_add.set_color_by_tex("w_{}".format(i), color=ORANGE)

            neuron_formula.add(to_add)
            neuron_formula[i].next_to(neuron_formula[i - 1])
            neuron_formula.move_to(ORIGIN)
        
        neuron_formula.shift(DOWN * 3).scale(.75)
        
        self.play(Create(neuron_circle), Write(neuron_text), run_time=1.5)
        self.play(Write(neuron_formula[0]))
        for i in [1, 2, 3]:
            self.play(Write(inputs_text[i - 1]), Create(inputs_link[i - 1]))
            self.play(Write(neuron_formula[i]))
            self.wait(.3)

        self.play(Create(output_link), Write(output_text))
        
        output_formula = MathTex("output = f(neurone)", substrings_to_isolate=["output", "neurone"])
        output_formula.move_to(neuron_formula)
        output_formula.set_color_by_tex("output", TEAL)
        output_formula.set_color_by_tex("neurone", GREEN)

        self.wait(5)
        self.play(FadeOut(neuron_formula))
        self.wait()
        self.play(Write(output_formula))
        self.wait(5)