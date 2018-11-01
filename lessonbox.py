from tkinter import *
from tinydb import TinyDB, Query
from subprocess import run

global index, Student, studentName
Student = ''
studentName = 'trombone'
index = 1
db = TinyDB('db.json')
User = Query()
print('variables set')

def printHello():
  run(["echo", "Hello World"])
def listAll():
  run(["ls", "-al"])
def purgeDB():
	db.purge()
def quitApp():
  root.destroy()
def allStudents(l):
	n_components = db.all()
	global names
	names = ''
	for i in n_components:
		names = names + i['name'] + ', '
	l.config(text=names)
	#print (names)
def dbChange(dir):
	print('button pressed: ' + dir)
	global index
	dbLen = len(db.all()) - 1
	if dir == 'up' and index < dbLen:
		index += 1
	elif dir == 'down' and index > 0:
		index -= 1
	print('Index is at: ' + str(index) + ' - ' + str(studentName))
	getName()
def getName():
	print('getName- Index is: ' + str(index))
	Student = db.search(User['id'] == index)
	print('getName- Student is: ' + str(Student))
	print('getName- Student name: ' + Student[0]['name'])
	print('changing label')
	labelIndexLoc['text'] = index
	labelStudentName['text'] = str(Student[0]['name'])

print('methods set')

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
db.insert({'id':3, 'name':'William Tall', 'student':False, 'firstDate': '11/1/88', 'school':['Curtis','Rice']})

print('db set')

#Gui Elements
descIndexLoc = Label(root, text="Number in Database: ")
labelIndexLoc = Label(root, text=index, padx=5, borderwidth=2, relief="groove")
quit = Button(root, text = 'QUIT', command = quitApp)
descStudentName = Label(root, text="Name of Student: ")
labelStudentName = Label(root, text=studentName, padx=5, borderwidth=2, relief="groove")
prevStudent = Button(root, command= lambda: dbChange('down'), text="Previous")
nextStudent = Button(root, command= lambda: dbChange('up'), text="Next")
listDir = Button(root, command=listAll, text="List Dir")
labelDbAll = Label(root, fg="green", padx=5, borderwidth=2, relief="groove")
allStudents(labelDbAll)

print('gui initialized')

#Gui Elements Properties
descIndexLoc.grid(row=0, column=0)
labelIndexLoc.grid(row=0, column=1)
quit.grid(row=0, column=3)
descStudentName.grid(row=1, column=0)
labelStudentName.grid(row=1, column=1)
prevStudent.grid(row=2, column=0)
nextStudent.grid(row=2, column=1)
labelDbAll.grid(row=3,column=0,columnspan=2)

print('gui set')

#Setup Main Loop
getName()
print('preMainLoop- Student ' + str(studentName))
print('preMainLoop- Index is at: ' + str(index) + ' - ' + str(studentName))

#Run Main Loop
root.mainloop()