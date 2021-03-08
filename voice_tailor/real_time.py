from audio import audio_record
from baidu_api import aip_get_asrresult
from mouse import mouse_control
import time

while (True):
    # 请说出语音指令，例如["向上", "向下", "向左", "向右"]
    print("\n\n==================================================")
    print("Please tell me the command(limit within 3 seconds):")
    # print("Please tell me what you want to identify(limit within 10 seconds):")
    audio_record(AUDIO_OUTPUT, 3)  # 录制语音指令
    print("Identify On Network...")
    asr_result = aip_get_asrresult(client, AUDIO_OUTPUT, AUDIO_FORMAT)  # 识别语音指令
    if len(asr_result) != 0:  # 语音识别结果不为空，识别结果为一个list
        print("Identify Result:", asr_result[0])
        print("Start Control...")
        mouse_control(asr_result[0])  # 根据识别结果控制页面滚动
        print("Control End...")
        if asr_result[0].find("退出") != -1:  # 如果是"退出"指令则结束程序
            break;
        time.sleep(1)  # 延时1秒
