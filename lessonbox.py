import sys
from subprocess import run
from guizero import App, Text, Combo, CheckBox, ButtonGroup, PushButton, info

#def do_booking():
#    info("Booking", "Thank you for booking with us")
#    print( film_choice.value )
#    print( vip_seat.value )
#    print( row_choice.value )

def print_hello():
    run(["echo", "Hello World"])
def list_all():
    run(["ls", "-al"], shell=True)
def exit_program():
    sys.exit()
  
app = App(title="LessonBox", width=1024, height=768, layout="grid")

#film_description = Text(app, text="Which film?", grid=[0,0], align="left")
#film_choice = Combo(app, options=["Star Wars", "Frozen", "Lion King"], grid=[1,0], align="left")

#vip_description = Text(app, text="Seat type", grid=[0,1], align="left")
#vip_seat = CheckBox(app, text="VIP seat?", grid=[1,1], align="left")

#row_description = Text(app, text="Seat location", grid=[0,2], align="left")
#row_choice = ButtonGroup(app, options=[ ["Front","F"],["Middle","M"],["Back","B"] ], selected="M", horizontal=True, grid=[1,2], align="left")

btn_print_hello = PushButton(app, command=print_hello, text="Say Something", grid=[0,1], align="left")
btn_list_dir = PushButton(app, command=list_all, text="List Dir", grid=[1,1], align="left")
btn_exit_prgm = PushButton(app, command=exit_program, text="Exit", grid=[3,0], align="right")
                         
app.display()
