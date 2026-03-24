# AI Voice Sentiment Analyzer

This project converts **speech to text using OpenAI Whisper** and then performs **sentiment analysis using HuggingFace Transformers**.

The system allows users to upload an audio file and automatically determine the emotional sentiment of the speech.

---

## Features

- Speech to Text using Whisper
- Sentiment Analysis using Transformers
- Audio Upload Interface
- Built and tested using Google Colab

---




---

## Project Workflow

Audio File  
↓  
Speech Recognition (Whisper)  
↓  
Text Transcription  
↓  
Sentiment Analysis (Transformers)  
↓  
Sentiment Result

---

## Technologies Used

- Python
- OpenAI Whisper
- HuggingFace Transformers
- Flask / Gradio
- Google Colab

---

## Project Structure

```
ai-voice-sentiment-analyzer
│
├── audio_sentiment_analyzer.ipynb
├── requirements.txt
├── README.md
├── images
│   ├── input_project.png
│   └── output_project.png
├── templates
│   ├── index.html
│   └── result.html
```

---

## How to Run

1. Install dependencies

```
pip install openai-whisper transformers torch flask
```

2. Run the application or notebook.

3. Upload an audio file.

4. View the transcription and sentiment analysis result.

---

## Future Improvements

- Emotion detection
- Real-time microphone input
- Better UI

---

## Author

TUSHAR KUMAR
