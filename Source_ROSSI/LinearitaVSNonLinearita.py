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
        ax.shift(DOWN * .5)

        linear_relation = VGroup()

        linear_f_header = Tex("Relazione lineare")
        linear_f_header.move_to(ax.get_center()).shift(UP * 4).scale(1.5)
        linear_f = ax.plot(lambda x: 2*x, x_range=[-2.5, 2.5])
        linear_f.set_color(GREEN)
        linear_f_label = ax.get_graph_label(linear_f, "f(x) = 2x")
        linear_f_label.rotate(linear_f)
        x_tracker = ValueTracker()

        def draw_function_text():
            text = MathTex(f"f({int(x_tracker.get_value())}) = 2\cdot({int(x_tracker.get_value())}) = {int(x_tracker.get_value()) * 2}",
                substrings_to_isolate=[f"{int(x_tracker.get_value())}"])
            text.set_color_by_tex(f"{int(x_tracker.get_value())}", GREEN)
            return text

        function_text = always_redraw(lambda: draw_function_text().next_to(ax, DR + UP * 1.5))
        function_text.add_updater(lambda obj: obj.next_to(ax, DR + UP * 1.5))
        
        linear_relation.add(ax, linear_f, linear_f_header, linear_f_label, function_text)

        self.add(linear_relation)
        vals = [1, 2, 3]
        for i in range(0, 3):
            self.play(x_tracker.animate.set_value(vals[i]))
            self.wait(.5)
        
        self.play(linear_relation.animate.scale(.5))
        self.play(linear_relation.animate.shift(LEFT * 3))

        non_linear_relation = ImageMobject("SleepingHoursGraph.jpg")
        self.add(non_linear_relation)
        self.wait()