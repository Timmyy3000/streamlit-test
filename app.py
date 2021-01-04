
import streamlit as st
from streamlit_drawable_canvas import st_canvas

canvas_result = st_canvas(
stroke_width = 25,
stroke_color = "#fff",
background_color = "#000",
height = 280,
width = 280,
drawing_mode = "freedraw",
key = "canvas",
)
