# FileInfo:
# Students/Devs: Jonas Åsander and Joachim Johnson
# Course: DT112
# Task 3 - Lab/Task 3 - Clustering

# Imports / Extra modules
import csv                                                                                                              # Save/Load files module
from pathlib import Path                                                                                                # Filechecking
import random                                                                                                           # Random number

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
        self.Type           = input('Type? (Pizza, Fastfood, Asian, Cafe, Traditional, Steakhouse)')
        self.Nationality    = input('Nationality? (Swedish, Italian, Amarican, German, Asian, French)')
        self.Quality        = input('Quality? (Low,Mid,High)')
        self.PriceClass     = input('PriceClass? (Low,Mid,High)')
        self.DistansUni     = input('Distans to university? (0-100 no string values)')

    def ADD_this2(self, inputt):                                                                                        # Input from an dict/file
        self.Name           = inputt[0]
        self.Type           = inputt[1]
        self.Nationality    = inputt[2]
        self.Quality        = inputt[3]
        self.PriceClass     = inputt[4]
        self.DistansUni     = inputt[5]

class validValues():
    validTypes              = ['Pizza', 'Fastfood', 'Asian', 'Cafe', 'Traditional', 'Steakhouse']
    validNationalities      = ['Swedish', 'Italian', 'Amarican', 'German', 'Asian', 'French']
    validQualityPrices      = ['Low', 'Mid', 'High']

class clustring():
    AvgValue                = []                                                                                        # Centeroid.
    containingCases         = []                                                                                        # Where all classes

    def numbofcasses(self):
        i = 0

        for rest in self.containingCases:
            i += 1

        print(i)

    def addcasse(self, inputt):
        self.containingCases.append(inputt)

    def printout_cluster(self):
        numb_of_clusters = 0
        numb_of_resturants = 0
        for resturantes in self.containingCases:
            numb_of_clusters += 1
            print(numb_of_clusters)
            for e in resturantes:
                numb_of_resturants += 1
                print(numb_of_resturants, e.Name)


''' ---------------------------------------------------------------------------------------------------------------- '''

# Storage Parameter
resturants = []

''' ---------------------------------------------------------------------------------------------------------------- '''
# Some default "checking" functions


def ifSaveFileexist():
    saveFileCheck = Path("SaveFile.csv")                                                                                # Checks if savefile exist
    if saveFileCheck.is_file():
        return True
    else:
        return False


def isNumber(inputValue):                                                                                               # Error Checking to search function
    try:                                                                                                                # Used to validating inputs that they are float values
        float(inputValue)
        return True
    except ValueError:
        return False

def randomindex(numbofclousters):
    randome = random.randrange(numbofclousters + 1)
    return randome


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


def meny(Load, MainLoadedFile):
    menyChoiceNumber = 1
    while menyChoiceNumber != 0:
        menyChoiceNumber = mainMeny()

        if menyChoiceNumber == '1':                                                                                     # Add to class resturants
            addResturantToClass()

        elif menyChoiceNumber == '2':                                                                                   # Compare 2 resturants
            numbofclousters = input('Please enter the number of desierd clusters')

            if isNumber(numbofclousters):
                clusterings(float(numbofclousters))
            else:
                print('Invalid input. Numbers only')

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

        elif menyChoiceNumber == '7':                                                                                   # Validate the class
            print(resturantValidator())
            if resturantValidator() is False:
                print('File is corrupt')
            if resturantValidator() is True:
                print('File is OK')

        elif menyChoiceNumber == '9':                                                                                   # Print out classvalues / resturants that are stored in program
            if resturants:
                printOutResturant()
            else:
                print('The program are empty')

        elif menyChoiceNumber == '0':
            print('Closing down, Good bye and have a nice day')
            break

        else:
            print(
                'you input is not accapted, please try again')                                                          # Everything else than number 0-6 and 9 are invalid input.


''' Meny ------------------------------------------------------------------------------------------------------------'''


def mainMeny():
    print('\n   Main meny <----------------------->')

    print('\n1. Add resturant in class,                     \n'
          '2. Clustering                                    \n'
          '3. Delete                                        \n'
          '4. Load from file to resturant class             \n'
          '5. Save stored resturants class                  \n'
          '6. Search suiteble resturant                     \n'
          '7. validate class                                \n'
          '9. Print out all stored values                   \n'
          '0. Quit                                          \n')

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


