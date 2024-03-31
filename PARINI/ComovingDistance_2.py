from manim import *
from General import *

class ComovingDistance2(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_CLR

        f_domain = [0, 4]
        hubbles_sphere_1 = classic_plane.plot(lambda x: 1.5 * (((3 * np.log( (np.exp(x) - .1) / ( np.exp(2 * x) + 1 ))) / (x + 1)) + 2.4), x_range=f_domain)
        hubbles_sphere_2 = classic_plane.plot(lambda x: -1.5 * (((3 * np.log( (np.exp(x) - .1) / ( np.exp(2 * x) + 1 ))) / (x + 1)) + 2.4), x_range=f_domain)

        hubbles_sphere = VGroup(hubbles_sphere_1, hubbles_sphere_2)
        hubbles_sphere.rotate(angle=PI/2, about_point=classic_plane.get_origin()).rotate(angle=PI).set_color(TEAL)

        event_horizon = classic_plane.plot(lambda x: -abs(1.5 * x) + 5, x_range=[-3.333, 3.333])
        event_horizon.set_color(BLUE)

        light_cone = classic_plane.plot(lambda x: -abs(x) + 2, x_range=[-2,2])
        light_cone.set_color(PURPLE)

        particle_horizon = classic_plane.plot(lambda x: abs(x))
        particle_horizon.set_color(PINK)

        now = classic_plane.plot(lambda x: 2, stroke_width=.5)
        ghost_fx_1 = classic_plane.plot(lambda x: 5)

        # area1 = classic_plane.get_area(graph=event_horizon, 
        #     bounded_graph=ghost_fx_1, 
        #     color=GREEN, 
        #     opacity=.3, 
        #     x_range=(-5,5))

        graph_title = Tex("Comoving Distance \#2").scale(2).move_to(classic_plane.get_center() + (3.25 * DOWN))
        
        self.add(classic_plane)
        self.play(AnimationGroup(
            Create(event_horizon),
            Create(hubbles_sphere),
            Create(now),
            Create(light_cone),
            Create(DashedVMobject(particle_horizon, dashed_ratio=.3)),
            Write(graph_title),
            run_time=12,
            lag_ratio=1
        ))