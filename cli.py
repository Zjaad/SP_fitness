#!/usr/bin/python3

magenta = '\033[95m'
cyan = '\033[96m'
red = '\033[91m'
yellow = '\033[93m'
reset = '\033[0m'

banner = f"""{magenta}
  ╔═══════════════════════════╗
  ║   S P   BODY CALCULATOR   ║
  ╚═══════════════════════════╝{reset}"""

def paint(text , color):
    return f'{color}{text}{reset}'

def frame(lines):
    width = max(len(line) for line in lines) + 2
    box = '╔' + '═' * width + '╗\n'
    for line in lines:
        box += '║' + line.ljust(width) + '║\n'
    box += '╚' + '═' * width + '╝'
    return box
