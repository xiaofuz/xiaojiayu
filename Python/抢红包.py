import time
import pyautogui

x, y = 440, 511  # 鼠标需要移动到的位置
num_seconds = 2  # 将鼠标移动到指定坐标的间隔时间

pyautogui.moveTo(x, y, duration=num_seconds)

time.sleep(3)  # 延迟3秒
i = 60

while True:
    pyautogui.click()