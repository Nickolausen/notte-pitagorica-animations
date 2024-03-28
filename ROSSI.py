from manim import *
from General import BACKGROUND_CLR

class Versione1(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_CLR

        h_funzione = Tex(r"$\mathbb{F}$\textsc{unzioni}")
        h_funzione.generate_target()
        
        h_funzione.target.to_corner(UL).shift(DOWN * .25).shift(RIGHT)
        h_funzione.target.scale(1.5)
        h_funzione.move_to(ORIGIN).scale(3)

        black_box = Rectangle(color=WHITE, height=4, width=2)
        black_box.move_to(ORIGIN)
        black_box.set_fill(GRAY)


        f_input = MathTex('x', substrings_to_isolate='x')
        f_input.set_color_by_tex('x', YELLOW)

        f_input_arrow = Arrow(start=LEFT, end=RIGHT, stroke_width=2, buff=0, tip_shape=ArrowTriangleTip)
        f_input.next_to(f_input_arrow, UP)
        f_input_group = VGroup(f_input, f_input_arrow)
        
        f_output = MathTex('y').set_color(GREEN)
        f_output_arrow = Arrow(start=LEFT, end=RIGHT, stroke_width=2, buff=0, tip_shape=ArrowTriangleTip)
        f_output.next_to(f_output_arrow, UP)
        f_output_group = VGroup(f_output, f_output_arrow)
        
        function = MathTex('f(x)', substrings_to_isolate='x')
        function.set_color_by_tex('x', YELLOW)

        function.next_to(black_box, UP)
        f_input_group.next_to(black_box, LEFT)
        f_output_group.next_to(black_box, RIGHT)
        # function_display = VGroup(black_box, input_group, output_group)

        self.play(Write(h_funzione))
        self.wait(5)
        self.play(AnimationGroup(
            MoveToTarget(h_funzione),
            Create(black_box),
            Create(f_input_arrow),
            Write(f_input),
            Write(function),
            lag_ratio=.90))
        
        self.wait(.5)
        self.play(Wiggle(black_box))
        self.wait(.5)
        self.play(Create(f_output_group))
        self.remove(f_input)
        f_input.set(value='5')
        self.wait(3)
        self.play(Write(f_input))
        self.play(Uncreate(function))