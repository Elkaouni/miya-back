import whisper
import torch
import numpy as np
import torch

import gpt4free
from gpt4free import Provider

def generate_response_gpt4free(prompt):
    response =  gpt4free.Completion.create(Provider.You, prompt=prompt)
    return response

def load_audio_model(model='base'):
    audio_model = whisper.load_model(model)
    return audio_model

def stt_whisper(audio_model, audio, english=False, verbose=False):
    audio_data = torch.from_numpy(np.frombuffer(audio.get_raw_data(), np.int16).flatten().astype(np.float32) / 32768.0)

    if english:
        result = audio_model.transcribe(audio_data,language='english')
    else:
        result = audio_model.transcribe(audio_data)

    if not verbose:
        predicted_text = result["text"]
        predicted_language = result["language"]
        
    return result

def load_tts_model():
    #load mu tts model here
    return None
    
def tts_response(audio_model, prompt):
    #return wav file
    return None


