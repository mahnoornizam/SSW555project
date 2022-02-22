from operator import contains
from datetime import date
from click import secho
from prettytable import PrettyTable


raw_file = input("Please enter file name: ") #enter name of the file

class individual: #create class to identify all individuals
    ID = "" #each individual has these traits that will be added to table
    name = ""
    sex = ""
    birthDate = ""
    deathDate = ""
#    age = ""

    mother = None
    father = None

    def __init__(self, ID, name, sex, birthDate, deathDate):
        self.ID = ID
        self.name = name
        self.sex = sex
        self.birthDate = birthDate
        self.deathDate = deathDate
#        self.age = age #age incomplete
    
    def printIndividual(self):
        print("")

    def getID(self):
        return self.ID
    
    def getName(self):
        return self.name

    def getSex(self):
        return self.sex

    def getBirthDate(self):
        return self.birthDate
    
    def getDeathDate(self):
        return self.deathDate

""" #incomplete function for determining the age
    def age(self, birthDate):
        birthDate = birthDate
        deathDate = deathDate
        today  = date.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

        return self.age
"""

#class ends
#below are functions for finding individual traits

def findIndividual(content): 
    individuals = [] #all individuals
    for i in range(0, len(content)):
        if ("INDI" in content[i]):
            start = i
            i += 1
            individual = [] #each individual that will be added to list of all individuals
            while (content[i][0] != "0"):
                individual.append(content[i])
                i += 1
            individuals.append(individual)
            i = start
    return individuals

def getIndividualName(individual): #returns individuals name
    name = ""
    for line in individual:
        if ("NAME" in line):
            name = line[7:line.index("\n")]
    if ("/" in name):
        nameList = []
        for i in range(0, len(name)):
            if (name[i] != "/"):
                nameList.append(name[i])
        name = "".join(nameList)
    return name

def getIndividualSex(individual): #returns individuals sex
    sex = ""
    for i in range(0, len(individual)):
        if "SEX" in individual[i]:
            sex = individual[i][6]
    return sex

def getIndividualBirthDate(individual): #returns individuals birthDate
    birthDate = ""
    for i in range(0, len(individual)):
        if "BIRT" in individual[i]:
            i += 1
            birthDate = individual[i][7:individual[i].index("\n")]
    return birthDate

def getIndividualDeathDate(individual): #returns individuals deathDate
    deathDate = ""
    for i in range(0, len(individual)):
        if "DEAT" in individual[i]:
            i += 1
            deathDate = individual[i][7:individual[i].index("\n")]
    # i tried adding else: "alive" but it just makes all of them = alive.. 
    return deathDate

#individual trait functions end here
#below are for family functions

def searchByID(ID, individualsWithData):
    for individual in individualsWithData:
        if individual.getID() == ID:
            return individual
        
def makeFamilies(families, individualsWithData):
    for i in range(0, len(families)):
        for x in range(0, families[i]):
            father = None
            mother = None

            if "CHIL" in families[i][x]:
                childID = families[i][x][7:families[i][x].index("\n")]
                child = searchByID(childID, individualsWithData)
                for y in range(0, len(families[i])):
                    if "HUSB" in families[i][y]:
                        fatherID = families[i][y][7:families[i][x].index("\n")]
                        father = searchByID(fatherID, individualsWithData)
                        child.setFather(father)
                    if "HUSB" in families[i][y]:
                        motherID = families[i][y][7:families[i][x].index("\n")]
                        mother = searchByID(motherID, individualsWithData)
                        child.setMother(mother)
#main function below
#main function opens file, gets individuals data
#creates table and adds elements by column

                        
def main(): #main
    fileContent = []
    f = open(raw_file, mode='r')
    with f as gedcomFile:
        line = gedcomFile.readline()
        while (line != ""):
            fileContent.append(line)
            line = gedcomFile.readline()
        
        individuals = findIndividual(fileContent)
        #families = findFamilies(fileContent)

        names  = []
        for i in range(0, len(individuals)):
            name = getIndividualName(individuals[i])
            names.append(name)
        birthDates = []
        for i in range(0, len(individuals)):
            birthDate = getIndividualBirthDate(individuals[i])
            birthDates.append(birthDate)
        deathDates = []
        for i in range(0, len(individuals)):
            deathDate = getIndividualDeathDate(individuals[i])
            deathDates.append(deathDate)
        sexes = []
        for i in range(0, len(individuals)):
            sex = getIndividualSex(individuals[i])
            sexes.append(sex)
        IDS = []
        for i in range(1, len(individuals)+1):
            IDS.append("@P{0}@".format(i))

        individualsWithData = []
        for i in range(0, len(individuals)):
            individualsWithData.append(individual(IDS[i], names[i], sexes[i], birthDates[i], deathDates[i]))

    
        table = PrettyTable()

        #table.field_names = ["ID", "Name", "Sex", "birthDate", "deathDate"]
        table.add_column("ID", IDS)
        table.add_column("Name", names)
        table.add_column("Sex", sexes)
        table.add_column("birthDate", birthDates)
        table.add_column("deathDate", deathDates)

        print(table)



if (__name__ == "__main__"):
    main()



