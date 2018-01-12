CSVFile1 = open('cs162hw01salesData01.csv', 'r')
#CSVFile2 = open('cs162hw01salesData02', 'r')

if CSVFile1:
	
	Header = CSVFile1.readline()
	Header = Header.strip('\r\n')
	Header = Header.split(',')
	
	Database = {}
	
	for i in range(0, len(Header)):
		Database[Header[i]] = []
		
	print Database
	
	while CSVFFile1 is not None:
		NewLine = CSFVFile1.readline()