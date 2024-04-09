class Company:

    def __init__(self, yard):
        # private variables
        self.__yard = yard

    def readYard(self):
        return self.__yard

    def updateYard(self, location):
        self.__yard = location

# ---------------------------------------------


class Fleet:

    def __init__(self, name, wage, licence, yard, truck):
        # private variables
        self.__driverName = name
        self.__driverWage = wage
        self.__driverLicence = licence
        # aggregation
        self.__companyYard = Company(yard)
        self.__truck = truck
        self.__available = True

    def readAvailable(self):
        return self.__available

    def markAvailable(self):
        self.__available = True

    def markUnavailable(self):
        self.__available = False

    def readDriverName(self):
        return self.__driverName

    def readDriverWage(self):
        return self.__driverWage

    def readDriverLicence(self):
        return self.__driverLicence

    def readCompanyYard(self):
        return self.__companyYard.readYard()

    def readAssignedTruck(self):
        return self.__truck

    # Polymorphic Methods

    def readType(self):
        return ''

    def readDescriptionPart1(self):
        return ''

    def readDescriptionPart2(self):
        return ''

    def readDescriptionPart3(self):
        return ''

    # --------------------------------------------


class Loaded(Fleet):

    def __init__(self, name, wage, licence, yard, truck, trailer, load, destination):
        super().__init__(name, wage, licence, yard, truck)
        self.__trailer = trailer
        self.__load = load
        self.__destination = destination
        self.__available = False

    def readAvailable(self):
        return self.__available

    def readType(self):
        return 'Loaded'

    def readDescriptionPart1(self):
        return 'Trailer : ' + str(self.__trailer)

    def readDescriptionPart2(self):
        return 'Load : ' + str(self.__load)

    def readDescriptionPart3(self):
        return 'Destination : ' + str(self.__destination)

    # --------------------------------------------


class Truck(Fleet):

    def __init__(self, name, wage, licence, yard, truck, make, horsepower, reg):
        super().__init__(name, wage, licence, yard, truck)
        self.__make = make
        self.__horsepower = horsepower
        self.__reg = reg

    def readType(self):
        return 'Truck'

    def readDescriptionPart1(self):
        return 'Make : ' + str(self.__make)

    def readDescriptionPart2(self):
        return 'Horsepower : ' + str(self.__horsepower)

    def readDescriptionPart3(self):
        return 'Reg : ' + str(self.__reg)

    # --------------------------------------------


class Driver(Fleet):

    def __init__(self, name, wage, licence, yard, truck, fullName, age, allLicences):
        super().__init__(name, wage, licence, yard, truck)
        self.__fullName = fullName
        self.__age = age
        self.__allLicences = allLicences

    def readType(self):
        return 'Driver'

    def readDescriptionPart1(self):
        return 'Full Name : ' + str(self.__fullName)

    def readDescriptionPart2(self):
        return 'Age : ' + str(self.__age)

    def readDescriptionPart3(self):
        return 'Licences : ' + str(self.__allLicences)

    # --------------------------------------------
