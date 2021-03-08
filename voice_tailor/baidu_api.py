# 读取paudio录制好的音频文件, 调用百度语音API, 设置api参数, 完成语音识别
#    client:AipSpeech对象
#    afile:音频文件
#    afmt:音频文件格式(wav)
from pip._internal.req.req_file import get_file_content
CUID = '1023572829292874575181823817475182'
DEV_PID = []
def aip_get_asrresult(client, afile, afmt):
    # 选项参数:
    # cuid    String  用户唯一标识，用来区分用户，填写机器 MAC 地址或 IMEI 码，长度为60以内
    # dev_pid String  语言类型(见下表), 默认1537(普通话 输入法模型)
    # 识别结果已经被SDK由JSON字符串转为dict
    result = client.asr(get_file_content(afile), afmt, 16000, {"cuid": CUID, "dev_pid": DEV_PID,})
    #print(result)
    # 如果err_msg字段为"success."表示识别成功, 直接从result字段中提取识别结果, 否则表示识别失败
    if result["err_msg"] == "success.":
        #print(result["result"])
        return result["result"]
    else:
        #print(result["err_msg"])
        return ""
