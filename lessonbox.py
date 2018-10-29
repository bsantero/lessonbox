import sys
from tinydb import TinyDB, Query
from subprocess import run
from guizero import App, Text, Combo, CheckBox, ButtonGroup, PushButton, info

def print_hello():
    run(["echo", "Hello World"])
def list_all():
    run(["ls", "-al"], shell=True)
def exit_program():
    sys.exit()

db = TinyDB('db.json')

app = App(title="LessonBox", width=1024, height=768, layout="grid")

btn_print_hello = PushButton(app, command=print_hello, text="Say Something", grid=[0,1], align="left")
btn_list_dir = PushButton(app, command=list_all, text="List Dir", grid=[1,1], align="left")
btn_exit_prgm = PushButton(app, command=exit_program, text="Exit", grid=[3,0], align="right")
                         
app.display()
