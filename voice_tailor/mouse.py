# 控制鼠标滚动
from pymouse import PyMouse


def mouse_control(dir_tr):
    MOVE_DX = 5  # 每次滚动行数
    ms = PyMouse()
    horizontal = 0
    vertical = 0
    if dir_tr.find("上") != -1:  # 向上移动
        vertical = MOVE_DX
        # print("vertical={0}, 向上".format(vertical))
    elif dir_tr.find("下") != -1:  # 向下移动
        vertical = 0 - MOVE_DX
        # print("vertical={0}, 向下".format(vertical))
    elif dir_tr.find("左") != -1:  # 向左移动
        horizontal = 0 - MOVE_DX
        # print("horizontal={0}, 向左".format(horizontal))
    elif dir_tr.find("右") != -1:  # 向右移动
        horizontal = MOVE_DX
        # print("horizontal={0}, 向右".format(horizontal))

    # print("horizontal, vertical=[{0},{1}]".format(horizontal, vertical))
    # 通过scroll(vertical, horizontal)函数控制页面滚动
    # 另外PyMouse还支持模拟move光标,模拟鼠标click,模拟键盘击键等
    ms.scroll(vertical, horizontal)
