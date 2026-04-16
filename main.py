import streamlit as s
from api_caller import note_generator
from PIL import Image
import api_caller as ap
s.title("Note Summary and Quiz Generator",anchor=False)
s.markdown("Upload **at most 3 images** to generate summary and quizzes")
s.divider()

with s.sidebar:
    s.header("Controls")
    images = s.file_uploader("Upload the photos of your notes", ['jpeg','png','jpg'], accept_multiple_files=True)
    if images:
        cols = s.columns(len(images))
        for i, par_image in enumerate(images):
            with cols[i]:
                s.image(par_image)
    option = s.selectbox("Enter the difficulty of Quiz", ('easy','medium','hard'), index=0)
    pressed = s.button("Click me to instantiate", type="primary")
if pressed:
    if not images:
        s.error("Upload your images")
    if not option:
        s.error("Enter the difficulty of Quiz") 
    if images and option: 
        if len(images) > 3:
            s.warning("you uploaded more than 3")
        else:
            pill_image=[]
            for i in images:
                    pill_image.append(Image.open(i))
            generated_note=ap.note_generator(pill_image, ap.generate_prompt(pill_image,0,option))
            with s.container(border=True):
                s.header("Your notes")
                with s.spinner("AI is writting for you"):
                    s.markdown(generated_note)
            with s.container(border=True):
                with s.spinner("AI is writting for you"):
                    audio_text = generated_note.replace('**', '').replace('*', '').replace('__', '').replace('_', '').replace('#', '').replace('`', '').strip()
                    s.audio(ap.generate_audio(audio_text))
            with s.container(border=True):
                with s.spinner("AI is writting for you"):
                    s.markdown(ap.note_generator(pill_image, ap.generate_prompt(pill_image,1,option)))
