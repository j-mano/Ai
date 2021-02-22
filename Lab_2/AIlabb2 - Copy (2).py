# FileInfo:
# Students/Devs: Jonas Åsander and Joachim Johnson
# Course: DT112

# Imports / Extra modules
import csv                                                                                                              # Save/Load files module
from pathlib import Path                                                                                                # Filechecking


''' ---------------------------------------------------------------------------------------------------------------- '''


class resturantsClass():
    def __init__(self):                                                                                                 # Def of class
        self.Name           = 'undifiende'
        self.Type           = 'undifiende'
        self.Nationality    = 'undifiende'
        self.Quality        = 'undifiende'
        self.PriceClass     = 'undifiende'
        self.DistansUni     = 'undifiende'

    def ADD_this(self):                                                                                                 # For manual input
        self.Name           = input('Name?')
        self.Type           = input('Type?')
        self.Nationality    = input('Nationality?')
        self.Quality        = input('Quality?')
        self.PriceClass     = input('PriceClass?')
        self.DistansUni     = input('Distans to university?')

    def ADD_this2(self, inputt):                                                                                        # Input from an dict/file
        self.Name           = inputt[0]
        self.Type           = inputt[1]
        self.Nationality    = inputt[2]
        self.Quality        = inputt[3]
        self.PriceClass     = inputt[4]
        self.DistansUni     = inputt[5]


''' ---------------------------------------------------------------------------------------------------------------- '''

# Storage Parameters
'''
    similarity is the liknes of the resturant to each other.
    0 = absolut no simularities. 1 everything matches.
'''

resturants = []


''' ---------------------------------------------------------------------------------------------------------------- '''


def main():                                                                                                             # Start of the program
    MainLoadedFile = 0
    Load = 0

    if ifSaveFileexist() == True:                                                                                       # If file exist loads it
        openFile()
        print('Resturants loaded')
        Load += 1
        MainLoadedFile += 1
        meny(Load, MainLoadedFile)
    elif ifSaveFileexist() == False:                                                                                    # If not ignore to load anything
        print('SaveFile not found')
        meny(Load, MainLoadedFile)
    else:
        print('Loading error!? /n Closing down')                                                                        # If somthing realy weird happens


''' ---------------------------------------------------------------------------------------------------------------- '''


def ifSaveFileexist():
    saveFileCheck = Path("SaveFile.csv")                                                                                # Checks if savefile exist
    if saveFileCheck.is_file():
        return True
    else:
        return False


''' ---------------------------------------------------------------------------------------------------------------- '''


def meny(Load, MainLoadedFile):

    menyChoiceNumber = 1
    while menyChoiceNumber != 0:
        menyChoiceNumber = the_Meny()

        if menyChoiceNumber == '1':                                                                                     # Add to class resturants
            addResturantToClass()

        elif menyChoiceNumber == '2':                                                                                   # Compare 2 resturants
            similarity()

        elif menyChoiceNumber == '3':                                                                                   # Delete resurant
            print('Enter Password:')                                                                                    # Password protected. "Very simple password protection"
            Password()

        elif menyChoiceNumber == '4':                                                                                   # Load from file/planed to only be uset once per programrun
            if Load == 0:
                openFile()
                Load += 1
            else:
                print('File alredy loaded')

        elif menyChoiceNumber == '5':                                                                                   # Save to file
            saveFile()
            if MainLoadedFile == 0:                                                                                     # For Not making dubblets
                Load = 1

        elif menyChoiceNumber == '6':                                                                                   # Search suiteble resturant
            search()

        elif menyChoiceNumber == '9':                                                                                   # Print out classvalues / resturants that are stored in program
            if resturants:
                printOutResturant()
            else:
                print('The program are empty')

        elif menyChoiceNumber == '0':
            print('Closing down, Good bye')
            break

        else:
            print('you input is not accapted, please try again')                                                        # Everything else than number 0-6 and 9 are invalid input.


''' Meny ------------------------------------------------------------------------------------------------------------'''


def the_Meny():
    print()
    print('1. Add resturant in class,'
          '\n2. Compare two existing resturants             \n'
          '3. Delete \n4. Load from file to resturant class \n'
          '5. Save stored resturants class                  \n'
          '6. Search suiteble resturant                     \n'
          '9. Print out all stored values                   \n'
          '0. Quit')
    print()
    menyChoiceNumber = input()
    return menyChoiceNumber


''' MenyChoiceNumber == 1: ----------------------------------------------------------------------------------------- '''


def addResturantToClass():
    resturants.append(resturantsClass())
    resturants[len(resturants) - 1].ADD_this()
    print('\nResturant added')


'''----------------------------------------------------------------------------------------------------------------- '''


def add_Resturants():
    resturant = [resturants() for x in range(0, 20)]


''' MenyChoiceNumber == 2:------------------------------------------------------------------------------------------ '''


