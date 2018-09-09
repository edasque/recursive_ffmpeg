import os
import re
import subprocess
import time

def scan(path):
    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                # print(entry.name)
                match = re.search(".*(mp4|mkv|m4v|wmv|avi)", entry.name)
                if match:
                    # print(match)
                    print(entry.path)
                    # pid = subprocess.Popen(["ffmpeg", "-i",entry.path]).pid
                    # pid = subprocess.Popen(["/usr/local/bin/ffprobe","-v error","-select_streams","v:0","-show_entries","stream=codec_name","-of","default=noprint_wrappers=1:nokey=1",entry.path]).pid
                    pid = subprocess.Popen(["/usr/local/bin/mediainfo",entry.path]).pid
                    while os.waitpid(pid, os.WNOHANG) == (0,0):
                        time.sleep(0.1)
                        print("Not finished")
                    print("finished")
                # else:
                    # print("NOT " + entry.path)
            elif not entry.name.startswith('.'):
                # print("->"+entry.path)
                # print("o>"+entry.name)
                scan(entry.path)
                

scan(".")
