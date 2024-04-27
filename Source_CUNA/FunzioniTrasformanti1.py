from manim import *
from Funzione import *
from random import randint
from math import floor

class FunzioniTrasformanti(Scene):
    def construct(self):

        # Ampiezza
        A1, A2 = ValueTracker(1), ValueTracker(1)
        
        # Pulsazione
        omega1, omega2 = ValueTracker(1), ValueTracker(2)
        
        # Costante di fase
        phi1, phi2 = ValueTracker(), ValueTracker()

        sum_display = Axes(
            x_range=[0, 10],
            y_range=[-5, 5]
        ).add_coordinates()
        
        ax1 = Axes(
            x_range=[0, 10],
            y_range=[-5, 5]
        ).add_coordinates()

        ax2 = Axes(
            x_range=[0, 10],
            y_range=[-5, 5]
        ).add_coordinates()

        total = Axes(
            x_range=[0, 10],
            y_range=[-5, 5]
        ).add_coordinates()

        total.shift(RIGHT * 3.5).scale(.5)

        input_group = VGroup(ax1, ax2).arrange_in_grid(cols=1, buff=1)
        axes_group = VGroup(input_group, sum_display).arrange_in_grid(cols=1, buff=2).scale(.3).shift(LEFT * 2)

        def cos_parametrico(x):
            return A1.get_value() * np.cos(omega1.get_value() * x + phi1.get_value())

        def sin_parametrico(x):
            return A2.get_value() * np.sin(omega2.get_value() * x + phi2.get_value())

        fcos = always_redraw(lambda: ax1.plot(lambda x: cos_parametrico(x)).set_color(RED))
        fcos_label = MathTex(r"y_1 = A_1\cos(\omega_1 x + \phi_1)").scale(.5).set_color(RED).next_to(ax1, LEFT, .3)

        fsin = always_redraw(lambda: ax2.plot(lambda x: sin_parametrico(x)).set_color(GREEN))
        fsin_label = MathTex(r"y_2 = A_2\sin(\omega_2 x + \phi_2)").scale(.5).set_color(GREEN).next_to(ax2, LEFT, .3)
        
        f_sum = always_redraw(lambda: sum_display.plot(lambda x: cos_parametrico(x) + sin_parametrico(x)).set_color(BLUE))
        fsum_label = MathTex(r"y_3 = y_1 + y_2").scale(.5).set_color(BLUE).next_to(sum_display, LEFT, .3)

        right_fcos = always_redraw(lambda: total.plot(lambda x: cos_parametrico(x)).set_color(RED))
        right_fsin = always_redraw(lambda: total.plot(lambda x: sin_parametrico(x)).set_color(GREEN))
        right_f_sum = always_redraw(lambda: total.plot(lambda x: cos_parametrico(x) + sin_parametrico(x)).set_color(BLUE))

        t1 = MathTex(r"A_1 = ").set_color(RED)
        t2 = MathTex(r"\quad A_2 = ").set_color(GREEN)
        t3 = MathTex(r"\quad \omega_1 = ").set_color(RED)
        t4 = MathTex(r"\quad \omega_2 = ").set_color(GREEN)
        t5 = MathTex(r"\quad \phi_1 = ").set_color(RED)
        t6 = MathTex(r"\quad \phi_2 = ").set_color(GREEN)

        CST_SCALE_FACTOR = .7
        values_label = VGroup(
            t1, 
            always_redraw(lambda: Text("{:.1f}".format(A1.get_value())).next_to(t1, buff=.1).scale(CST_SCALE_FACTOR).set_color(RED)),
            t2, 
            always_redraw(lambda: Text("{:.1f}".format(A2.get_value())).next_to(t2, buff=.1).scale(CST_SCALE_FACTOR).set_color(GREEN)),
            t3, 
            always_redraw(lambda: Text("{:.1f}".format(omega1.get_value())).next_to(t3, buff=.1).scale(CST_SCALE_FACTOR).set_color(RED)),
            t4, 
            always_redraw(lambda: Text("{:.1f}".format(omega2.get_value())).next_to(t4, buff=.1).scale(CST_SCALE_FACTOR).set_color(GREEN)),
            t5, 
            always_redraw(lambda: Text("{:.1f}".format(phi1.get_value())).next_to(t5, buff=.1).scale(CST_SCALE_FACTOR).set_color(RED)),
            t6,
            always_redraw(lambda: Text("{:.1f}".format(phi2.get_value())).next_to(t6, buff=.1).scale(CST_SCALE_FACTOR).set_color(GREEN))
        ).arrange_in_grid(rows=3, buff=.5).next_to(right_f_sum, DOWN, .8).scale(CST_SCALE_FACTOR)

        self.add(axes_group, fcos, fsin, f_sum, total, right_fcos, right_fsin, right_f_sum, fcos_label, fsin_label, fsum_label, values_label)

        min = 1
        max = 10

        self.play(omega2.animate.set_value(omega1.get_value()))

        for i in range(min, max):
            self.play(phi1.animate.set_value(i * 2))

        rand_numbers = [randint(min, max) for i in range(0, 4)]

        self.play(phi1.animate.set_value(phi1.get_value() + PI/2))

        for i in range(min, max * 2):
            if i % 2 == 0:
                self.play(omega1.animate.set_value(((omega2.get_value() + (i - .4 * i)) % 3) + 1))
            else:
                self.play(omega2.animate.set_value(((omega1.get_value() + (i - .4 * i)) % 3) + 1))
            
            if i in rand_numbers:
                if i % 2 == 0: self.play(A1.animate.set_value(((A1.get_value() + i) % 3) + 1))
                else: self.play(A2.animate.set_value(((A2.get_value() + i) % 3) + 1))

            prev_value = phi1.get_value()
            self.play(phi1.animate.set_value((i * 2) % 4), phi2.animate.set_value(prev_value))

        