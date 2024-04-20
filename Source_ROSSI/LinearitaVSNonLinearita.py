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

        linear_relation = VGroup()

        linear_f_header = Tex("Relazione lineare")
        linear_f_header.move_to(ax.get_center()).shift(UP * 3.5)
        linear_f = ax.plot(lambda x: 2*x, x_range=[-3, 3])
        linear_f.set_color(GREEN)
        
        x_tracker = ValueTracker()

        def draw_function_text():
            text = MathTex(f"f({int(x_tracker.get_value())}) = 2\cdot{int(x_tracker.get_value())} = {int(x_tracker.get_value()) * 2}")
            text.next_to(ax, DOWN)
            return text

        function_text = always_redraw(lambda: draw_function_text())
        function_text.add_updater(lambda obj: obj.next_to(ax, DOWN))
        
        linear_relation.add(ax, linear_f, linear_f_header, function_text)

        self.add(linear_relation)
        for i in [1, 2, 3]:
            x_tracker.set_value(i)
            self.wait(1)
        
        self.play(linear_relation.animate.scale(.5))
        self.play(linear_relation.animate.shift(LEFT * 3))