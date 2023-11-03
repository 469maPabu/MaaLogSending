import sys
import os
import datetime
from send_email import send_email

def read_config(config_filename='config.txt'):
    config_path = os.path.join(os.getcwd(), config_filename)  # 直接使用当前目录路径
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

    log_path = os.path.join(os.getcwd(), 'debug', 'gui.log')  # 直接使用当前目录路径

    try:
        with open(log_path, 'r', encoding='utf-8') as log_file:
            log_content = log_file.read()
    except FileNotFoundError:
        print(f"日志文件 {log_path} 未找到。")
        sys.exit(1)
    
    last_connection_line, log_to_send = find_last_connection_attempt(log_content)
    print({log_to_send})
    if last_connection_line is None:
        print("未在日志中找到连接尝试。")
        sys.exit(1)
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if "任务出错" in log_to_send:
        subject = f"{current_time} 运行出错-MAA运行日志"
        content = f"{current_time} 运行出错！请检查出错情况。\n\n{log_to_send}"
    else:
        subject = f"{current_time} 运行成功-MAA运行日志"
        content = f"{current_time} 运行成功！\n\n{log_to_send}"
    
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




