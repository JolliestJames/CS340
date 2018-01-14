# Written by: James Martinez
# Assignment: Homework 1 - Flat Files & Physical Data

class Transaction:

	def __init__(self):
		self.Attributes = {}
		
	def SetAttributes(self, Keys, Values):
		for i in range(0, len(Keys)):
			self.Attributes[Keys[i]] = Values[i]
			
def PrintDatabase(Database, Keys):
	for i in range(0, len(Database)):
		for j in range(0, len(Keys)):
			print Database[i].Attributes[Keys[j]],
		print ''
		
def CountNameOccurrences(Database, Name):
	
	Name = Name.lower()
	
	Count = 0
	
	for i in range(0, len(Database)):
		if Name in Database[i].Attributes['Name'].lower():
			Count += 1
			
	return Count
		
def ProcessFlatFile(FileName):

	CSVFile = open(FileName, 'r')

	if CSVFile:
		
		Header = CSVFile.readline()
		Header = Header.strip('\r\n')
		Header = Header.split(',')
		
		Database = []
		
		NewLine = "blank"
		
		while len(NewLine) > 1:
			NewLine = CSVFile.readline()
			NewLine = ' '.join(NewLine.split())
			NewLine = NewLine.split(',')
			if len(NewLine) > 1:
				#Remove unwanted whitespace
				NewLine[4].strip(' ')
				NewLine[1] = ''.join(NewLine[1].split())
				#Create new transaction
				NewTransaction = Transaction()
				NewTransaction.SetAttributes(Header, NewLine)
				Database.append(NewTransaction)
		
		return Database, Header
			
def CalculateAverageTransactionAmount(Database):
	
	TotalTransactionAmount = 0

	for i in range(0, len(Database1)):
		
		if len(Database1[i].Attributes['Price']) > 0:
			TransactionAmount = int(Database[i].Attributes['Price'])
			TotalTransactionAmount += TransactionAmount

	AverageTransactionAmount = TotalTransactionAmount/len(Database1)
	
	return AverageTransactionAmount

def ChangeData(Database, Category, Old, New):

	OldForCompare = Old.lower()

	for i in range(0, len(Database)):
		if OldForCompare in Database[i].Attributes[Category].lower():
			Database[i].Attributes[Category] = New

	return Database
	
def CreateNewDatabaseFile(Database, Keys, FileToWrite):

	NewFile = open(FileToWrite, "w")

	LineToOutput = ""
		
	for i in range(0, len(Keys)):
		if i == len(Keys) - 1:
			LineToOutput = LineToOutput + Keys[i] + "\n"
		else:
			LineToOutput = LineToOutput + Keys[i] + ","

	for i in range(0, len(Database)):
		for j in range(0, len(Keys)):
			if j == len(Keys) - 1:
				LineToOutput = LineToOutput + Database[i].Attributes[Keys[j]] + "\n"
				NewFile.write(LineToOutput)
			else:
				LineToOutput = LineToOutput + Database[i].Attributes[Keys[j]] + ","
		LineToOutput = ""

	NewFile.close()
	
#Step1
Database1, Keys = ProcessFlatFile('cs162hw01salesData01.csv')
Database1 = sorted(Database1, key=lambda Transaction: Transaction.Attributes['Product'])
PrintDatabase(Database1, Keys)

#Step2
NumberOfAmandas = CountNameOccurrences(Database1, 'Amanda')
print "\nThere are " + str(NumberOfAmandas) + " Amandas.\n"
	
#Step3
AverageTransactionAmount = CalculateAverageTransactionAmount(Database1)
print "The average transaction amount is " + str(AverageTransactionAmount) + ".\n"

#Step4
Database1 = ChangeData(Database1, 'Country', 'United States', 'USA')
CreateNewDatabaseFile(Database1, Keys, 'NewDatabase1.csv')
print "Every instance of United States has been replaced with USA and written to NewDatabase1.csv\n"

#Step5
Database2, Keys = ProcessFlatFile('cs162hw01salesData02.csv')
Database2 = sorted(Database2, key=lambda Transaction: Transaction.Attributes['Product'])
PrintDatabase(Database2, Keys)

NumberOfAmandas = CountNameOccurrences(Database2, 'Amanda')
print "\nThere are " + str(NumberOfAmandas) + " Amandas.\n"
	
AverageTransactionAmount = CalculateAverageTransactionAmount(Database2)
print "The average transaction amount is " + str(AverageTransactionAmount) + ".\n"

Database2 = ChangeData(Database2, 'Country', 'United States', 'USA')
CreateNewDatabaseFile(Database2, Keys, 'NewDatabase2.csv')
print "Every instance of United States has been replaced with USA and written to NewDatabase2.csv\n"






















		
		
		
		