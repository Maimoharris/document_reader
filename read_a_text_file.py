import pyttsx3
run=pyttsx3.init()
path=input("Enter File Path:")
file=open(path,'r')
lines=file.readlines()
run.say(lines)
run.runAndWait()
run.setProperty('Rate',20)