import sys
import os
import datetime
from send_email import send_email

def get_resource_path(relative_path):
    """ 返回资源的绝对路径，用于访问包含在 PyInstaller --onefile 中的资源 """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def read_config(config_filename='config.txt'):
    config_path = get_resource_path(config_filename)
    config = {}
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            for line in f:
                if not line.strip() or line.startswith('#'):
                    continue
                key, value = line.strip().split('=', 1)
                config[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"配置文件 {config_path} 未找到。")
        sys.exit(1)
    return config

def find_last_connection_attempt(log_content):
    lines = log_content.splitlines()
    for line in reversed(lines):
        if "正在连接模拟器……" in line:
            return line, "\n".join(lines[lines.index(line):])
    return None, None

def main():
    config = read_config()

    # 从当前工作目录获取路径
    log_path = os.path.join(os.getcwd(), 'debug', 'gui.log')

    try:
        with open(log_path, 'r', encoding='utf-8') as log_file:
            log_content = log_file.read()
    except FileNotFoundError:
        print(f"日志文件 {log_path} 未找到。")
        sys.exit(1)
    
    last_connection_line, log_to_send = find_last_connection_attempt(log_content)
    print( {log_to_send} )
    if last_connection_line is None:
        print("未在日志中找到连接尝试。")
        sys.exit(1)
    
    current_time = datetime.datetime.now().strftime("%m-%d %H:%M")
    if "任务出错" in log_to_send:
        subject = f"{current_time} 运行出错-MAA运行日志"
        content = f"{current_time}运行出错！请检查出错情况。\n\n{log_to_send}"
    else:
        subject = f"{current_time} 运行成功-MAA运行日志"
        content = f"{current_time}运行成功！\n\n{log_to_send}"
    
    send_email(
        smtp_server=config['smtp_server'],
        port=int(config['port']),
        sender=config['sender'],
        password=config['password'],
        receiver=config['receiver'],
        subject=subject,
        content=content
    )

if __name__ == "__main__":
    main()



