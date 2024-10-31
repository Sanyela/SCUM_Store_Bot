import time, pyautogui, psutil, pyperclip, keyboard, sys, os, socks, socket
import codecs, re, threading, win32gui, win32con
from ftplib import FTP
from flask import Flask, request
from datetime import datetime, timedelta
import pygetwindow as gw

os.system("title SCUM 商城后端")
app = Flask(__name__)

# 基础配置
KEYS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'enter', 'space', 'backspace', 'delete', 'insert', 'home', 'end', 'page up', 
        'page down', 'left', 'right', 'up', 'down', 'shift', 'ctrl', 'alt', 'caps lock', 'num lock', 'scroll lock',
        'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']

# 设置代理和FTP连接
socks.set_default_proxy(socks.SOCKS5, "localhost", 8889)
socket.socket = socks.socksocket
ftp = FTP()
ftp.connect('127.0.0.1', '1234')
ftp.login(user='admin', passwd='admin')

def send_command(command):
    """统一的命令发送函数"""
    try:
        activate_scum_window()
        activate_and_lock_keyboard()
        if psutil.Process(get_scum_pid()).name() == "SCUM.exe":
            if gw.getWindowsWithTitle('SCUM  '):
                pyautogui.write("t")
                time.sleep(0.1)
                pyperclip.copy(command)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')
                unlock_keyboard()
                return "成功"
        return "游戏未运行"
    except Exception as e:
        return f"错误: {str(e)}"

def get_scum_pid():
    for proc in psutil.process_iter():
        if proc.name() == 'SCUM.exe':
            return proc.pid
    return None

def activate_scum_window():
    hwnd = win32gui.FindWindow(None, 'SCUM  ')
    if hwnd:
        pyautogui.hotkey('win', 'd')
        time.sleep(0.5)
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)

def activate_and_lock_keyboard():
    if gw.getWindowsWithTitle('SCUM  '):
        gw.getWindowsWithTitle('SCUM  ')[0].activate()
        for key in KEYS:
            keyboard.block_key(key)

def unlock_keyboard():
    for key in KEYS:
        keyboard.unblock_key(key)

@app.route('/tp_service/')
def tp_service():
    steamid = request.args.get('SteamID')
    tp_locations = {
        "A0": (-613404.188, -556331.750, 2435.560),
        "Z3": (27467.420, -677666.313, 347.970),
        "B4": (577438.125, -228798.031, 365.020),
        "C2": (-147688.609, 292396.125, 69688.172)
    }
    loc = tp_locations.get(request.args.get('safe_area'))
    if loc:
        return send_command(f'#teleport {loc[0]} {loc[1]} {loc[2]} "{steamid}"')
    return "无效的位置"

@app.route('/new_tp/')
def new_tp():
    return send_command(f'#teleportto "{request.args.get("SteamIDA")}" "{request.args.get("SteamIDB")}"')

@app.route('/add_blance/')
def add_blance():
    return send_command(f'#ChangeCurrencyBalance Normal {request.args.get("num")} {request.args.get("SteamID")}')

def monitor_login_file():
    pattern = re.compile(r"(\d{4}.\d{2}.\d{2}-\d{2}.\d{2}.\d{2}): '(?:\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3} |0.0.0.0 )\d{17}:(.*?)(?:\(\d+\))' logged (.*?) at")
    last_line = None
    first_run = True

    while True:
        try:
            files = [f for f in ftp.nlst('156.146.56.42_7120') if f.startswith('login')]
            if files:
                buffer = bytearray()
                ftp.retrbinary(f'RETR 156.146.56.42_7120/{files[-1]}', buffer.extend)
                content = codecs.decode(buffer, 'utf-16-le')
                
                for line in content.split('\n'):
                    if line == last_line:
                        continue
                    match = pattern.match(line)
                    if match and not first_run:
                        date_time = datetime.strptime(match.group(1), '%Y.%m.%d-%H.%M.%S') + timedelta(hours=9)
                        action = '上线了' if match.group(3) == 'in' else '下线了'
                        send_command(f'【{date_time.strftime("%Y.%m.%d %H.%M.%S")}】尊敬的玩家：【{match.group(2)}】{action}！！！')
                    last_line = line
                first_run = False
        except Exception as e:
            print(f"监控错误: {str(e)}")
        time.sleep(5)

if __name__ == '__main__':
    threading.Thread(target=monitor_login_file, daemon=True).start()
    app.run()
