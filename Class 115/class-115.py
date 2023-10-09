import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

source = "C:/Users/angel/Downloads"
destination = "C:/Users/angel/Desktop"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    #Student Activity1

    

    def on_created(self, event):
        name,ext = os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if ext in value:
                i = os.path.basename(event.src_path)
                print("downloaded" + i)
                path1 = source + '/' + i
                path2 = destination + '/' + key
                path3 = destination + '/' + key + '/' + i
                if os.path.exists(path2):
                    print("directory exists")

                    if os.path.exists(path2):
                        print("file already exists")
                        print("renaming file")
                        new_file_name = os.path.splitext(i)[0] + str(random.randint(0, 999)) + os.path.splitext(i)[1]
                        path4 = destination + '/' + key + '/' + new_file_name
                        print("moving")
                        shutil.move(path1, path4)
                        time.sleep(1)
                    else:
                        print("moving")
                        shutil.move(path1, path3)
                else:
                    os.makedirs(path2)
                    print("creating and moving")
                    shutil.move(path1, path3)


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, source, recursive=True)


# Start the Observer
observer.start()

#Student Activity2
try:

    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()
    

    