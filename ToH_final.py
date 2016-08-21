import random
import sys
optimal_set = [7, 6, 5, 4, 3, 2, 1]
set1 = [7, 6, 5, 4, 3, 2, 1]
set2 = []
set3 = []

def movement(seta, setb):
    lengtha = len(seta)
    lengthb = len(setb)
    transition = seta[lengtha - 1]
    del seta[lengtha - 1]
    setb.append(transition)

def trial_failure_check(setb):
    global failure
    lengthb = len(setb)
    if setb[lengthb - 1] > setb[lengthb - 2]:
        failure = True
    else:
        failure = False

probability_index = {1 : [37, 7, 13, 19, 25, 31, 37]}

def old_choose_set(set1, set2, set3):
    global seta
    global setb
    randint1 = random.randrange(1, 4)
    randint2 = random.randrange(1, 4)
    while randint1 == randint2:
        randint1 = random.randrange(1, 4)
        randint2 = random.randrange(1, 4)
    if randint1 == 1:
        seta = set1
    elif randint1 == 2:
         seta = set2
    elif randint1 == 3:
        seta = set3
    else:
        pass
    if randint2 == 1:
        setb = set1
    elif randint2 == 2:
        setb = set2
    elif randint2 == 3:
        setb = set3
    else:
        pass

def choose_set(set1, set2, set3, probability_index, max_iteration):
    global seta
    global setb
    global choice
    choice_set = probability_index[max_iteration]
    if "override" in choice_set:
        choice = choice_set[1]
    else:
        randint = random.randrange(1, choice_set[6])
        if randint in range(1, choice_set[1]):
            choice = 1
        elif randint in range(choice_set[1], choice_set[2]):
            choice = 2
        elif randint in range(choice_set[2], choice_set[3]):
            choice = 3
        elif randint in range(choice_set[3], choice_set[4]):
            choice = 4
        elif randint in range(choice_set[4], choice_set[5]):
            choice = 5
        elif randint in range(choice_set[5], choice_set[6]):
            choice = 6
        else:
            pass
    if choice == 1:
        seta = set1
        setb = set2
    elif choice == 2:
        seta = set1
        setb = set3
    elif choice == 3:
        seta = set2
        setb = set1
    elif choice == 4:
        seta = set2
        setb = set3
    elif choice == 5:
        seta = set3
        setb = set1
    elif choice == 6:
        seta = set3
        setb = set2
        

def level_advancement(max_level, set2, set3, failure):
    global advancement
    global new_max_level
    if len(set2) > max_level and failure != True:
        new_max_level = len(set2)
        advancement = True
    elif len(set3) > max_level and failure != True:
        new_max_level = len(set3)
        advancement = True
    else:
        advancement = False

def probability(set_choice, choice, change):
    global new_set_choice
    if change < 0 and "override" not in set_choice:
        while True:
            try:
                difference = set_choice[choice + 1] - set_choice[choice] - 1
                break
            except:
                difference = set_choice[choice] - set_choice[choice - 1] - 1
                break
        change = difference
        for item in range(choice + 1, 7):
            set_choice[item] -= change
    elif "override" in set_choice:
        pass
    else:
        for item in range(choice + 1, 7):
            set_choice[item] += change
    new_set_choice = set_choice

def probability_manipulation(advancement, failure, advance_iteration, probability_index, choice):
    choice_set = probability_index[max_iteration]
    if advancement == True:
        probability_index[max_iteration - 1] = ["override"]
        probability_index[max_iteration - 1].append(choice)
    if advance_iteration == True and failure != True:
        probability_index[max_iteration - 1] = ["override"]
        probability_index[max_iteration - 1].append(choice)
    elif failure != True:
        if "override" in choice_set:
            pass
        else:
            probability(choice_set, choice, 1)
    elif failure == True:
        probability(choice_set, choice, -1)

max_level = 0
max_iteration = 0
trial_iterations = 0
reserve = {1 : [], 2 : [], 3 : []}
ultimate_success = False
while ultimate_success != True:
    trial_success = False
    iteration_history = []
    while trial_success != True and trial_success != "Failure":
        iteration_success = False
        while iteration_success != True and iteration_success != "Failure" and iteration_success != "Success":
            if max_iteration == 0:
                seta = set1
                setb = set2
                choice = 1
            else:
                choose_set(set1, set2, set3, probability_index, max_iteration)
            if len(seta) == 0:
                break
            print seta
            print setb
            movement(seta, setb)
            print seta
            print setb
            trial_failure_check(setb)
            level_advancement(max_level, set2, set3, failure)
            if failure == False and failure != True:
                max_iteration += 1
                probability_index[max_iteration] = [37, 7, 13, 19, 25, 31, 37]
                advance_iteration = True
            else:
                advance_iteration = False
            iteration_history.append(choice)
            probability_manipulation(advancement, failure, advance_iteration, probability_index, choice)
            print "Advance Iteration: " + str(advance_iteration)
            if advancement == True:
                max_level = new_max_level
                for x in range(1000):
                    print max_level
            if failure == True:
                print "Failure"
                movement(setb, seta)
                reserve[1] = set1
                reserve[2] = set2
                reserve[3] = set3
                iteration_success = "Failure"
            elif set2 == optimal_set or set3 == optimal_set:
                iteration_success = "Success"               
        if iteration_success == "Failure":
            trial_iterations += 1
            print "history: " + str(iteration_history)
            iteration_history = []
            print "max level: " + str(max_level)
            print "Trial iteration: "+str(trial_iterations)
            print "max iteration: " + str(max_iteration)
            
            set1 = reserve[1]
            set2 = reserve[2]
            set3 = reserve[3]
            trial_success = "Failure"
        elif iteration_success == "Success":
            print "THE GODS HAVE SMILED UPON US! SUCCESS!!!!!"
            trial_success = True
    if trial_success == True:
        print probability_index
        ultimate_success = True
