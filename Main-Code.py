import pickle
from random import *
name2=input("enter player name:")
print("welcome to GUESS THE WORD",name2.capitalize())
#attempts=int(input('enter no of attempts(less than 20): '))
scoree=0
#if attempts>20:
#    while(attempts>20):
#        attempts=int(input('enter no of attempts to guess the word(less than 20):'))
#print("how many letter word do u want?")
#print("three(3),four(4),five(5) or greater than five(>5)")
#lett=int(input())
#while(lett<3):
#    lett=int(input("enter number greater than 2 "))    
names={1:'adolesant',2:'anticipate',3:'awful',4:'beneath',5:'biological',6:'bombing',7:'malignant',8:'scrumptious',9:'nausea',10:'anthropologist',11:'ambient',12:'christmas',13:'reversible',14:'yearly',15:'tactful',16:'technique',17:'radiant',18:'radical',19:'quaterback',20:'negligence',21:'lexological',22:'abroad',23:'accept',24:'across',25:'acting',26:'actual',27:'auspicious',28:'bottom',29:'philanthropist'
       }
three={1:['all','Hint : everyone'],2:['owl','Hint : large eyed bird '],3:['new','Hint : Fresh'],4:['mad','Hint : crazy'],5:['wow','Amazing'],6:['cap','Hint : Wear on head'],7:['yet','Hint : Not untill now'],8:['bad','Hint : Not good'],9:['mom','Hint : Gives Birth'],10:['sky','Hint : Above all'],11:['cat','Hint : Kitty'],12:['urn','Hint : Made of wool']}
four={1:['blow','Hint : Expel air through lips'],2:['host','Hint : Show organizer'],3:['ring','Hint : wear on hand'],4:['wolf','Hint : arctic animal'],5:['wife','Hint : reference to a person by husband'],6:['tree','Hint : oxygen producer'],7:['star','Hint : a million lights in the night sky'],8:['lion','Hint : king of the jungle'],9:['duck','Hint : move away to avoid a hit'],10:['rain','Hint : weeping sky']}
five={1:['sugar','Hint : sweetener'],2:['dream','Hint : a cherished aspiration'],3:['drama','Hint : a stage show'],4:['apple','Hint : if not this we would not have discovered gravity'],5:['pizza','Hint : a round eatable of slices'],6:['water','Hint : major content of our body'],7:['music','Hint : instrumental sounds'],8:['tiger','Hint : striped animal'],9:['story','Hint : a tale'],10:['india','Hint : nation of cultures']}
cont='n'
while(1):
    #print('HI')
    err=1
    while(err==1):
        try:  
            attempts=int(input('enter no of attempts to guess the word(less than 20):'))
            err=0
        except:
            print('Enter valid input')
            err=1
    if attempts>20:
        while(attempts>20):
            print('Enter value less than 20')
            try:  
                attempts=int(input('enter no of attempts to guess the word(less than 20):'))
                err=0
            except:
                print('Enter valid input')
                err=1
    #attempts=int(input('enter no of attempts to guess the word(less than 20):'))
    print("how many letter word do u want?")
    print("three(3),four(4),five(5) or greater than five(>5)")
    err=1
    while(err==1):
        try:
            lett=int(input())
            err=0
        except:
            print('Enter valid input')
            err=1
    err=1
    while(lett<3):
        try:  
            lett=int(input("enter number greater than 2 "))
            err=0
        except:
            print('Enter valid input')
            err=1
    '''if attempts>20:
        while(attempts>20):
            attempts=int(input('enter no of attempts to guess the word(less than 20):'))
    '''
    attempts=abs(attempts)
    at=attempts
    print('no of attempts to guess the word:',attempts)
    if lett==3:
        rand=randint(1,len(three))
        name=three[rand][0]
        hin=three[rand][1]
    elif lett==4:
        rand=randint(1,len(four))
        name=four[rand][0]
        hin=four[rand][1]
    elif lett==5:
        rand=randint(1,len(five))
        name=five[rand][0]
        hin=five[rand][1]
    else:    
        rand=randint(1,len(names))
        name=names[rand]
    star=['*']*len(name)
    fail=0
    name1=list(name)
    while(fail!=attempts):
        if(list(name)==star):
            scoree+=1
            print("YAYYY you have Guessed the word Right")
            #cont=input("Do u want to continue the game(y/n): ")
            #if cont=='n' or cont=='N':
            break
        print('Guess the word:',''.join(star))
        ch=input('Enter a letter to guess in word: ')
        #ch=ch[0]
        if ch in name1:
            if star[name1.index(ch)]=='*':
                star[name1.index(ch)]=ch
            name1[name1.index(ch)]='*'
        else:
            print('Wrong Guess')
            fail+=1
            if fail>(attempts//2):
                hi=input("Do u want a hint?(y/n)")
                if hi[0]=='y':
                    print(hin)
        print("attempts left =",attempts-fail)
    if fail==attempts:
        print("The word is",name)
        print('You have lost the game')
    cont=input('Do u want to play again(y/n): ')

    if cont=='n' or cont=='N':
        print('Your Score:',scoree)
        break
        #print(list(name))
        #print(star)

fp=open('text_file.txt','rb')
b=pickle.load(fp)
fp.close()
if b['score']<scoree:
    b['score']=scoree
    b['naam']=name2
fp=open('text_file.txt','wb')
pickle.dump(b,fp)
fp.close()
fp=open('text_file.txt','rb')
b=pickle.load(fp)
fp.close()
print("high score:",b['score'],"by",b['naam'].capitalize())
