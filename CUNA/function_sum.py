from manim import *
from General import *

class FunctionSum(Scene):
    def construct(self):
        _A = ValueTracker(0)
        omega = ValueTracker(0)
        alpha = ValueTracker(0)

        sin = always_redraw(lambda: classic_plane.plot(lambda x: _A.get_value() * np.sin(omega.get_value() * x + alpha.get_value()), color=RED))
        
        cos = always_redraw(lambda: classic_plane.plot(lambda x: _A.get_value() * np.cos(omega.get_value() * x + alpha.get_value()), color=GREEN))

        self.play(AnimationGroup(
            Create(classic_plane),
            Create(sin),
            Create(cos),
            run_time=5
        ))

        for i in range(0, 5):
            self.play(_A.animate.set_value(i ** 2))
            self.play(omega.animate.set_value(i * 2))
            self.play(alpha.animate.set_value(i / 2))
            self.wait(1)