import random

x = 0

questions = {


    1 : "What is 1+1? ", 
    2 : "What is 2+2? ",
    3 : "What is 4+4? " 
}


answers = {
    1 : "2",
    2 : "4",
    3 : "8"
}





def quzzing(e,x):
    print("yo")

def chooseCourse(crz):
    return crz in courses:
        

def mainMenu(krs):
    lista = []
    list = []
    for i in range(1,len(questions)):
        lista.append(i)
        list.append(i)
    print(f'\tWELCOME TO STUDYGUIDE™\n')
    for i in range(len(krs)):
        print(f'{i+1}): {krs[i]} ')
    if input("Choose a course: ") in courses:
        quizzing()
    else:
        print("Not a course. Try again!")
        






courses = ['Grundläggande Algebra', 'Introduktion till IT']
mainMenu(courses)