def similarity():                                                                                                       # Simularity cheking of 2 resturants
    if resturants == []:                                                                                                # If it is no resturant in the program
        print('There is no spoon, Neo')
        return
    print('Which resturants do you wish to compare?')
    i = input()
    n = input()
    I = checkName(i)
    N = checkName(n)

    if I == None:                                                                                                       # Vilket den avbryter om den ena av de returnerade är blanka
        print('no resturant whit that name:', i)                                                                        # Vilket gör att den första bör vara blank
        return
    elif N == None:
        print('no resturant whit that name:', n)
        return
    elif N == I:
        print('this is the same resturant')
        return

    resturantOne = resturantsInfo(I)                                                                                    # Kollar om man hittar namnet bland de olika resturangerna / checking if you could find the name among the resturants.
    resturantTwo = resturantsInfo(N)                                                                                    # Om inte så returnerar den den första resturangen / If no value is return from the first one.

    sim = 0
    for i in range(0, len(resturantOne)):                                                                               # Loopar igenom de två valda resturangerna och jämnför de två olika / looping thourge the 2 choschen values and compaire them
        if resturantOne[i] == resturantTwo[i]:                                                                          # If they have somthing in common

            sim += 1
    similar = sim / len(resturantTwo)                                                                                   # Take the sum of all simularites and diveds it by number of strngs

    print(resturantOne, resturantTwo, 'is similar to', similar * 100, '%')


''' ---------------------------------------------------------------------------------------------------------------- '''


def resturantsInfo(i):
    returingRestValue = (resturants[i].Name,
         resturants[i].Type,
         resturants[i].Nationality,
         resturants[i].Quality,
         resturants[i].PriceClass,
         resturants[i].DistansUni)
    return returingRestValue


''' ---------------------------------------------------------------------------------------------------------------- '''


def checkName(inname):
    outname = 0
    for Rest in resturants:

        if inname == Rest.Name:
            return outname
        outname += 1
    return


''' MenyChoiceNumber == 3:------------------------------------------------------------------------------------------ '''


def Password():                                                                                                         # Passwordfunction. uset for delete function
    password = input()
    if password == '1234':                                                                                              # Hardcoded password 1234
        Delete()
    else:
        print('Wrong input')
        return


def Delete():
    if resturants == []:                                                                                                # Cheking if there are resturants to delete
        print('There is no resturants')
        return

    print('Which resturants do you wish to delete?')                                                                    # Which restorant to delete
    i = input()
    del resturants[checkName(i)]


''' MenyChoiceNumber == '4':---------------------------------------------------------------------------------------- '''


def openFile():
    if ifSaveFileexist() == True:                                                                                       # If file exist loads it
        with open('SaveFile.csv', newline='') as csvfile:
            readFile = csv.reader(csvfile, delimiter=' ', quotechar='|')

            for row in readFile:                                                                                        # Loping thoure all values in savefile
                if row:
                    valuesFromFile = row                                                                                # Indevidual value from the file
                    if valuesFromFile != ['Name', 'Type', 'Nationality', 'Quality', 'PriceClass', 'DistansUni']:        # Header remover
                        resturants.append(resturantsClass())                                                            # Puts it into class/program
                        resturants[len(resturants) - 1].ADD_this2(valuesFromFile)
                else:
                    print('File empty')
            csvfile.close();

    elif ifSaveFileexist() == False:                                                                                    # If not ignore to load anything
        print('Loading error \n SaveFile not found \n returning to meny')

    else:
        print('Critical Loading error!?')


''' MenyChoiceNumber == '5':---------------------------------------------------------------------------------------- '''


def saveFile():
    if resturants:
        with open('SaveFile.csv', 'w', newline='') as csvfile:                                                          # Open/Create file with name SaveFile.csv
            writToFile = csv.writer(csvfile, delimiter=' ',                                                             # Savefile name = SaveFile.csv
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            Header = ['Name', 'Type', 'Nationality', 'Quality', 'PriceClass', 'DistansUni']
            writToFile.writerow(Header)                                                                                 # HeaderLines Is removed again in openfile

            print('Sucessfuly open savefile')
            for Rest in resturants:
                temp = [Rest.Name, Rest.Type, Rest.Nationality, Rest.Quality, Rest.PriceClass,
                        Rest.DistansUni]                                                                                # Inserlist for file
                writToFile.writerow(temp)
    else:
        print('Nothing to save.')


''' MenyChoiceNumber == '6': --------------------------------------------------------------------------------------- '''


def search():
    print('Please enter some values of the resturant you would like to go')                                             # Function that compare a new value to stored value in class

    inputClass = resturantsClass

    inputClass.Type         = input('Enter what type of resturant: ')
    inputClass.Nationality  = input('Enter what nationality of the resturant: ')
    inputClass.Quality      = input('Enter what quality of the resturant: ')
    inputClass.PriceClass   = input('Enter what price type of the resturant (High,Mid,Low): ')
    inputClass.DistansUni   = input('Enter what distans from the university (in km): ')
    Return_score = []

    for e in resturants:
        score = 0
        if e.Type           == inputClass.Type:
            score += 1
        if e.Nationality    == inputClass.Nationality:
            score += 1
        if e.Quality        == inputClass.Quality:
            score += 1
        if e.PriceClass     == inputClass.PriceClass:
            score += 1
        if e.DistansUni     == inputClass.DistansUni:
            score += 1
        Return_score.append(score)
   # print(Return_score)

    for i in range(0, len(Return_score)):
        if max(Return_score) == Return_score[i]:
            print(resturants[i].Name + ' Is Moust simular to youre request')


''' MenyChoiceNumber == 9: ----------------------------------------------------------------------------------------- '''


def printOutResturant():                                                                                                # Prints out all values stored in the class
    for Rest in resturants:
        print('Name:', Rest.Name,
              'Type:', Rest.Type,
              'Nationality:', Rest.Nationality,
              'PriceClass:', Rest.PriceClass,
              'Quality:', Rest.Quality,
              'Distans To University:', Rest.DistansUni)

