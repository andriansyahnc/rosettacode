import random

def swap(d, emptyidx, myinput):
    input_idx = checkindex(d, myinput)
    d[emptyidx] = myinput
    d[input_idx] = ''

def checkindex(d, val):
    for a in d:
        if(str(d[a]) == str(val)):
            return a


def checkmove(d, emptyidx, myinput):
    is_continue = False
    input_idx = checkindex(d, myinput)

    empty_floor = emptyidx // 4
    empty_mod = emptyidx % 4
    input_floor = input_idx // 4
    input_mod = input_idx % 4

    if empty_mod == input_mod and (input_floor == empty_floor + 1 or input_floor == empty_floor - 1):
        is_continue = True
    elif input_idx == emptyidx + 1 and empty_mod != 0:
        is_continue = True
    elif input_idx == emptyidx - 1 and empty_mod != 1:
        is_continue = True

    return is_continue


def checkinput(d, myinput):
    emptyidx = checkindex(d, '')
    is_continue = checkmove(d, emptyidx, myinput)
    if is_continue == True:
        swap(d, emptyidx, myinput)
        print("")
    else:
        print("Input is not valid, try again")

def cs(val):
    if val == '':
        return '  '
    return val if len(str(val)) == 2 else " " + str(val)


def checkdict(d):
    for x in range(1, 15):
        if x != d[x]:
            return False
    return True


def play(d):
    while checkdict(d) == False:
        print("To play, what you need to do is input the number you want to move.")
        myinput = input("Number you want to move: ")
        print("\033[H\033[J")
        checkinput(d, myinput)
        frame(d)
    print("Congratulations, You Win")


def frame(d):
    print('---------------------')
    print('| %s | %s | %s | %s |' % (cs(d[1]), cs(d[2]), cs(d[3]), cs(d[4])))
    print('---------------------')
    print('| %s | %s | %s | %s |' % (cs(d[5]), cs(d[6]), cs(d[7]), cs(d[8])))
    print('---------------------')
    print('| %s | %s | %s | %s |' %
          (cs(d[9]), cs(d[10]), cs(d[11]), cs(d[12])))
    print('---------------------')
    print('| %s | %s | %s | %s |' %
          (cs(d[13]), cs(d[14]), cs(d[15]), cs(d[16])))
    print('---------------------')


def puzzle():
    d = {}
    val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, '']
    random.shuffle(val)
    for idx in range(1, len(val) + 1):
        d[idx] = val[idx - 1]
    frame(d)
    play(d)


if __name__ == "__main__":
    puzzle()
