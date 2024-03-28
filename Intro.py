from General import BACKGROUND_CLR

from manim import *
from random import randint

class Versione1(Scene):
    def construct(self):
        screen_width = int((14 + 2/9) / 2) 
        screen_height = int(8/2)
        
        self.camera.background_color = BACKGROUND_CLR
        
        # Creazione titolo
        first_word = Tex(r"$\mathbb{O}$\textsc{rizzonti}").scale(3)
        second_word = Tex(r"$\mathbb{P}$\textsc{itagorici}").scale(3)
        second_word.next_to(first_word, DOWN, buff=.2)
        sentence = VGroup(first_word, second_word)
        sentence.move_to(ORIGIN)

        start_index = 0
        end_index = 30
        count = end_index + 1

        # Creazione oggetti - Serie di Fibonacci e Golden Ratio
        squares = VGroup(Square(1 * 0.3))
        next_dir = [RIGHT, UP, LEFT, DOWN]
        FSeq = [1, 2, 3, 5, 8, 13, 21]

        for j, i in enumerate(FSeq):
            d = next_dir[j % 4]
            squares.add(Square(i * 0.3).next_to(squares, d, buff=0))

        squares.center()
        squares.set_stroke(color=GRAY, width=.5)

        direction = [1, -1, -1, 1]
        corner = [[UL, -UL], [UR, -UR]]
        spiral = VGroup()

        for j, i in enumerate(squares):
            c = corner[j % 2]
            d = direction[j % 4]
            arc = ArcBetweenPoints(
                i.get_corner(c[0]),
                i.get_corner(c[1]),
                angle=PI / 2 * d,
                color=GRAY,
                stroke_width=1
            )
            if direction[j % 4] != 1:
                arc = arc.reverse_direction()
            spiral.add(arc)

        # Animazioni
        self.play(
            AnimationGroup(*[Create(square) for square in squares], 
            Create(spiral), 
            lag_ratio=.90)
        )
        self.wait()

        self.play(Write(sentence))
        self.wait(5)
        self.play(Unwrite(sentence))

        self.play(FadeOut(squares), Uncreate(spiral[::-1]), run_time=1.5)
        
        self.wait()