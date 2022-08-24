import time

print('Welcome to my quiz :)')
time.sleep(1)

playing = input('Do you want to play? (Y)es (N)o \n').lower()

if playing == 'y' or playing == 'yes':
    print('So... Lets go play this game :)')
else:
    quit()

while True:
    choice = input('First, choose one theme pls: \n\
    (1) Animals  (2) Cars  (3) Games  (4) Solar system planets \n')

    if choice == 1:
        sub_theme = input('Choose a sub theme \n\
        (1) Curiosities about animals (2) Animal anatomy')
        if sub_theme == 1:
            pass
        if sub_theme == 2:
            pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    else:
        print('Digite o numero do tema correto')




