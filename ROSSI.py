from manim import *

BACKGROUND_CLR = "#010a14"

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

        value = "x"

        input = Tex(f"${value}$")
        input_arrow = Arrow(start=LEFT, end=RIGHT, stroke_width=2, buff=0)
        input.next_to(input_arrow, UP)
        input_group = VGroup(input, input_arrow)
        
        def update_input_values(input_text):
            input_text.become(Tex(f"${value}$")).next_to(input_arrow, UP)
        
        input.add_updater(update_input_values)
        
        output = Tex("$y$")
        output_arrow = Arrow(start=LEFT, end=RIGHT, stroke_width=2, buff=0)
        output.next_to(output_arrow, UP)
        output_group = VGroup(output, output_arrow)
        
        function = Tex(f"$f({value})$")

        function.next_to(black_box, UP)
        input_group.next_to(black_box, LEFT)
        output_group.next_to(black_box, RIGHT)
        function_display = VGroup(black_box, input_group, output_group)

        self.play(Write(h_funzione))
        self.wait(5)
        self.play(AnimationGroup(
            MoveToTarget(h_funzione),
            Create(black_box),
            Create(input_group),
            Create(function),
            lag_ratio=.90))
        
        self.wait(.5)
        self.play(Wiggle(black_box))
        self.wait(.5)
        self.play(Create(output_group))
        value = "5"
        self.wait(5)
        
