def recommend(score):
    if score >= 25:
        return "Do Zumba Today"
    elif score >= 20:
        return "Light walk"
    elif score >= 10:
        return "Study session"
    else:
        return "Rest"



name=input("Enter Your Name: ")
sleep_hr=int(input("Enter sleep hour: "))
energy_level=int(input('Enter energy level(1-10): '))
mood=int(input("rate mood(1-10): "))
score=sleep_hr+energy_level+mood

print('Your Details are: ')
print('Name:',name)
print('Sleep Hour:',sleep_hr)
print('Energy Level:',energy_level)
print('Mood:',mood)
task=recommend(score)
print('Recommended Activity:',task)
score=((sleep_hr*5)+(energy_level*5)+(mood*5))
print('Your Score is:',score)


