import os
import re
import subprocess
import time
import shlex

def scan(path):
    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                # print(entry.name)
                match = re.search(".*(mp4|mkv|m4v|wmv|avi)", entry.name)
                if match:
                    # print(match)
                    input_filename = entry.path
                    output_filename = os.path.splitext(entry.path)[0]+'_h265.mkv'
                    ffmpeg_command = "/usr/local/bin/ffmpeg -i '"+input_filename+"' -c:v libx265 -crf 28 -s hd720 -c:a copy '"+output_filename+"'"
                    print(ffmpeg_command)
                    args = shlex.split(ffmpeg_command)
                    print(args)
                    # pid = subprocess.Popen(["ffmpeg", "-i",entry.path]).pid
                    # pid = subprocess.Popen(["/usr/local/bin/ffprobe","-v error","-select_streams","v:0","-show_entries","stream=codec_name","-of","default=noprint_wrappers=1:nokey=1",entry.path]).pid
                    # pid = subprocess.Popen(["/usr/local/bin/ffmpeg",ffmpeg_command]).pid
                    
                    pid = subprocess.Popen(args).pid

                    
                    
                    while os.waitpid(pid, os.WNOHANG) == (0,0):
                        time.sleep(1)
                    print("Conversion complete: "+input_filename+" -> "+output_filename)
                # else:
                    # print("NOT " + entry.path)
            elif not entry.name.startswith('.'):
                # print("->"+entry.path)
                # print("o>"+entry.name)
                scan(entry.path)
                

scan(".")
