import time
import webbrowser

print("This program started on "+time.ctime())
for i in range(3):
    time.sleep(5)
    webbrowser.open("http://bbc.co.uk/")

