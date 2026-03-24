import whisper
from transformers import pipeline
import gradio as gr

# Load models
model = whisper.load_model("base")
sentiment = pipeline("sentiment-analysis")

# Function to process audio
def analyze_audio(audio):

    result = model.transcribe(audio)
    text = result["text"]

    sentiment_result = sentiment(text)[0]

    label = sentiment_result["label"]
    score = round(sentiment_result["score"] * 100, 2)

    return text, f"Sentiment: {label} ({score}%)"

# Gradio interface
demo = gr.Interface(
    fn=analyze_audio,
    inputs=gr.Audio(type="filepath"),
    outputs=["text", "text"],
    title="AI Voice Sentiment Analyzer",
    description="Upload audio to convert speech to text and detect sentiment."
)

demo.launch()
