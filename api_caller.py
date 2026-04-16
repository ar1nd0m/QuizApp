import os
from google import genai 
from dotenv import load_dotenv
from gtts import gTTS
import io
load_dotenv()
api_key= os.getenv("key")
client=genai.Client(api_key=api_key)
def generate_audio(answer):
        speech=gTTS(answer,lang='en',slow=False)
        audio_buffer=io.BytesIO()
        speech.write_to_fp(audio_buffer)
        return audio_buffer
def note_generator(pill_image,prompt):
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[pill_image,prompt]
    )
    return response.text
def generate_prompt(pill_image,type,difficulty):
    
    if type == 0:
        prompt = "summarize the picture in note format at max in 100 words, make sure to add necessary markdown to differentiate different sections"
    else:
        prompt = f"generate 15 quizzes at difficulty level {difficulty}"
    return prompt