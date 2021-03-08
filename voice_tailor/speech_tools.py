import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
# print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language="zh"))


#
# r = sr.Recognizer()    #调用识别器
# test = sr.AudioFile("C:\\Users\cc\Desktop\\test1.flac")   #导入语音文件
# with test as source:
#     audio = r.record(source)
# type(audio)
c = r.recognize_sphinx(audio, language='zh-cn')  # 识别输出
print(c)
