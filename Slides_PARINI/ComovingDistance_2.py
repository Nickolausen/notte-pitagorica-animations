from manim import *
from General import *

class ComovingDistance2(Scene):
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

        f_domain = [0, 4]
        hubbles_sphere_1 = classic_plane.plot(lambda x: 1.5 * (((3 * np.log( (np.exp(x) - .1) / ( np.exp(2 * x) + 1 ))) / (x + 1)) + 2.4), x_range=f_domain)
        hubbles_sphere_2 = classic_plane.plot(lambda x: -1.5 * (((3 * np.log( (np.exp(x) - .1) / ( np.exp(2 * x) + 1 ))) / (x + 1)) + 2.4), x_range=f_domain)

        hubbles_sphere = VGroup(hubbles_sphere_1, hubbles_sphere_2)
        hubbles_sphere.rotate(angle=PI/2, about_point=classic_plane.get_origin()).rotate(angle=PI).set_color(TEAL)
        
        hubbles_sphere_label = classic_plane.get_graph_label(graph=hubbles_sphere_1, label="Hubble\ Sphere", color=TEAL)
        hubbles_sphere_label.scale(CST_SCALE_FACTOR).move_to(classic_plane.get_origin()).shift(UP * 2 + RIGHT * .35).rotate(PI/2.5)

        event_horizon = classic_plane.plot(lambda x: -abs(1.5 * x) + 5, x_range=[-3.333, 3.333])
        event_horizon.set_color(BLUE)
        event_horizon_label = classic_plane.get_graph_label(graph=event_horizon, label="event\ horizon", color=BLUE)
        event_horizon_label.scale(CST_SCALE_FACTOR).next_to(event_horizon).shift(LEFT * 2.5).rotate(-(PI/2 - np.arctan(3.3333/5)))

        light_cone = classic_plane.plot(lambda x: -abs(x) + 2, x_range=[-2,2])
        light_cone.set_color(PURPLE)
        light_cone_label = classic_plane.get_graph_label(graph=light_cone, label="light\ cone", color=PURPLE)
        light_cone_label.scale(CST_SCALE_FACTOR).next_to(light_cone).shift(LEFT * 1.60).rotate(-(PI/2 - np.arctan(1)))

        particle_horizon = classic_plane.plot(lambda x: abs(x))
        particle_horizon.set_color(PINK)
        particle_horizon_label = classic_plane.get_graph_label(particle_horizon, "particle\ horizon", color=PINK)
        particle_horizon_label.scale(CST_SCALE_FACTOR).next_to(particle_horizon).shift(UP * 1.5 + LEFT * 2.5).rotate(PI/4)

        now = classic_plane.plot(lambda x: 2, stroke_width=.5)
        now_label = classic_plane.get_graph_label(graph=now, label="now")
        now_label.scale(CST_SCALE_FACTOR)
        ghost_fx_1 = classic_plane.plot(lambda x: 5)

        area1 = classic_plane.get_area(graph=event_horizon, 
            bounded_graph=ghost_fx_1, 
            color=GREEN, 
            opacity=.3, 
            x_range=(-5,5))

        ghost_fx_2 = classic_plane.plot(lambda x: 0)
        area2 = classic_plane.get_area(graph=event_horizon, 
            bounded_graph=ghost_fx_2, 
            color=GREEN, 
            opacity=.3, 
            x_range=(-5,3.333))

        area3 = classic_plane.get_area(graph=event_horizon, 
            bounded_graph=ghost_fx_2, 
            color=GREEN, 
            opacity=.3, 
            x_range=(3.333,5))

        graph_title = Tex("Comoving Distance \#2").scale(2).move_to(classic_plane.get_center() + (3.25 * DOWN))
        
        grn_area = Difference(Difference(area1, area2), area3, color=GREEN)
        grn_area.set_fill(GREEN).set_opacity(.25)

        self.add(classic_plane)
        self.play(AnimationGroup(
            Create(event_horizon),
            Write(event_horizon_label),
            Create(hubbles_sphere),
            Write(hubbles_sphere_label),
            Create(now),
            Write(now_label),
            Create(light_cone),
            Write(light_cone_label),
            Create(DashedVMobject(particle_horizon, dashed_ratio=.3)),
            Write(particle_horizon_label),
            FadeIn(grn_area),
            Write(graph_title),
            lag_ratio=1
        ))