''' MenyChoiceNumber == 2: ----------------------------------------------------------------------------------------- '''


def clusterings(numbofclousters):
    if resturantValidator():                                                                                            # The resturant moust pass the validaton test. That it is inside the frame we set upp
        print('Resturants validated.')

        itirations          = 1000
        numb_of_resturants  = 0
        clusters            = []
        initalClusters      = []                                                                                        # To jumpstart with the random values to the loop
        numbofclousters     -= 1                                                                                        # Number of clouster that shoud be created. Take -1 to make it work in an loop thats starts at 0

        tempi = 0
        i = 0
        while tempi <= numbofclousters:                                                                                 # Creating the list of instanses of clouster classes / Creating the number of clousters
            tempi += 1
            initalClusters.append([])
            clusters.append(clustring())

        for res in resturants:
            numb_of_resturants += 1                                                                                     # Takes out the number of returants loaded in the program
            randominde = randomindex(numbofclousters)

            initalClusters[randominde].append(res)                                                                      # Randomly load resturants in the clusters får kolla mer på då den är fel.

        #i = 0
        #while i <= numb_of_resturants:
        #    i += 1
        #    randominde = randomindex(numbofclousters)
        #    clusters[randominde].containingCases.append(resturants[(i-2)])

        tempi = 0
        for actualclusters in clusters:
            tempi += 1
            actualclusters.AvgValue = [AVGCenteroid(initalClusters[tempi - 1])]                                         # Setting first itaration of centerid

        ''' ------------------------------------------------------------------------ '''
        i = 0
        while i <= itirations:                                                                                          # How many times it lopping thoue to final clouster, The cloustering itself
            i += 1

            for clusers in clusters:                                                                                    # Removing all the resturants in the clusters
                clusers.containingCases = []

            for restant in resturants:                                                                                  # Cheking thohe the resturants and reassign them the clusters baset on the last iteration.
                putinindex = compareson(restant, clusters)                                                              # Get the index of wich clouser that are the "closest"

                clusters[putinindex].containingCases.append(restant)                                                    # and append it to the "right clouster"

            for clusers in clusters:                                                                                    # Delete the centeroids
                clusers.AvgValue = []

            for actualclusters in clusters:                                                                             # Append new centeroid based on this iteration
                actualclusters.AvgValue = [AVGCenteroid(actualclusters.containingCases)]
        ''' ------------------------------------------------------------------------ '''

        i = 0
        for actualclusters in clusters:                                                                                 # Printing out the final clousters
            i += 1
            restsinclouster = 0
            for rest in actualclusters.containingCases:                                                                 # Take out the total amount of resturants in clouster
                restsinclouster += 1
            centeroid = []
            for e in actualclusters.AvgValue:
                centeroid = e

            print('\n', 'cluster: ', i, '\n' 
                        '  Number of resturants: ', restsinclouster, 'out of', numb_of_resturants, '\n',
                        ' Centeroid: Name:' + centeroid.Name, 'Type: ' + centeroid.Type,
                        'Natonality: ' + centeroid.Nationality,
                        'Quality: ' + centeroid.Quality,
                        'Priceclass: ' + centeroid.PriceClass,
                        'Distans to university: ', centeroid.DistansUni,
                  '\n  Resturants in cluster: \n')
            for rest in actualclusters.containingCases:
                print('      ', rest.Name, rest.Type)
    else:
        print('There is no resturants loaded')

