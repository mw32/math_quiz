#!/usr/bin/python

import operator
import random
import time

TYPES = {
         '1':('addition', operator.add, '+'),
         '2':('subtraction', operator.sub, '-'),
         '3':('multiplication', operator.mul, 'x'),
         '4':('division', operator.div, '/')
        }

OPS = {'1':operator.add,
       '2':operator.sub,
       '3':operator.mul,
       '4':operator.div}

type = max_int = max_time = None
total = solved = error = 0


def printplus(obj):
    # dict
    if isinstance(obj, dict):
        for k, v in sorted(obj.items()):
            print u'{0}: {1}'.format(k, v)
    # list or tuple            
    elif isinstance(obj, list) or isinstance(obj, tuple):
        for x in obj:
            print x
    # other
    else:
        print obj


def get_type_descs():
    d = {}
    for k,v in TYPES.items():
        d[k] = v[0]
    return d


def get_input_params():
    global type, max_int, max_time
    type_prompt = "Select exercise type %s : " 
    int_prompt = "\nEnter the max number to be used : "
    time_prompt = "\nEnter the max time (minutes) for the exercise: "
    print "\nWelcome to Algebra Exercise!\n\nExercise types:"
    printplus(get_type_descs())
    type = raw_input(type_prompt % sorted(TYPES.keys()))
    max_int = raw_input(int_prompt)
    max_time = raw_input(time_prompt)
    max_time = int(max_time) * 60
    #print "%s %s %s" % (type, max_int, max_time)
 

def generate_problem():
    #print "%s %s %s" % (type, max_int, max_time)
    global solved, error
    x = random.randint(0,int(max_int))
    y = random.randint(0,int(max_int))

    # no negative numbers yet
    if type in ['2', '4'] and x < y:
        # swap
        t = x
        x = y
        y = t

    ans = TYPES[type][1](x,y)
    problem = "%s %s %s = " % (x, TYPES[type][2], y)
    a = raw_input(problem)
    # typo
    if not a.isdigit():
        print "I/O Error: a number expected!\n"
        return 
    if ans == int(a):
        print "CORRECT!\n"
        solved += 1 
    else:
        print "WRONG! Correct answer is: %s\n" % ans
        error += 1
    return


def countdown(t):
    while t >= 0:
        time.sleep(1)
        t -= 1


def timer_loop():
    global max_time, total
    raw_input ("\nHIT ENTER TO START!")

    #TODO: Thread
    #t = threading.Thread(target=countdown, args=max_time)
    #t.daemon = True
    #t.start()

    start = time.time()
    while (time.time() - start <= int(max_time)):
        generate_problem()
        total += 1


def post_result():
    global total, solved, error
    print "\n\nTime is up!!!!"
    print "\nTotal problems %s, correct: %s, wrong: %s.\n\n" %\
        (total, solved, error)


def run_exercise():
    get_input_params()
    timer_loop()
    post_result()


if __name__ == '__main__':
    run_exercise()
