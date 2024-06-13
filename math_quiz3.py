#
# Copyright (c) 2021, CMW
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or any later ver24
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#

import operator
import random
import time

TYPES = {
         '1':('addition', operator.add, '+'),
         '2':('subtraction', operator.sub, '-'),
         '3':('multiplication', operator.mul, 'x'),
         '4':('division', operator.truediv, '/')
        }

OPS = {'1':operator.add,
       '2':operator.sub,
       '3':operator.mul,
       '4':operator.truediv}

type = max_int = max_time = "None"
index = total = solved = error = 0


def printplus(obj):
    # dict
    if isinstance(obj, dict):
        for k, v in sorted(obj.items()):
            print(u'{0}: {1}'.format(k, v))
    # list or tuple
    elif isinstance(obj, list) or isinstance(obj, tuple):
        for x in obj:
            print(x)
    # other
    else:
        print(obj)


def get_type_descs():
    d = {}
    for k,v in TYPES.items():
        d[k] = v[0]
    return d


def reset_globals():
    global type, max_int, max_time, index, solved, error, total
    type = max_int = max_time = "None"
    total = solved = error = 0
    index = 1


def get_input_params():
    global type, max_int, max_time
    type_prompt = "Select exercise type %s : "
    int_prompt = "\nEnter the max round (integer) number to be used : "
    time_prompt = "\nEnter the max time (minutes) for the exercise: "
    print("\nMathQuiz Algebra Exercise\n")
    while type not in ['1', '2', '3', '4']:
        print("\nExercise types:")
        printplus(get_type_descs())
        type = input(type_prompt % sorted(TYPES.keys()))

    while not max_int.isdigit():
        max_int = input(int_prompt)

    while not max_time.isdigit():
        max_time = input(time_prompt)

    max_time = int(max_time) * 60
    #print "%s %s %s" % (type, max_int, max_time)


def generate_problem():
    #print "%s %s %s" % (type, max_int, max_time)
    global index, solved, error, total
    x = random.randint(0,int(max_int))
    y = random.randint(0,int(max_int))

    # no negative numbers yet
    if type in ['2', '4'] and x < y:
        # swap
        t = x
        x = y
        y = t

    ans = TYPES[type][1](x,y)
    problem = "     %s) %s %s %s = " % (index, x, TYPES[type][2], y)
    index += 1
    a = input(problem)
    if not a.isdigit():
        print("     I/O Error! A number is expected.\n")
        return
    total += 1
    if ans == int(a):
        print("     CORRECT!\n")
        solved += 1
    else:
        print("     WRONG! The correct answer is %s.\n" % ans)
        error += 1


def countdown(t):
    while t >= 0:
        time.sleep(1)
        t -= 1


def timer_loop():
    global max_time
    input("\n     HIT ENTER TO START!")

    #TODO: Thread
    #t = threading.Thread(target=countdown, args=max_time)
    #t.daemon = True
    #t.start()

    start = time.time()
    while (time.time() - start <= int(max_time)):
        generate_problem()


def post_result():
    global total, solved, error
    print("\n\nTime is up!!!!")
    print("\nTotal problems attempted: %s, correct: %s, wrong: %s.\n\n" % (total, solved, error))


def run_exercise():
    start = True
    while start:
        a = None
        reset_globals()
        get_input_params()
        timer_loop()
        post_result()

        while a not in ['y', 'Y', 'n', 'N', '']:
            a = input("Want to retry and improve your skills? [Y]/N: ")
            if a in ['n', 'N']:
                finish()
                return
            elif a in ['y', 'Y', '']:
                start = True


def finish():
    print("\nThank you for using MathQuiz!")
    print("Copyright (c) 2021, CMW - GNU Public License\n\n")


if __name__ == '__main__':
    run_exercise()
