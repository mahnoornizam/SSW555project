from operator import contains
from datetime import date
from click import secho
from prettytable import PrettyTable


raw_file = input("PLease enter file name: ")

#f = open(raw_file, mode='r')
#f = f.read()
#print(f)

class individual:
    ID = ""
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
#        self.age = age
    
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

"""
    def age(self, birthDate):
        birthDate = birthDate
        deathDate = deathDate
        today  = date.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

        return self.age
"""

def findIndividual(content):
    individuals = []
    for i in range(0, len(content)):
        if ("INDI" in content[i]):
            start = i
            i += 1
            individual = []
            while (content[i][0] != "0"):
                individual.append(content[i])
                i += 1
            individuals.append(individual)
            i = start
    return individuals

def getIndividualName(individual):
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

def getIndividualSex(individual):
    sex = ""
    for i in range(0, len(individual)):
        if "SEX" in individual[i]:
            sex = individual[i][6]
    return sex

def getIndividualBirthDate(individual):
    birthDate = ""
    for i in range(0, len(individual)):
        if "BIRT" in individual[i]:
            i += 1
            birthDate = individual[i][7:individual[i].index("\n")]
    return birthDate

def getIndividualDeathDate(individual):
    deathDate = ""
    for i in range(0, len(individual)):
        if "DEAT" in individual[i]:
            i += 1
            deathDate = individual[i][7:individual[i].index("\n")]
    # i tried adding else: "alive" but it just makes all of them = alive.. 
    return deathDate




def main():
    fileContent = []
    #raw_file = "C:\Users\Leo\Downloads\LeoPapadopoulosGEDCOM (1).ged "#input("PLease enter file name: ")
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



