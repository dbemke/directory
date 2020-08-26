telefonos = {'Adam':577568429,'Bartek':546096742}
telefonos['Camel']=645986723
print('MENU')
print('PHONE BOOK')
print('1. List all entries \n2. Add new entries\n3.Exit')
x = int(input("What would you like to do?\nPlease enter a number: "))
while True:
    if x== 1:
        for key, value in telefonos.items():
            print(key, ' : ', value)
    if x == 2:
        name = input('What is the persons name?')
        tel = input('Whats his/her number?')
        telefonos[name]=tel
        #print(telefonos)
    if x ==3:
        print('Thank you')
        break
#question1 = input('Do you want to check sbs number?')
#if question1 == 'no':
 #   print('Answer yes or no')
  #  question2 = input('Do you want to add number?')
   # if question2 == 'yes':
      #  name = input('What is the persons name?')
       # tel = input('Whats his/her number?')
       # telefonos[name]=tel
        #print(telefonos)
    #else:
     #   print('Thank you.Bye')
#elif question1 == 'yes':
 #   nameinquiry = input('What is the persons name?')
  #  if nameinquiry in telefonos:
   #     print(nameinquiry,telefonos[nameinquiry])
    #else:
     #   print('Sorry- no number')
#else:
 #   print('JOZEK miales odpowiedzec yes or no !!!')