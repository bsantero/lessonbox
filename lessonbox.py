from tkinter import *
from tinydb import TinyDB, Query
from subprocess import run

def printHello():
  run(["echo", "Hello World"])
def listAll():
  run(["ls", "-al"])
def purgeDB():
	db.purge()
def quitApp():
  root.destroy()
def allStudents(l):
	global names
	n_components = db.all()
	names = ''
	for i in n_components:
		names = names + i['name'] + ', '
	l.config(text=names)
	print (names)

db = TinyDB('db.json')
root = Tk()

#FullScreen
#root.overrideredirect(True)
#root.overrideredirect(False)
#root.attributes('-fullscreen',True)

root.geometry("1024x576")

#Database Testing
db.purge()
db.insert({'id':0, 'name':'Jadie Kordan', 'student':True, 'firstDate': '8/29/16', 'school':['Curtis','Juilliard']})
db.insert({'id':1, 'name':'Oretnas Nairb', 'student':False, 'firstDate': '1/10/15', 'school':'none'})
db.insert({'id':2, 'name':'Vaughn der Alex', 'student':True, 'firstDate': '8/28/18', 'school':['Oberlin','Curtis','Juilliard']})

numInDb = len(db)
index = 1
bool = True
User = Query()
Student = db.search(User['id'] == index)
print(Student[0])

#Gui Elements
labelStudentName = Label(root, text=Student[0]['name'])
labelDbNum = Label(root, text=numInDb)
quit = Button(root, text = 'QUIT', command = quitApp)
printHello = Button(root, command=printHello, text="Say Something")
exitPrgm = Button(root, command=quitApp, text="Exit")
listDir = Button(root, command=listAll, text="List Dir")
labelDbAll = Label(root, fg="green")
allStudents(labelDbAll)
     
#Gui Elements Properties
quit.grid(row=0, column=0)
labelDbNum.grid(row=0, column=1)
labelStudentName.grid(row=1, column=0, columnspan=2)
printHello.grid(row=2, column=0)
listDir.grid(row=2, column=1)
labelDbAll.grid(row=3,column=1,columnspan=2)

#Run Main Loop
root.mainloop()