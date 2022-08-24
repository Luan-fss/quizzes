import time

# Colocar versão portugues e ingles como escolha .... 
# Colocar TODOS temas, e 2 sub temas para cada um

print('Welcome to my quiz :)')
#time.sleep(1)

#playing = input('Do you want to play? (Y)es (N)o \n').lower()

#if playing == 'y' or playing == 'yes':
#    print('So... Lets go play this game :)')
#else:
#    quit()

score = 0
choice = input('First, choose one theme pls: \n(1) Animals  (2) Cars  (3) Games  (4) Solar system planets \n')

if choice == '1':
    sub_theme = input('Choose a sub theme: \n(1) Curiosities about animals (2) Felines\n')
    if sub_theme == '1':
        #################################################################################################################################################
        question1 = print('What is the largest land animal?')
        answer = input(' (1) Indian elephant\n (2) African elephant\n (3) White rhino\n (4) African lion\n (5) Blue whale\n')
        if answer == '2':
            print('Correct!')
            score += 1
        else:
            print('Incorrect!')
        ##########################################################
        question2 = print('Qual o maior felino?')
        answer = input('Type an answer: ').lower()
        if answer == 'siberian tiger':
            print('Correct!')
            score += 1
        else:
            print('Incorrect!')
        ###########################################################

    elif sub_theme == '2':
        #############################################################################################################################################
        question1 = print('What is the only feline species that specimens are found alone?')
        answer = input(' (1) Cheetah\n (2) Tiger\n (3) Lion\n (4) Cat\n (5) Lynx\n')
        if answer == '3':
            print('Correct!')
            score += 1
        else:
            print('Incorrect, the answer is Lion')
        ###########################################################
        question2 = print('Which of the following felines has a larger size?')
        answer = input(' (1) Cheetah\n (2) Leopard\n (3) Caracal\n (4) Ounce\n (5) Tiger\n')
        if answer == '5':
            print('Correct!')
            score += 1
        else:
            print('Incorrect, the answer is Tiger')
        ###########################################################
        question3 = print('Which one of the next cats hunts at night?')
        answer = input(' (1) Lion\n (2) Cat\n (3) Tiger\n (4) Puma\n (5) Leopard\n')
        if answer == '1':
            print('Correct!')
            score += 1
        else:
            print('Incorrect, the answer is Lion')
        ###########################################################
        question4 = print('Which of the following felines is smaller?')
        answer = input(' (1) Lynx\n (2) Desert lynx\n (3) Fishing cat (Prionailurus viverrinus)\n (4) Sand Cat\n')
        if answer == '4':
            print('Correct!')
            score += 1
        else:
            print('Incorrect, the answer is Sand cat')
        ###########################################################
        question5 = print('The male lion is the slowest of all the big cats. True or false?')
        answer = input(' (1) True\n (2) False\n')
        if answer == '1':
            print('Correct!')
            score += 1
        else:
            print('Incorrect, the answer is True')
        ###########################################################
        question6 = print('Which of the cats to follow has the best ability to climb trees?')
        answer = input(' (1) Tiger\n (2) Cat\n (3) Leopard\n (4) Puma\n')
        if answer == '3':
            print('Correct!')
            score += 1
        else:
            print('Incorrect, the answer is Leopard')    
        ###########################################################
        question7 = print('Which of the cats to follow has the greatest custom and ability to hunt birds?')
        answer = input(' (1) Lynx\n (2) Desert lynx\n (3) House cat\n ')
        if answer == '2':
            print('Correct!')
            score += 1
        else:
            print('Incorrect, the correct answer is Desert lynx')
        ###########################################################
        question8 = print('What is the name of the largest tiger species today (2016)? TIP: s....... tiger')
        answer = input('Type an answer: ').lower()
        if answer == 'siberian tiger':
            print('Correct!')
            score += 1
        else:
            print('Incorrect, the correct answer is siberian tiger')
        ###########################################################
        question9 = print('What is the name of the most recently discovered feline species? TIP: ne..b... panther')
        answer = input('Type an answer: ').lower()
        if answer == 'nebula panther':
            print('Correct!')
            score += 1
        else:
            print('Incorrect, the correct answer is nebula panther')
        ###########################################################
        question10 = print('How many breeds of domestic cats are there about?')
        answer = input(' (1) 80\n (2) 46\n (3) 60\n (4) 100\n')
        if answer == '1':
            print('Correct!')
            score += 1
        else:
            print('Incorrect, the correct answer is 80')

elif choice == '2':
    pass
elif choice == '3':
    pass
elif choice == '4':
    pass
else:
    print('Digite um número de tema válido')


# Creating score definition
if score == 10:
    print(f'OOWWW... YOU ARE INSANE, YOUR SCORE: {score}/10')
elif score >= 7:
    print(f'Congratulations, your Score: {score}/10')
elif score >= 4:
    print(f'You didnt do so well, your Score: {score}/10')
elif score >= 0:
    print(f'You were so bad... your Score: {score}/10')




