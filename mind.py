from openai import OpenAI

from head.ears import listenVoiceAndSave
from head.mounth import speaking

openAI = OpenAI()

# Components 

# ## listening and Recogize 
# listenVoiceAndSave("./voiceTest.wav")
# voiceInput = open("./voiceTest.wav", "rb")
# inputVoiceText = openAI.audio.transcriptions.create(
#     model="whisper-1",
#     file=voiceInput
# )
# print(inputVoiceText.text)


##Response 

gfresponseStream = openAI.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}  #f'{inputVoiceText}'
  ],
  stream=True
)


words = ""
for chunk in gfresponseStream:
    word = chunk.choices[0].delta
    if word.content is not None: 
        
        #print(word.content)
        # print(word.content.replace(" ", ""))
        # print(word.content, end='') ()
        words += word.content  

      
        
## TextToVoice
voice = openAI.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=words
)
voice.stream_to_file(f'./gfVoice.mp3')    

# Speaking
## TextToVoice 

