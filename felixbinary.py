import random


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





def mainMenu(krs):
    print(f'\tWELCOME TO STUDYGUIDE™\n')
    for i in range(len(krs)):
        print(f'{i+1}): {krs[i]} ')
    if input("Choose a course: "):
        if input(questions.get(2)) == answers.get(2):
            print("correct!")
        else: 
            print("Incorrect!")






courses = ['Grundläggande Algebra', 'Introduktion till IT']
mainMenu(courses)



