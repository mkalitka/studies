from openai import OpenAI

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    text="Hello, my name is John.",
    voice="onyx",
)

response.stream_to_file("hello.mp3")
