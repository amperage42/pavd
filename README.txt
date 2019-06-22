Python Audio. Video. Downloader v. 0.0.1.

Is a program to download videos from the web and either convert them to mp3(audio) or to mp4(video).


Requirements: 
python3.x and youtube-dl with ffmpeg installed, Linux distro, Ubuntu 16.04+ was tested.
Extract the zip to a folder, and then to run program: Python3 avd.py


Install and use:

#1. Download or clone this repo.
#2. Add the desired link to the frist collumn the /datastore/titles.csv
#2. To run, navigate to the pavd directory and run: $~/: python3 avd.py


DUE to issues with youtube-dl 4-2019+ follow the below steps to install the patched version.

STEPS to install patched youtube-dl:

After that, you must install the latest version from the official youtube-dl repository on GitHub:

$ sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
$ sudo chmod a+rx /usr/local/bin/youtube-dl

If you do not have curl, you can alternatively use wget:

$ sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
$ sudo chmod a+rx /usr/local/bin/youtube-dl

Reference:
https://cialu.net/how-to-fix-the-token-parameter-not-in-video-info-for-unknown-reason-error/
