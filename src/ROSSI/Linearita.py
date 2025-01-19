from manim import *

class LinVSNonLin(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            axis_config={
                "include_numbers": True
            }
        )

        def double(x):
            return 2 * x
        
        linear_relation = VGroup()

        linear_f_header = Tex("Relazione lineare")
        linear_f_header.move_to(ax.get_center()).shift(UP * 4).scale(1.5)
        linear_f = ax.plot(lambda x: double(x), x_range=[-2.5, 2.5])
        linear_f.set_color(GREEN)
        linear_f_label = ax.get_graph_label(linear_f, "f(x) = 2x")

        x_tracker = ValueTracker(-1)

        def draw_function_text():
            all_together = VGroup()

            text = MathTex(f"f({int(x_tracker.get_value())}) = 2\cdot({int(x_tracker.get_value())})",
                substrings_to_isolate=[f"{int(x_tracker.get_value())}", f"{double(int(x_tracker.get_value()))}"])
            text.set_color_by_tex(f"{int(x_tracker.get_value())}", GREEN)
            
            result = MathTex(f"= {double(int(x_tracker.get_value()))}", 
                substrings_to_isolate=[f"{double(int(x_tracker.get_value()))}"])
            result.set_color_by_tex(f"{double(int(x_tracker.get_value()))}", RED)
            result.next_to(text, direction=RIGHT)

            all_together.add(text, result)
            return all_together

        function_text = always_redraw(lambda: draw_function_text().move_to(ax).shift(DOWN * 2 + RIGHT * 3))
        function_text.add_updater(lambda obj: obj.move_to(ax).shift(DOWN * 2 + RIGHT * 3))
        linear_f_label.move_to(function_text)
        
        self.play(Create(ax), Write(linear_f_label))
        self.play(Create(linear_f), run_time=3)
        self.wait(3)
        self.play(Transform(
            linear_f_label, 
            function_text, 
            replace_mobject_with_target_in_scene=True))
        self.wait(.5)
        for i in [-1, 1, 2]:
            self.play(x_tracker.animate.set_value(i))
            self.play(Create(ax.get_vertical_line(point=ax.c2p(int(x_tracker.get_value()), double(int(x_tracker.get_value()))), line_func=DashedLine)))
            self.play(Create(ax.get_horizontal_line(point=ax.c2p(int(x_tracker.get_value()), double(int(x_tracker.get_value()))), line_func=DashedLine, color=RED)))
            self.play(Create(Dot(point=ax.c2p(int(x_tracker.get_value()), double(int(x_tracker.get_value()))))), FocusOn(Dot(point=ax.c2p(int(x_tracker.get_value()), double(int(x_tracker.get_value()))))))
            self.wait(2)

        self.play(FadeOut(*self.mobjects))