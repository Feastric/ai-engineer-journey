name=input('Enter your name')
study=int(input('Study minutes today: '))
exercise=int(input("Workout minutes today: "))
score=study+exercise
print('\n RESULT')
print('User: ',name)
print('Total points: ',score)
if score>120:
    print('strong today')
else:
    print('Work harder tommorow')