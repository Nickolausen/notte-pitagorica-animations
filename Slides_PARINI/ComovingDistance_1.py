from manim import *
from General import *

class ComovingDistance1(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_CLR

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

        def event_horizon_f(x):
            return .7629 / (.1 * x ** 2)
        
        def hubble_sphere_f(x):
            return (abs(8.35 * x) ** .944) / np.power(3.8, np.power(x, .6))
        
        first_half_event_horizon = classic_plane.plot(lambda x: event_horizon_f(x), x_range=[-5, -1.235])
        second_half_event_horizon = classic_plane.plot(lambda x: event_horizon_f(x), x_range=[1.235, 5])
        event_horizon = VGroup(first_half_event_horizon, second_half_event_horizon)
        event_horizon.set_color(BLUE)
        event_horizon_label = classic_plane.get_graph_label(first_half_event_horizon, "event\ horizon", color=BLUE)
        event_horizon_label.scale(CST_SCALE_FACTOR).move_to(classic_plane.get_origin()).shift(UP * .7 + LEFT * 4.2).rotate(PI/12)

        first_half_hubble_sphere = classic_plane.plot(lambda x: hubble_sphere_f(x), x_range=[0, 5])
        second_half_hubble_sphere = classic_plane.plot(lambda x: -hubble_sphere_f(x), x_range=[0, 5])

        hubble_sphere = VGroup(first_half_hubble_sphere, second_half_hubble_sphere)
        hubble_sphere.rotate(angle=PI/2, about_point=classic_plane.get_origin()).set_color(TEAL)
        hubble_sphere_label = classic_plane.get_graph_label(first_half_hubble_sphere, "Hubble\ Sphere", color=TEAL)
        hubble_sphere_label.scale(CST_SCALE_FACTOR).move_to(classic_plane.get_origin()).shift(UP * 3 + RIGHT * 1.3).rotate(PI/2 + PI/10).rotate(PI)

        particle_horizon = classic_plane.plot(lambda x: .1 * x**2, color=PINK)
        particle_horizon_label = classic_plane.get_graph_label(particle_horizon, "particle\ horizon", color=PINK)
        particle_horizon_label.scale(CST_SCALE_FACTOR).rotate(PI/4).shift(LEFT * .4 + DOWN * .2)

        light_cone = classic_plane.plot(lambda x: ((1 - np.exp(- abs( 2 * x ))) / abs(x)), color=PURPLE)
        light_cone_label = classic_plane.get_graph_label(light_cone, "light\ cone", color=PURPLE)
        light_cone_label.scale(CST_SCALE_FACTOR).move_to(classic_plane.get_origin()).shift(UP * 1.6 + RIGHT * .6).rotate(-PI/4)

        now = classic_plane.plot(lambda x: 2, stroke_width=.5)
        now_label = classic_plane.get_graph_label(now, "now")
        now_label.scale(CST_SCALE_FACTOR).shift(LEFT * .35)

        ghost_fx = classic_plane.plot(lambda x: 5)

        first_half_area = classic_plane.get_area(graph=first_half_event_horizon, bounded_graph=ghost_fx, opacity=.25)
        second_half_area = classic_plane.get_area(graph=second_half_event_horizon, bounded_graph=ghost_fx, opacity=.25)

        grn_area = VGroup(first_half_area, second_half_area).set_color(GREEN)

        graph_title = Tex("Comoving Distance \#1").scale(2).move_to(classic_plane.get_center() + (3.25 * DOWN))

        self.add(classic_plane)
        self.play(
            AnimationGroup(
                Create(now),
                Write(now_label),
                Create(light_cone),
                Write(light_cone_label),
                Create(hubble_sphere),
                Write(hubble_sphere_label),
                Create(event_horizon),
                Write(event_horizon_label),
                FadeIn(grn_area),
                Create(DashedVMobject(particle_horizon, dashed_ratio=.3)),
                Write(particle_horizon_label),
                Write(graph_title),
                lag_ratio=1
            )
        )