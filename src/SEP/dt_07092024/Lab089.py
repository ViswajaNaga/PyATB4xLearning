# whichever is common we will mark it as staticmethod
# static class is not possible in python , it is possible in Java
class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading from Excel")

class MySQLdbConnection:
    @staticmethod
    def readMySQLFile():
        print("Reading from MySQL")

class TC1:
    def runTC(self):
        ExcelReader.readExcelFile()
        MySQLdbConnection.readMySQLFile()

tc1=TC1()
tc1.runTC()