def AVGCenteroid(containingCases):
    centeroid = resturantsClass()                                                                                       # Make it an resturant case to add in the

    NumOfResturants = 0
    tempdistans     = 0.0
    Qulityi         = 0
    Priceclassi     = 0
    Nationalityi    = 0
    Typei           = 0

    for row in containingCases:                                                                                         # Reading of the input case for loop
        NumOfResturants = NumOfResturants + 1

        if row.Nationality   == 'Swedish':                                                                              # Nationality
            Nationalityi += 0                                                                                           # Give numbers to the "symbolic" values
        elif row.Nationality == 'Italian':
            Nationalityi += 1
        elif row.Nationality == 'Amarican':
            Nationalityi += 2
        elif row.Nationality == 'German':
            Nationalityi += 3
        elif row.Nationality == 'Asian':
            Nationalityi += 4
        elif row.Nationality == 'French':
            Nationalityi += 5

        if row.Type   == 'Pizza':                                                                                       # Type
            Typei += 0                                                                                                  # Give numbers to the "symbolic" values
        elif row.Type == 'Fastfood':
            Typei += 1
        elif row.Type == 'Asian':
            Typei += 2
        elif row.Type == 'Cafe':
            Typei += 3
        elif row.Type == 'Traditional':
            Typei += 4
        elif row.Type == 'Steakhouse':
            Typei += 5

        if row.Quality   == 'High':                                                                                     # Quality
            Qulityi += 3                                                                                                # Give numbers to the "symbolic" values
        elif row.Quality == 'Mid':
            Qulityi += 2
        elif row.Quality == 'Low':
            Qulityi += 1

        if row.PriceClass == 'High':                                                                                    # Priceclass
            Priceclassi += 3                                                                                            # Give numbers to the "symbolic" values
        elif row.PriceClass == 'Mid':
            Priceclassi += 2
        elif row.PriceClass == 'Low':
            Priceclassi += 1

        tempdistans = tempdistans + float(row.DistansUni)                                                               # Distans to university. Add to a big number and devided by all resturant and put in centeroid.

    if Qulityi != 0:
        Qulityi = Qulityi / NumOfResturants

    if Qulityi > 4:                                                                                                     # Avarage of quality
        print('error')
    elif Qulityi > 2.5:
        centeroid.Quality = 'High'                                                                                      # Put back symbolic values based on the values of the input values gave
    elif Qulityi > 1.5:
        centeroid.Quality = 'Mid'
    elif Qulityi >= 0:
        centeroid.Quality = 'Low'

    if Priceclassi != 0:
        Priceclassi = Priceclassi / NumOfResturants

    if Priceclassi > 4:                                                                                                 # Avarage of Price
        print('error')
    elif Priceclassi > 2.5:
        centeroid.PriceClass = 'High'                                                                                   # Put back symbolic values based on the values of the input values gave
    elif Priceclassi > 1.5:
        centeroid.PriceClass = 'Mid'
    elif Priceclassi >= 0:
        centeroid.PriceClass = 'Low'

    if Nationalityi != 0:
        Nationalityi = Nationalityi / NumOfResturants

    if Nationalityi > 7:                                                                                                # avarage of Nationality
        print('error')
    elif Nationalityi > 4.5:
        centeroid.Nationality = 'French'                                                                                # Put back symbolic values based on the values of the input values gave
    elif Nationalityi > 3.5:
        centeroid.Nationality = 'Asian'
    elif Nationalityi > 2.5:
        centeroid.Nationality = 'German'
    elif Nationalityi > 1.5:
        centeroid.Nationality = 'Amarican'
    elif Nationalityi > 0.5:
        centeroid.Nationality = 'Italian'
    elif Nationalityi >= 0:
        centeroid.Nationality = 'Swedish'

    if Typei != 0:
        Typei = Typei / NumOfResturants

    if Typei > 7:                                                                                                       # Avarage of Tpye
        print('error')
    elif Typei > 4.5:
        centeroid.Type = 'Pizza'                                                                                        # Put back symbolic values based on the values of the input values gave
    elif Typei > 3.5:
        centeroid.Type = 'Fastfood'
    elif Typei > 2.5:
        centeroid.Type = 'Asian'
    elif Typei > 1.5:
        centeroid.Type = 'Cafe'
    elif Typei > 0.5:
        centeroid.Type = 'Traditional'
    elif Typei >= 0:
        centeroid.Type = 'Steakhouse'

    centeroid.Name = ('Centeroid')                                                                                      # Dosen't care about the name and give it an random one

    if tempdistans != 0:
        centeroid.DistansUni = tempdistans / NumOfResturants                                                            # Avarge of distans. Devide it by all returants
    else:
        centeroid.DistansUni = 1                                                                                        # Centeroid is vill get to [Name / Centeroid, Type / Steakhouse , Nationality / Swedish , Quality / Low , Priceclass / Low, Distansuni / 0] if nothing is put in

    return centeroid                                                                                                    # Return the calculated centeroid.

