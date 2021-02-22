# Storage Parameters
start = [0, 0, 0,0,0,0]
currentState = [];
vistied = [];
comeFrom = [];
Goal= [2,2,2,2,2,2]
# ----------------------------------------------------------------------------------------
#def main(start,Goal):
def main():# new main
    print('test');
    c=0
    # Initial start parameters.
    run_Program = True;
    currentState.append(start);
    # General Loop that run the program.
    while run_Program == True:
        c=c+1
        # Checking if the goal state is reacht or not
       
        
        
        # Sparar de nya placeringar
        currentState.extend(New_state(currentState[0]))#utgå ifrån den som står först i currentState
        vistied.append(currentState[0])#sparar den som vi besökte
        comeFrom.append(the_way_to_go(vistied[len(vistied)-1],New_state(vistied[len(vistied)-1])))
        

        # Tar bort överlapande som annars ställer till problem
        n=0
        i=0
        while(i<len(vistied)):#går igenom vistied som öka varje gång vi har gått igrnom CurrentState
            if n>= len(currentState):
                i=i+1
                n=0
            elif vistied[i]==currentState[n]:#ifall vi hittar två lika så tas den bort ifrån currentState
                del currentState[n]
            else:
                n=n+1


                
        #if check_Goal(currentState[0],Goal) == False:
            #print()
            #comeFrom.append(currentState);
        if check_Goal(vistied[len (vistied)-1],Goal) == True:
            print('GOAL!!!!!');
            run_Program = False;
            #return comeFrom
            #return vistied
            print(c-1)
            print(find_your_way_home(comeFrom))
        
            break
     
# ----------------------------------------------------------------------------------------
def New_state(state):#tar fram alla möjliga sätt man kan flytta diskarna på
    New=[state.copy()]#kopierar State så den ej ändras
    Disk_place = []
    for i in range(0,len(state)):
        A =  check_disk(state,i)#kollar vilka diskar som går o flytta på
        if A == True:#om platsen är flytbar gör dådetta
            Disk_place.extend([i])#lagra platsen som är flyttbar  
    for i in range(len(Disk_place)):#kollar om man kan lägga de flytbara diskarna någonstans samt flyttar på dem
        New[0]=state.copy()
        New.append( Move_disk_one_step(New[0],Disk_place,i))#flyttar diskarna ett steg åt "höger"
        New[0]=state.copy()
        New.append( Move_disk_two_step(New[0],Disk_place,i))#flyttar diskarna två steg åt "höger"
        
    while New.count(None)!=0:#tar bort alla None värden
            New.remove(None)
            
        
    del New[0]# tar bort det första värdet
     
    return New
# ----------------------------------------------------------------------------------------

def Move_disk_one_step(state,Disk_place,i):
    a=[]
    state[Disk_place[i]] = (state[Disk_place[i]]+1)%3
    if check_disk(state,Disk_place[i])== True:
        a.extend(state)
        return a
# ----------------------------------------------------------------------------------------
def Move_disk_two_step(state,Disk_place,i):
    a=[]
    state[Disk_place[i]] = (state[Disk_place[i]]+2)%3
    if check_disk(state,Disk_place[i])== True:
        a.extend(state)
        return a
# ----------------------------------------------------------------------------------------
def check_disk(state,i):

   
    x=1
    if i==len(state)-1:
        return True
    for n in range (i,len(state)-1):                    
        if state[i]==state[n+1]:
            x=0
    if x==0:
        return False
    if x==1 :
        return True

# ----------------------------------------------------------------------------------------
def check_Goal(state,Goal):
    # check if the goal state is reacht.
    if state == Goal:
        return True;
    else:
        return False;
        
# ----------------------------------------------------------------------------------------
def the_way_to_go(vistied,currentState):
    #print(vistied,currentState)
    comeFrom=[currentState,vistied]
    return comeFrom    
#-----------------------------------------------------------------------------------
def find_your_way_home(comeFrom):
    way_home=[Goal.copy()]
    i=0
    n=0
    while(way_home[-1:]!=[start]):
        #print(way_home[-1:])
        #print([comeFrom[i][0][n]])
        #print(i,n)
        if [comeFrom[i][0][n]]==way_home[-1:]:
            way_home.append( comeFrom[i][-1])
        
            i=0
            n=0
        elif n>=len(comeFrom[i][0])-1:
            i=i+1
            n=0
        else:
            n=n+1
    return way_home
    
            
    
    
