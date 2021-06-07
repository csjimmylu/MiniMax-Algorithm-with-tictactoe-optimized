import random

def minimax_algorithm(ub): # should return a pos, such as 4, not index[1,1]
    optimal = 0
    options = []
    redundant_optimal = [] # This adds the random feature for the computer decision.
    for i in range(len(ub)):
        for j in range(len(ub[i])):
            if ub[i][j] != 'X' and ub[i][j] != 'O':
                # NOTE uboard[i][j's 0 is position, 1 is maxval, 2 is minval
                if ub[i][j][1] >= 10:
                    return ub[i][j][0]
                elif ub[i][j][2] <= -10:
                    return ub[i][j][0]
                else:
                    if abs(ub[i][j][1]) == abs(ub[i][j][2]):
                        # NOTE if abs of max = abs of min, add 1 to their sum. Why? because we want to win more more than limiting the enemy
                        options.append([abs(ub[i][j][1]) + abs(ub[i][j][2])+1, ub[i][j][0]])
                    else: # NOTE, [0] is the total val of abs(max + min). [1] is the index
                        options.append([abs(ub[i][j][1]) + abs(ub[i][j][2]), ub[i][j][0]])

    optimal = max(options) # NOTE for redundant_optimal, [0] is index, [1] is val
    for i in range(len(options)):
        if options[i][0] == optimal[0]:
            redundant_optimal.append(options[i][1])

    redundant_optimal.append(optimal[1])
    randnum = random.randint(0,len(redundant_optimal)-1)
    return redundant_optimal[randnum]