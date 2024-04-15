from manim import *

BACKGROUND_CLR = '#010a14'

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