def compareson(compareInput, cluster):
    returnScore = []
    referenses = validValues()                                                                                          # "Defult choices" the user can use
    centeroid = []
    numb_Of_Clousters = 0

    for cluser in cluster:
        numb_Of_Clousters += 1
        centeroid.append(cluser.AvgValue)

    i = 0

    for centeroidInfo in centeroid:                                                                                     # Comparing centeroid value to all resturants in database one by one
        for sub_Centeroid_Info in centeroidInfo:
            returningResults = float(comparisonSearch(referenses.validTypes,
                                                      sub_Centeroid_Info.Type, compareInput.Type))
            i += 1
            returningResults = returningResults + \
                               float(comparisonSearch(referenses.validNationalities,
                                                      sub_Centeroid_Info.Nationality, compareInput.Nationality))
            returningResults = returningResults + \
                               float(comparisonSearch2(referenses.validQualityPrices,
                                                       sub_Centeroid_Info.Quality, compareInput.Quality))
            returningResults = float(returningResults +
                                     (comparisonSearch2(referenses.validQualityPrices,
                                                        sub_Centeroid_Info.PriceClass, compareInput.PriceClass)))

            if isNumber(compareInput.DistansUni) == True:
                returningResults = float(returningResults) + comparisonSearchIntValues\
                    (float(sub_Centeroid_Info.DistansUni), float(compareInput.DistansUni))
            elif compareInput.DistansUni == '*':
                returningResults += 1

            returningResults = float(returningResults / 5)
            returnScore.append(returningResults)

    ''' ------------------------------------------------------------------------------------------ '''

    indexing                = 0
    closetcluseterindexing  = 0                                                                                         # Takes out wich cluster it's moust simular to
    temp_higest_numb        = 0

    for returnScorevalues in returnScore:                                                                               # Takes out the higest comparison values and the index of that value and wich cluster it belong to.
        if returnScorevalues > temp_higest_numb:
            temp_higest_numb = returnScorevalues
            closetcluseterindexing = indexing

            indexing += 1

    return closetcluseterindexing                                                                                       # Return the index there it shoud be put in
    # return returnScore;


''' MenyChoiceNumber == 3: ----------------------------------------------------------------------------------------- '''


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
#    del resturants[checkName(i)]


''' MenyChoiceNumber == '4': --------------------------------------------------------------------------------------- '''


def openFile():
    if ifSaveFileexist() == True:                                                                                       # If file exist loads it
        with open('SaveFile.csv', newline='') as csvfile:
            readFile = csv.reader(csvfile, delimiter=' ', quotechar='|')

            for row in readFile:                                                                                        # Loping thoure all values in savefile
                if row:
                    valuesFromFile = row                                                                                # Indevidual value from the file
                    if valuesFromFile != ['Name', 'Type', 'Nationality', 'Quality', 'PriceClass',
                                          'DistansUni']:                                                                # Header remover
                        resturants.append(resturantsClass())                                                            # Puts it into class/program
                        resturants[len(resturants) - 1].ADD_this2(valuesFromFile)
                else:
                    print('Target file is empty')
            csvfile.close();
            if resturantValidator():                                                                                    # Validation of whats loaded
                print('Database is validated')
            else:
                print('Database is corrupt')

    elif ifSaveFileexist() == False:                                                                                    # If not ignore to load anything
        print('Loading error \n SaveFile not found \n returning to meny')

    else:
        print('Critical Loading error!? html errorcode 418 steaming pot')                                               # If somthing unexpected happends


''' MenyChoiceNumber == '5': --------------------------------------------------------------------------------------- '''


