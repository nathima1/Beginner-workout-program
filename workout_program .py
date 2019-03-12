#import libraries
import statistics as s


#variables
excersize = ['Push', 'Pull', 'legs']
push = ['bench', 'dips', 'OHP']
pull = ['row','pullup', 'deadlift']
legs = ['squat', 'hip thrust', 'lunges']


#different workout selctions

#Strength selection for push
def push_strength():
    excersize_select = input('Select your excersize (bench, dips, or OHP): ')
    max_input = float(input('Enter your max: '))
    calc_workout_one =  float(max_input)*.90
    calc_strength_two = float(max_input)*.85
    if excersize_select in push:
        print('You have selected', excersize_select)
        print(excersize_select, calc_workout_one, 'for 3 sets of 1! Add 5 lbs total every week')
        print(excersize_select, calc_strength_two, 'for 3 sets of 3! Add 5 lbs total every week')
    else:
        print('Invalid selection')
# Hypertrophy for Push
def push_size():
    excersize_select = input('Select your excersize (bench, dips, or OHP): ')
    max_input = float(input('Enter your max: '))
    calc_workout_size_one =  float(max_input)*.80
    calc_size_two = float(max_input)*.75
    if excersize_select in push:
        print('You have selected', excersize_select)
        print(excersize_select, calc_workout_size_one, 'for 6 sets of 6! Add 5 lbs total every week')
        print(excersize_select, calc_size_two, 'for 3 sets of 8! Add 5 lbs total every week')
    else:
        print('Invalid selection')

def pull_strength():
    excersize_select = input('Select your excersize (row, pullup, or deadlift): ')
    max_input = float(input('Enter your max: '))
    calc_workout_one =  float(max_input)*.90
    calc_strength_two = float(max_input)*.85
    if excersize_select in pull:
        print('You have selected', excersize_select)
        print(excersize_select, calc_workout_one, 'for 3 sets of 1! Add 5 lbs total every week')
        print(excersize_select, calc_strength_two, 'for 3 sets of 3! Add 5 lbs total every week')
    else:
        print('Invalid selection')

def pull_size():
    excersize_select = input('Select your excersize (row, pullup, or deadlift) (): ')
    max_input = float(input('Enter your max: '))
    calc_workout_size_one =  float(max_input)*.80
    calc_size_two = float(max_input)*.75
    if excersize_select in pull:
        print('You have selected', excersize_select)
        print(excersize_select, calc_workout_size_one, 'for 6 sets of 6! Add 5 lbs total every week')
        print(excersize_select, calc_size_two, 'for 3 sets of 8! Add 5 lbs total every week')
    else:
        print('Invalid selection')

def leg_strength():
    excersize_select = input('Select your excersize (squat, hip thrust, or lunges): ')
    max_input = float(input('Enter your max: '))
    calc_workout_one =  float(max_input)*.90
    calc_strength_two = float(max_input)*.85
    if excersize_select in legs:
        print('You have selected', excersize_select)
        print(excersize_select, calc_workout_one, 'for 3 sets of 1! Add 5 lbs total every week')
        print(excersize_select, calc_strength_two, 'for 3 sets of 3! Add 5 lbs total every week')
    else:
        print('Invalid selection')

def leg_size():
    excersize_select = input('Select your excersize (squat, hip thrust, or lunges) (): ')
    max_input = float(input('Enter your max: '))
    calc_workout_size_one =  float(max_input)*.80
    calc_size_two = float(max_input)*.75
    if excersize_select in legs:
        print('You have selected', excersize_select)
        print(excersize_select, calc_workout_size_one, 'for 6 sets of 6! Add 5 lbs total every week')
        print(excersize_select, calc_size_two, 'for 3 sets of 8! Add 5 lbs total every week')
    else:
        print('Invalid selection')
def main():
    print("""
    Welcome to Workout planner!
    [1] - Push Strength
    [2] - Push Size
    [3] - Pull Strength
    [4] - Pull Size
    [5] - Leg Strength
    [6] - Leg Size
    [7] - Exit
    """)

    action = input("Select desired workout: ")

    if action == '1':
        push_strength()
    elif action == '2':
        push_size()
    elif action == '3':
        pull_strength()
    elif action == '4':
        pull_size()
    elif action == '5':
        leg_strength()
    elif action == '6':
        leg_size()
    elif action == '7':
        exit()
    else:
        print('invalid selection')

main()
