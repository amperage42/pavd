#!/usr/bin/python3

import os
import sys
import subprocess

sys.path.append(os.path.join(os.path.dirname(__file__), "datastore"))
import readcsv


store = os.path.join(os.getcwd(), "", "datastore", "")
audio_store = os.path.join(os.getcwd(), "", "audio", "")
video_store = os.path.join(os.getcwd(), "", "video", "")


class Globals:
    def __init__(self, line=2):
        self.data = readcsv.CSVDetails(store+"titles.csv")
        self.line = line

    def start_youtube_dl_audio(self):
        while True:
            try:
                cp = self.data.get_col_row(1, g.line)
                print("Starting to rip :" + cp)
                if cp == "":
                    break
                else:
                    vid = self.data.get_col_row(1, self.line)
                    subprocess.call('youtube-dl --extract-audio --audio-format vorbis -o "' + audio_store + '%(title)s.%(ext)s" ' + vid, shell=True)
                    print(self.data.get_col_row(1, self.line))
                    g.line += 1
            except IndexError:
                print("No more items found!")
                exit()
            except Exception as e:
                print("Error: %s" % (e))
            

    def start_youtube_dl_video(self):
        while True:
            try:
                cp = self.data.get_col_row(1, g.line)
                print("Starting to rip :" + cp)
                if cp == "":
                    break
                else:
                    vid = self.data.get_col_row(2, self.line)
                    subprocess.call('youtube-dl -o "' + video_store + '%(title)s.%(ext)s" ' + vid, shell=True)
                    print(self.data.get_col_row(2, self.line))
                    g.line += 1
            except IndexError:
                print("No more items found!")
                exit()
            except Exception as e:
                print("Error: %s" % (e))
        


g = Globals()
while True:
    print("\n****************************************\n***********Welcome to P.A.V.D.!***********\n****************************************\n")
    type_content = input("Would you like to download video (v) or audio (a) or exit (q)? ")
    if type_content == "a":
        try:
            g.start_youtube_dl_audio()
        except Exception as e:
            print("Error: %s" % (e))
    elif type_content == "v":
        try:
            g.start_youtube_dl_video()
        except Exception as e:
            print("Error: %s" % (e))
    elif type_content == "q":
        print("Goodbye!")
        exit()
