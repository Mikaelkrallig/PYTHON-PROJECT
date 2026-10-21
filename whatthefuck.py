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







def mainMenu(krs):
    lista = []
    list = []
    for i in range(1,len(questions)):
        lista.append(i)
        list.append(i)
    print(f'\tWELCOME TO STUDYGUIDE™\n')
    for i in range(len(krs)):
        print(f'{i+1}): {krs[i]} ')
    if input("Choose a course: "):
        for i in range(0, len(lista)):
            x = list[random.randint(0,len(lista)-1)]
            if input(questions.get(x)) == answers.get(x):
                print("correct!")
            else: 
                print("Incorrect!")
            list.remove(x)





courses = ['Grundläggande Algebra', 'Introduktion till IT']
mainMenu(courses)



