letters=[]
inputKey = u"о"
stroka = ''
def setup():
    size(600,400)
def draw():
    global inputKey,letters,stroka
    background(100)
    text(stroka,100,40) #поле ввода
    for letter in letters: # вывод списка букв
        fill(random(200,255),random(200,255),random(200,255))
        text(letter,10,40)
        translate(0,30)
def keyPressed():
    global inputKey,letters,stroka
    
    if key!=CODED and key!=ENTER and key!=RETURN and key!=BACKSPACE:
        inputKey = key
        stroka = stroka+inputKey
    elif key==ENTER or key==RETURN  :
        letters.append(stroka)
        stroka=''
    
    elif key==BACKSPACE:
        if len(letters)>0:
    
            poslednyy = len(letters) - 1
            del letters[poslednyy]
