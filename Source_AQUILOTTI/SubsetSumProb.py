from manim import *
from random import randint

class SubSetProb(Scene):
    def construct(self):
        title = Title(r"\textsc{Subset Sum Problem}").set_color(BLUE)
        description = Tex(r"Dato un insieme $S = \{a_1, a_2, \dots, a_n\}$ e un valore $T$, determinare \\ se esiste un sottoinsieme di $S$ la cui somma è uguale a $T$.").next_to(title, DOWN).scale(.7)

        es_1 = VGroup()
        t_0 = MathTex(r"T = 0", substrings_to_isolate=["0"])
        t_0.set_color_by_tex("0", TEAL)
        s_0 = MathTex(r"S = \{", r"10", ",", r"-3", ",", r"-2", ",", r"8", "," r"5", "\}").next_to(t_0, RIGHT, 2)

        es_1.add(t_0, s_0)
        es_1.move_to(ORIGIN).shift(UP)

        sol = VGroup()
        solution_numbers = MathTex(r"&-3 -2 + 5", "= 0", substrings_to_isolate=["-3 -2 + 5", "0"])
        solution_numbers.set_color_by_tex("-3 -2 + 5", GREEN)
        solution_numbers.set_color_by_tex("0", TEAL)
        solution = Tex(r"Soluzione $= \{-3, -2, 5\}$")
        solution.next_to(solution_numbers, DOWN)
        
        sol.add(solution_numbers, solution)
        sol.next_to(es_1, DOWN, buff=1)
        
        costi = VGroup()
        test_soluzione = MathTex(r"\text{Verifica della soluzione: } O(n)", substrings_to_isolate=["O(n)"])
        calcolo_soluzione = MathTex(r"\text{Calcolo della soluzione: } O(2^n)", substrings_to_isolate=["O(2^n)"])
        calcolo_soluzione.next_to(test_soluzione, RIGHT, 1.2)
        costi.add(test_soluzione, calcolo_soluzione)
        costi.move_to(ORIGIN).next_to(sol, DOWN, 1).scale(.75)

        self.play(AddTextWordByWord(title))
        self.play(Write(description), run_time=5)
        self.play(Write(t_0))
        self.wait(.5)
        self.play(Write(s_0))

        for i in range(0, 4):
            self.play(Circumscribe(s_0[2 * i + 1]), run_time=1)
        
        self.play(Circumscribe(s_0[8]), run_time=1)
        
        self.play(Create(sol))
        
        self.play(s_0[3].animate.set_color(GREEN))
        self.play(s_0[5].animate.set_color(GREEN))
        self.play(s_0[8].animate.set_color(GREEN))




        self.play(Write(test_soluzione))
        self.play(test_soluzione.animate.set_color_by_tex("O(n)", GREEN))
        
        self.play(Write(calcolo_soluzione))
        self.play(calcolo_soluzione.animate.set_color_by_tex("O(2^n)", RED))