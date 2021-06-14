from moviepy.editor import *

clip = (VideoFileClip("frozen_trailer.mp4")
        .subclip((0,1),(0,5))
        .resize(0.3))
clip.write_gif("use_your_head3.gif")
