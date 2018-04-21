print('Hello, Django girls!')
if 3 > 2 :
    print('It works!')
    name = 'Vanessa'
    if name == 'Mariella':
        print ('Hello Mariella !')
    elif name == 'Vanessa':
        print('Hello Vanessa')
    else :
        print('Hello anonymous')
volume = 57
if volume < 20:
    print("C'est plutôt calme.")
elif 20 <= volume < 40:
    print("Une jolie musique de fond.")
elif 40 <= volume < 60:
    print("Parfait, je peux entendre tous les détails du morceau.")
elif 60 <= volume < 80:
    print("Parfait pour faire la fête !")
elif 80 <= volume < 100:
    print("Un peu trop fort !")
else:
    print("Au secours ! Mes oreilles ! :(")
def hi ():
    print('Hi there!')
    print('How are you?')

hi()
def hi2(name):
    if name == 'Vanessa':
        print('Hi Vanessa!')
    elif name == 'Mariella':
         print('Hi Mariella!')
    else:
        print('Hi anonymous !')
hi2('Carole')
def hi(name):
    print('Hi' + ' ' + name + '!')
hi('Rachel')
girls = ['Rachel','Monica', 'Phoebe', 'Vanessa']
def hi(name):
    print('Hi' + ' ' + name + '!')
girls = ['Rachel','Monica', 'Phoebe', 'Vanessa']
for name in girls:
    hi(name)
    print('Next girl')
for i in range(1,6):
    print(i)
