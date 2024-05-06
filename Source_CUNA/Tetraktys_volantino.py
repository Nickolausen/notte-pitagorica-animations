from manim import *

class Tetraktys_VOLANTINO(Scene):
    def construct(self):
        self.camera.background_color = "#17395D"
        colors = [MAROON, GREEN, TEAL, ORANGE]
        circles = VGroup()

        for i in range(0, 4):
            layer = VGroup()
            for j in range(0, i + 1):
                new_circ = Circle(color=colors[i])
                new_circ.set_fill(colors[i], opacity=1) 
                layer.add(new_circ)

            layer.arrange_in_grid(rows=1, buff=1)
            circles.add(layer)

        circles.arrange_in_grid(cols=1).move_to(ORIGIN).scale(.5)

        triangle = Polygon(
            circles.get_top(), 
            circles.get_right() + DOWN * 2, 
            circles.get_left() + DOWN * 2).scale(1.35).shift(UP * .2).set_color(MAROON).set_stroke(opacity=.6, width=25)
        
        tetraktys = VGroup(circles, triangle).scale(1.1).shift(DOWN * .2)
        writing = Tex(r"\textsc{Tetraktys}").scale(4.5).next_to(tetraktys, DOWN, 1)
        objects = VGroup(tetraktys, writing).move_to(ORIGIN)
        
        self.add(objects)