from manim import *
from General import *

class ComovingDistance1(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_CLR

        def event_horizon_f(x):
            return 5 / (.3 * x ** 2)
        
        first_half_event_horizon = classic_plane.plot(lambda x: event_horizon_f(x), x_range=[-5, -0.1])
        second_half_event_horizon = classic_plane.plot(lambda x: event_horizon_f(x), x_range=[0.1, 5])
        event_horizon = VGroup(first_half_event_horizon, second_half_event_horizon)
        event_horizon.set_color(BLUE)

        particle_horizon = classic_plane.plot(lambda x: .1 * x**2, color=PINK)
        light_cone = classic_plane.plot(lambda x: ((1 - np.exp(- abs( 2 * x ))) / abs(x)), color=PURPLE)
        now = classic_plane.plot(lambda x: 2, stroke_width=.5)
        ghost_fx = classic_plane.plot(lambda x: 10)

        first_half_area = classic_plane.get_area(graph=first_half_event_horizon, bounded_graph=ghost_fx, opacity=.5)
        second_half_area = classic_plane.get_area(graph=second_half_event_horizon, bounded_graph=ghost_fx, opacity=.5)

        grn_area = VGroup(first_half_area, second_half_area).set_color(GREEN)

        graph_title = Tex("Comoving Distance \#1").scale(2).move_to(classic_plane.get_center() + (3.25 * DOWN))

        self.add(classic_plane)
        self.play(
            AnimationGroup(
                Create(now),
                Create(light_cone),
                Create(event_horizon),
                Create(DashedVMobject(particle_horizon, dashed_ratio=.3)),
                FadeIn(grn_area),
                Write(graph_title),
                lag_ratio=1
            )
        )