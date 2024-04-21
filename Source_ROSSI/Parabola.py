from manim import *

class Parabola(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 8],
            y_range=[0, 8],
            axis_config={
                "include_numbers": True
            })

        def net_function(x):
            return (x - 4) ** 2

        ax.get_x_axis().numbers[3].set_color(YELLOW)

        parabola = ax.plot(lambda x: net_function(x), x_range=[1.25, 6.75])
        parabola.set_color(RED)
        

        parabola_label_text = MathTex("f(x) = (x - 4)^2", substrings_to_isolate=["4"])
        parabola_label = ax.get_graph_label(parabola, parabola_label_text)
        parabola_label_text.set_color_by_tex("4", YELLOW)
        parabola_label.shift(DOWN * 5)

        net_guess_tracker = ValueTracker(1.5)

        net_guess = always_redraw(lambda: Dot(point=ax.c2p(net_guess_tracker.get_value(), net_function(net_guess_tracker.get_value())), color=BLUE))
        y_projection = always_redraw(lambda: ax.get_vertical_line(point=ax.c2p(net_guess_tracker.get_value(), net_function(net_guess_tracker.get_value())), line_func=DashedLine, color=TEAL))
        x_projection = always_redraw(lambda: ax.get_horizontal_line(point=ax.c2p(net_guess_tracker.get_value(), net_function(net_guess_tracker.get_value())), line_func=DashedLine, color=TEAL))
    
        objs = VGroup(ax, parabola, parabola_label, net_guess, y_projection, x_projection)
        objs.shift(UP * .7).scale(.8)

        def draw_label():
            point = [net_guess_tracker.get_value(), net_function(net_guess_tracker.get_value())]
            return Text("({:.2f}, {:.2f})".format(point[0], point[1]))

        dot_label = always_redraw(lambda: draw_label().scale(.5))
        dot_label.add_updater(lambda obj: obj.next_to(net_guess, UR))

        attempts_tracker = ValueTracker(1)
        attempts_label = always_redraw(lambda: 
            Tex(r"Tentativo \#${:d}$".format(int(attempts_tracker.get_value()))).shift(DOWN * 3)
        )

        self.play(
            Create(ax),
            Create(parabola),
            Write(parabola_label),
            Create(net_guess),
            Create(y_projection),
            Create(x_projection),
            Write(dot_label),
            Write(attempts_label)
        )

        idx = 1
        for i in [2, 2.5, 3, 3.5, 5, 4.5, 4]:
            self.wait(.7)
            self.play(attempts_tracker.animate.set_value(idx))
            self.wait(.3)
            self.play(net_guess_tracker.animate.set_value(i))
            idx += 1

        self.play(Flash(net_guess, flash_radius=.3), net_guess.animate.set_color(YELLOW), run_time=2)

        self.wait(6)
        self.play(FadeOut(*self.mobjects))
        self.wait(1)