import pyaudio, whisper

def record_and_transcribe():
    model = whisper.load_model("base")
    p = pyaudio.PyAudio()
    
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)
    
    print("Recording...")
    
    while True:
        data = stream.read(1024)
        result = model.transcribe(data)
        yield result["text"]
    