def saveFile():                                                                                                         # Save over the alredy existing files/file
    if resturantValidator():
        for row in resturants:
            if row != ['Name', 'Type', 'Nationality', 'Quality', 'PriceClass', 'DistansUni'] \
               and row != ['name', 'type', 'nationality', 'quality', 'priceClass', 'distansUni'] \
               and row != ['Name', 'Type', 'Nationality', 'Quality', 'PriceClass', 'DistansUniversity']:

                with open('SaveFile.csv', 'w', newline='') as csvfile:                                                  # Open/Create file with name SaveFile.csv
                    writToFile = csv.writer(csvfile, delimiter=' ',                                                     # Savefile name = SaveFile.csv
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
                    Header = ['Name', 'Type', 'Nationality', 'Quality', 'PriceClass', 'DistansUni']
                    writToFile.writerow(Header)                                                                         # HeaderLines Is removed again in openfile

                    for Rest in resturants:
                        temp = [Rest.Name, Rest.Type, Rest.Nationality, Rest.Quality, Rest.PriceClass,
                                Rest.DistansUni]                                                                        # Inserlist for file
                        writToFile.writerow(temp)

                print('Sucessfuly saved')
    else:
        print('Failed to save')


''' MenyChoiceNumber == '6': --------------------------------------------------------------------------------------- '''


def search():
    print('Please enter some values of the resturant you would like to go')                                             # Function that compare a new value to stored value in class

    inputClass = resturantsClass                                                                                        # This is the values the user puts in

    inputClass.Type        = input('\nEnter what type of resturant '
                                    '\n  Pizza, Fastfood, Cafe, Asian, Traditional, Steakhouse: ')
    inputClass.Nationality = input('\nEnter what nationality of the resturant'
                                    '\n  Swedish, Italian, Amarican, German, Asian, French: ')
    inputClass.Quality     = input('\nEnter what quality of the resturant\n  Low,Mid,High: ')
    inputClass.PriceClass  = input('\nEnter what price type of the resturant\n  Low,Mid,High: ')
    inputClass.DistansUni  = input('\nEnter what distans from the university\n  In 0 - 100km: ')
    returnScore = []

    referenses = validValues()                                                                                          # "Defult choices" the user can use
    i = 0

    for resturantsInfo in resturants:                                                                                   # Going throuhe the resturants and compare them to the input values
        returningResults = float(comparisonSearch(referenses.validTypes, resturantsInfo.Type, inputClass.Type))
        i += 1
        returningResults = returningResults + \
                           float(comparisonSearch(referenses.validNationalities,
                                                  resturantsInfo.Nationality, inputClass.Nationality))
        returningResults = returningResults + \
                           float(comparisonSearch2(referenses.validQualityPrices,
                                                   resturantsInfo.Quality, inputClass.Quality))
        returningResults = float(returningResults +
                                 (comparisonSearch2(referenses.validQualityPrices,
                                                    resturantsInfo.PriceClass, inputClass.PriceClass)))

        if isNumber(inputClass.DistansUni) == True:                                                                     # Input validation on numbers.
            returningResults = float(returningResults) + comparisonSearchIntValues\
                (float(resturantsInfo.DistansUni), float(inputClass.DistansUni))
        elif inputClass.DistansUni == '*':                                                                              # The * ignore function.
            returningResults += 1

        returningResults = float(returningResults / 5)                                                                  # Devide the comparison result so it become an 0-1 scale
        returnScore.append(returningResults)

    for i in range(0, len(returnScore)):                                                                                # Printout of Search function
        if max(returnScore) == returnScore[i]:                                                                          # Takes out the resturant with highes comparison value and print out the resturant.
            print('\n' + resturants[i].Name + ' Is Moust simular to youre request', 'whit a score of',
                  (returnScore[i]) * 100, '% match')

            print('\n' + 'Resturant info'                     + '\n ' +
                  'Type: '        + resturants[i].Type        + '\n ' +
                  'Nationality: ' + resturants[i].Nationality + '\n ' +
                  'Quality: '     + resturants[i].Quality     + '\n ' +
                  'PriceClass: '  + resturants[i].PriceClass  + '\n ' +
                  'Distans to örebro university: ' + resturants[i].DistansUni)


''' menyChoiceNumber == '7' ---------------------------------------------------------------------------------------- '''


def resturantValidator():                                                                                               # Primaliy for validate before saving so the database sodent get corrupt.
    headercunter = 0
    generalCunter = 0
    values = validValues()

    if resturants:                                                                                                      # Checking if resturants exists
        for row in resturants:                                                                                          # Going trough all resturants and compare the atributets to the valid class atribute.
            if row == ['Name', 'Type', 'Nationality', 'Quality', 'PriceClass', 'DistansUni']:                           # Checking if header exist
                headercunter += 1

            else:
                if isNumber(row.DistansUni) is False:
                    return False

                for subRow in values.validNationalities:                                                                # Going trouhe the valid values in class
                    if subRow == row.Nationality:                                                                       # Trigger if Nationality exist / are valid
                        generalCunter += 1

                if generalCunter == 0:
                    print('Nationaliteten är fel med ' + row.Name)                                                      # Validating Nationality. if previus code diden't trigger it's classified as nonvalid
                    return False

                generalCunter = 0

                for subRow in values.validTypes:                                                                        # Trigger if Types exist / are valid
                    if subRow == row.Type:
                        generalCunter += 1

                if generalCunter == 0:                                                                                  # Validating Type. if previus code diden't trigger it's classified as nonvalid
                    print('Typen är fel med ' + row.Name)
                    return False

                generalCunter = 0

                for subRow in values.validQualityPrices:                                                                # Going trouhe the valid values in class
                    if subRow == row.PriceClass:                                                                        # Trigger if Priceclass exist / are valid
                        generalCunter += 1

                if generalCunter == 0:
                    print('Price are wrong with ' + row.Name)
                    return False

                generalCunter = 0

                for subRow in values.validQualityPrices:                                                                # Going trouhe the valid values in class
                    if subRow == row.Quality:                                                                           # Validating Quality. If previus code diden't trigger it's classified as nonvalid
                        generalCunter += 1

                if generalCunter == 0:
                    print('Qvality are wrong with' + row.Name)
                    return False

                generalCunter = 0

            if headercunter >= 1:
                print('Sevral headers exist in the stuff you want to validate')                                         # Currently prints out if header exists

        return True                                                                                                     # True by defult to somthing is false.
    else:
        print('No resturants exists. Html error code 404')
        return False


''' ---------------------------------------------------------------------------------------------------------------- '''
# Search function uses the comparisonfunctions


def comparisonSearch(Listan, e_value, inputValue):                                                                      # Comparison of Nationalities and Type
    if inputValue == '*':
        return 1
    E = 0
    go_On = False

    for i in range(len(Listan)):
        if inputValue == Listan[i]:
            go_On = True

    if go_On == True:
        for i in range(len(Listan)):
            if e_value == Listan[i]:
                E = i
            if inputValue == Listan[i]:
                Input = i

        ans = abs(E - Input)
        if ans == 5:
            return 0
        elif ans == 4:
            return 0.2
        elif ans == 3:
            return 0.4
        elif ans == 2:
            return 0.6
        elif ans == 1:
            return 0.8
        elif ans == 0:
            return 1.1
    else:
        return 0


''' ---------------------------------------------------------------------------------------------------------------- '''


def comparisonSearch2(Listan, e_value, inputValue):                                                                     # Comparison with High Mid Low, Quantity and Pricelevel
    if inputValue == '*':
        return 1
    E = 0
    go_On = False

    for i in range(len(Listan)):
        if inputValue == Listan[i]:
            go_On = True

    if go_On == True:

        for i in range(len(Listan)):
            if e_value == Listan[i]:
                E = i
            if inputValue == Listan[i]:
                Input = i

        ans = abs(E - Input)

        if ans == 2:
            return 0.3
        elif ans == 1:
            return 0.6
        elif ans == 0:
            return 0.9
    else:
        return 0


''' ---------------------------------------------------------------------------------------------------------------- '''


def comparisonSearchIntValues(e_value, inputValue):                                                                     # Comparison with numbers. Distans with 0 - 100
    Dist = abs(e_value - inputValue)
    if Dist > 100:
        return 0
    else:
        Dist = abs((Dist * 0.01) - 1)
    return Dist


''' MenyChoiceNumber == 9: ----------------------------------------------------------------------------------------- '''


def printOutResturant():                                                                                                # Prints out all values stored in the class
    for Rest in resturants:
        print('Name:', Rest.Name,
              '\nType:', Rest.Type,
              '\nNationality:', Rest.Nationality,

              '\nQuality:', Rest.Quality,
              '\nPriceClass:', Rest.PriceClass,
              '\nDistans To University:', Rest.DistansUni)
        print()

