from watchdog.events import FileSystemEventHandler
import datetime
def get_name(a):
        a = a.split("\\")
        a = a[len(a) - 1].split(".")
        return a[0]
class FileShedule(FileSystemEventHandler):
    def __init__(self, file_path) -> None:
        self._file_path = file_path
    def on_modified(self, event):
        with open('./text/'+get_name(event.src_path),'r') as conn:
            line = conn.readlines()[-1].split()
            print(str(datetime.datetime.now())+" >> "+line[0]+"^"+line[1]+"="+line[2])