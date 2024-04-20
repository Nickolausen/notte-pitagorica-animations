from manim import *
from General import *

class ProperDistance(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_CLR

        def light_cone_f(x):
            return 1.5 * (((3 * np.log( np.exp(x) / ( np.exp(2 * x) + 1 ))) / (x + 1)) + 2.079)
        
        classic_plane = NumberPlane(
            x_range=[-5, 5, 1], 
            y_range=[0, 5, 1], 
            axis_config={
                "include_numbers": False,
            },
            background_line_style={
                "stroke_opacity": .5,
                "stroke_width": .5
            }
        )

        meeting_point = 2.25
        f_domain = [0, meeting_point]
        first_half = classic_plane.plot(lambda x: light_cone_f(x), x_range=f_domain)
        second_half = classic_plane.plot(lambda x: -light_cone_f(x), x_range=f_domain)

        light_cone = VGroup(first_half, second_half)
        light_cone.set_color(RED).rotate(angle=PI/2, about_point=classic_plane.get_origin())
        light_cone_label = classic_plane.get_graph_label(graph=first_half, label="light\ cone")
        light_cone_label.scale(CST_SCALE_FACTOR).move_to(classic_plane.get_origin()).shift(UP * 1.5 + RIGHT * 0.45).rotate(-PI/2.8)

        now = classic_plane.plot(lambda x: meeting_point)
        now.stroke_width = .5
        now_label = classic_plane.get_graph_label(now, "now")
        now_label.scale(CST_SCALE_FACTOR)
        
        particle_horizon = classic_plane.plot(lambda x: abs(.5 * x), color=PINK)
        particle_horizon_label = classic_plane.get_graph_label(particle_horizon, "particle\ horizon")
        particle_horizon_label.scale(CST_SCALE_FACTOR).move_to(classic_plane.get_origin()).shift(UP * 2.25 + RIGHT * 4).rotate(PI/2 - np.arctan(5/2.5))

        event_horizon = classic_plane.plot(lambda x: .5 * (x**2), x_range=[-3.162,3.162], color=BLUE)
        event_horizon_label = classic_plane.get_graph_label(event_horizon, "event\ horizon")
        event_horizon_label.scale(CST_SCALE_FACTOR).move_to(classic_plane.get_origin()).shift(UP * 4 + LEFT * 3.1).rotate(PI/2 + PI/10)

        hubble_sphere = classic_plane.plot(lambda x: abs(.5*x) + .4 * x**2, x_range=[-2.965,2.965], color=TEAL)
        hubble_sphere_label = classic_plane.get_graph_label(graph=hubble_sphere, label="Hubble\ Sphere")
        hubble_sphere_label.scale(CST_SCALE_FACTOR).move_to(classic_plane.get_origin()).shift(UP * 2 + RIGHT * 1.4).rotate(PI/3)

        ghost_fx = classic_plane.plot(lambda x: 0)
        area = classic_plane.get_area(graph=ghost_fx, bounded_graph=event_horizon, color=GREEN, opacity=.25)
        second_area = classic_plane.get_area(graph=event_horizon, bounded_graph=hubble_sphere, color=YELLOW, opacity=.25)
        
        ghost_fx_2 = classic_plane.plot(lambda x: 5)

        left_area = classic_plane.get_area(graph=ghost_fx, bounded_graph=ghost_fx_2, color=GREEN, opacity=.25, x_range=[-5, -3.162])
        right_area = classic_plane.get_area(graph=ghost_fx, bounded_graph=ghost_fx_2, color=GREEN, opacity=.25, x_range=[3.162, 5])
        total_area = Union(left_area, area, right_area)
        total_area.set_stroke(width=0)
        total_area.set_fill(GREEN, opacity=.25)

        graph_title = Tex("Proper Distance").scale(2).move_to(classic_plane.get_center() + (3.25 * DOWN))

        # graph_elements = VGroup(now, )

        self.play(
            AnimationGroup(
                Create(classic_plane), 
                Create(now),
                Write(now_label),
                Create(event_horizon),
                Write(event_horizon_label),
                Create(hubble_sphere),
                Write(hubble_sphere_label),
                FadeIn(total_area),
                FadeIn(second_area),
                Create(DashedVMobject(particle_horizon)),
                Write(particle_horizon_label),
                Create(light_cone),
                Write(light_cone_label),
                Write(graph_title), 
                lag_ratio=1))
        
        self.wait(4)
        self.play(FadeOut(*self.mobjects))