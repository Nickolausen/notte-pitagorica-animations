from manim import *
from General import *

class ProperDistance(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_CLR

        meeting_point = 2.25
        f_domain = [0, meeting_point]
        first_half = classic_plane.plot(lambda x: 1.5 * (((3 * np.log( np.exp(x) / ( np.exp(2 * x) + 1 ))) / (x + 1)) + 2.079), x_range=f_domain)
        second_half = classic_plane.plot(lambda x: -1.5 * (((3 * np.log( np.exp(x) / ( np.exp(2 * x) + 1 ))) / (x + 1)) + 2.079), x_range=f_domain)

        light_cone = VGroup(first_half, second_half)
        light_cone.set_color(RED).rotate(angle=PI/2, about_point=classic_plane.get_origin())

        now = classic_plane.plot(lambda x: meeting_point)
        now.stroke_width = .5
        
        particle_horizon = classic_plane.plot(lambda x: abs(.5 * x), color=PINK)
        event_horizon = classic_plane.plot(lambda x: .5 * (x**2), color=BLUE)
        
        hubble_sphere = classic_plane.plot(lambda x: abs(x) + .3 * x**2, color=TEAL)
        hubble_sphere.stroke_width = .8

        ghost_fx = classic_plane.plot(lambda x: 0)
        area = classic_plane.get_area(graph=ghost_fx, bounded_graph=event_horizon, color=GREEN, opacity=.5)
        second_area = classic_plane.get_area(graph=event_horizon, bounded_graph=hubble_sphere, color=YELLOW, opacity=.5)
        
        graph_title = Tex("Proper Distance").scale(2).move_to(classic_plane.get_center() + (3.25 * DOWN))

        self.play(
            AnimationGroup(
                Create(classic_plane), 
                Create(now),
                Create(event_horizon),
                Create(hubble_sphere),
                FadeIn(area),
                FadeIn(second_area),
                Create(DashedVMobject(particle_horizon)),
                Create(light_cone),
                Write(graph_title),
                run_time=13, 
                lag_ratio=1))
        
        self.wait(4)
        self.play(FadeOut(*self.mobjects))