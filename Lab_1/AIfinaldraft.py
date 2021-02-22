# Authurs: Joachim Johnson and Jonas Åsander
# Course: DT112G, artifical intelegens
# Task 1: Tower of Hanoi Problem

# Storage Parameters
numbofdisks = 6
start = [0] * numbofdisks                                      # Start value.
goal = [2] * numbofdisks                                       # Goal state to reach.


''' ---------------------------------------------------------------------------------------------------------------- '''


def Main():
    # Initial start parameters.
    # Nollställer vektorena om man ska köra den en gång till
    currentState = []
    vistied = []                                               # All visited states.
    comeFrom = []
    run_Program = True
    currentState.append(start)

    # Loop values.
    c = 0
   
    while run_Program == True: # General Loop that run the program.
        # Checking if the goal state is reacht or not
        c +=1

        # Sparar de nya placeringar
        currentState.extend(New_state(currentState[0]))        # Utgå ifrån den som står först i currentState.
        vistied.append(currentState[0])                        # Sparar den som vi besökte.
        # currentState.reverse()                               # Aktivate if you want deep search othewise it breath search.
        comeFrom.append(The_Way_To_Go(vistied[len(vistied) - 1], New_state(vistied[len(vistied) - 1])))

        
        # Tar bort överlapande som annars ställer till problem
        n = 0                                                  # NOLLSTÄLLER INFÖR LOOPEN
        i = 0
        while (i < len(vistied)):                              # Går igenom vistied som öka varje gång vi har gått igrnom CurrentState.
            if n >= len(currentState):
                i = i + 1
                n = 0
            elif vistied[i] == currentState[n]:                # Ifall vi hittar två lika så tas den bort ifrån currentState.
                del currentState[n]
            else:
                n += 1

        if Check_Goal(vistied[len(vistied) - 1], goal) == True:
            run_Program = False
            A=PrintoutGoalValues(c,comeFrom)
            A.reverse()
            return A
            break


''' ---------------------------------------------------------------------------------------------------------------- '''


def New_state(state):                                          # Tar fram alla möjliga sätt man kan flytta diskarna på
    New = [state.copy()]
                                                               # Kopierar State så den ej ändras
    Disk_place = []
    for i in range(0, len(state)):
        A = Check_Disk(state, i)                               # Kollar vilka diskar som går o flytta på.
        if A == True:                                          # Om platsen är flytbar gör då detta.
            Disk_place.extend([i])                             # Lagra platsen som är flyttbar.

    for i in range(len(Disk_place)):                           # Kollar om man kan lägga de flytbara diskarna någonstans samt flyttar på dem.
        New[0] = state.copy()
        New.append(Move_disk_one_step(New[0], Disk_place, i))  # Flyttar diskarna ett steg åt "höger".
        New[0] = state.copy()
        New.append(Move_disk_two_step(New[0], Disk_place, i))  # Flyttar diskarna två steg åt "höger".

    New = NoneRemover(New)                                     # Tar bort alla None värden.

    del New[0]                                                 # Tar bort det första värdet.
    return New


''' ---------------------------------------------------------------------------------------------------------------- '''


def Move_disk_one_step(state, Disk_place, i):
    a = []
    state[Disk_place[i]] = (state[Disk_place[i]] + 1) % 3
    if Check_Disk(state, Disk_place[i]) == True:
        a.extend(state)
        return a


''' ---------------------------------------------------------------------------------------------------------------- '''


def Move_disk_two_step(state, Disk_place, i):
    a = []

    state[Disk_place[i]] = (state[Disk_place[i]] + 2) % 3
    if Check_Disk(state, Disk_place[i]) == True:
        a.extend(state)
        return a


''' ---------------------------------------------------------------------------------------------------------------- '''


def Check_Disk(state, i):
    returnvalue = True

    if i == len(state) - 1:
        return True
    for n in range(i, len(state) - 1):
        if state[i] == state[n + 1]:
            returnvalue = False

    return returnvalue


''' ---------------------------------------------------------------------------------------------------------------- '''


def Check_Goal(state, goal):  # Check if the goal state is reacht.
    if state == goal:
        return True

    else:
        return False


''' ---------------------------------------------------------------------------------------------------------------- '''


def The_Way_To_Go(vistied, currentState):
    comeFrom = [currentState, vistied]
    return comeFrom


''' ---------------------------------------------------------------------------------------------------------------- '''


def Find_Way_Home(comeFrom):
    way_home = [goal.copy()]
    i = 0
    n = 0
    while (way_home[-1:] != [start]):
        if [comeFrom[i][0][n]] == way_home[-1:]:
            way_home.append(comeFrom[i][-1])

            i = 0
            n = 0

        elif n >= len(comeFrom[i][0]) - 1:
            i += 1
            n = 0

        else:
            n +=1
    return way_home


''' ---------------------------------------------------------------------------------------------------------------- '''


def NoneRemover(state):             # Tar bort alla None värden.
    while state.count(None) != 0:
        state.remove(None)

    return state


''' ---------------------------------------------------------------------------------------------------------------- '''


def PrintoutGoalValues(c,comeFrom):
    print('startvalues: ' + start + ' has been reacht and ended the search')
    print('Number of calculations: ',c - 1)
    return(Find_Way_Home(comeFrom))


