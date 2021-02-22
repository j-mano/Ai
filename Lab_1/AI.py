# Storage Parameters
start = [0] * 3                                       # Start value.
goal = [2] * 3                                        # Goal state to reach.


''' ---------------------------------------------------------------------------------------------------------------- '''


def Main():
    # Initial start parameters.
    # Nollställer vektorena om man ska köra den en gång till
    currentState = []
    vistied = []                                                 # All visited states.
    comeFrom = []
    run_Program = True
    currentState.append(start)
    c = 0

    while run_Program == True: # General Loop that run the program.
        # Checking if the goal state is reacht or not
        c = c + 1

        # Sparar de nya placeringar
        currentState.extend(New_state(currentState[0]))        # Utgå ifrån den som står först i currentState.
        vistied.append(currentState[0])                        # Sparar den som vi besökte.
        #currentState.reverse()
        comeFrom.append(The_Way_To_Go(vistied[len(vistied) - 1], New_state(vistied[len(vistied) - 1])))

        # Tar bort överlapande som annars ställer till problem
        n = 0                                                  # NOLLSTÄLLER INFÖR LOOPEN
        i = 0
        while (i < len(vistied)):                              # Går igenom vistied som öka varje
            if n >= len(currentState):                         # gång vi har gått igrnom CurrentState.
                i += 1
                n = 0
            elif vistied[i] == currentState[n]:                # Ifall vi hittar två lika så tas den bort ifrån currentState.
                del currentState[n]
            else:
                n += 1

        if Check_Goal(vistied[len(vistied) - 1], goal) == True:
            run_Program = False
            A=PrintoutGoalValues(c, comeFrom)
            return A
            break


''' ---------------------------------------------------------------------------------------------------------------- '''


def New_state(state):                                          # Tar fram alla möjliga sätt man kan flytta diskarna på
    New = [state.copy()]                                       # Kopierar State så den ej ändras
    Disk_place = []
    for i in range(0, len(state)):
        A = Check_Disk(state, i)                               # Kollar vilka diskar som går o flytta på.
        if A == True:                                          # Om platsen är flytbar gör då detta.
            Disk_place.extend([i])                             # Lagra platsen som är flyttbar.

    for i in range(len(Disk_place)):                           # Kollar om man kan lägga de flytbara diskarna någonstans samt flyttar på dem.
        New[0] = state.copy()
        New.append(Move_disk_one_step(New[0], Disk_place, i))  # Flyttar diskarna ett steg åt "höger".
        # New[0] = state.copy()
        # New.append(Move_disk_two_step(New[0], Disk_place, i))  # Flyttar diskarna två steg åt "höger".

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


def Move_disk_two_step(state, Disk_Place, i):
    a = []

    state[Disk_Place[i]] = (state[Disk_Place[i]] + 2) % 3
    if Check_Disk(state, Disk_Place[i]) == True:
        a.extend(state)
        return a


''' ---------------------------------------------------------------------------------------------------------------- '''


def Check_Disk(state, i):
    returnValue = True

    if i == len(state) - 1:
        return True
    for n in range(i, len(state) - 1):
        if state[i] == state[n + 1]:
            returnValue = False

    return returnValue


''' ---------------------------------------------------------------------------------------------------------------- '''


def Check_Goal(state, goal):  # Check if the goal state is reacht.
    if state == goal:
        return True
    elif state != goal:
        return False
    else:
        return False
        print('Ett fel har uppståt')  # If it isnt posseble to match the 2 parameters will it end upp here.


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
            i = i + 1
            n = 0

        else:
            n = n + 1
    return way_home


''' ---------------------------------------------------------------------------------------------------------------- '''


def NoneRemover(state):                 # Tar bort alla None värden.
    while state.count(None) != 0:
        state.remove(None)

    return state


''' ---------------------------------------------------------------------------------------------------------------- '''


def PrintoutGoalValues(c,comeFrom):
    print('Måltillståndet', goal,' har blivit uppfyllt')
    print('Antal uträkningar:', c - 1)
    return(Find_Way_Home(comeFrom))     # Revers?

