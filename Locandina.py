from manim import *
from General import BACKGROUND_CLR

class Volantino(Scene):
    def construct(self):

        self.camera.background_color = BACKGROUND_CLR
        
        # bgr = ImageMobject("bgr_notte_pitagorica.jpg")
        # bgr.scale(2).shift(UP * 3)
        # self.add(bgr)

        title = Tex(r"$\mathbb{N}\textsc{otte}$\\$\mathbb{P}\textsc{itagorica}$")
        address = Tex(r"Viale Cino Macrelli 100,\\Aula Magna Istituto '\textsc{Blaise Pascal}'")
        title.scale(5)
        address.scale(1.5).shift(DOWN * 3.5)

        self.add(title, address)