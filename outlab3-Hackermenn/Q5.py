import argparse,csv
import sys,os.path

class ArgParser(argparse.ArgumentParser):
	def error(self, message):
		print(message)
		exit()

class myDialect(csv.Dialect):
	delimiter=','
	quoting=csv.QUOTE_MINIMAL

class writeCSV(csv.DictWriter):
	def __init__(self,f):
		fieldnames=['first_name','last_name','roll_no','gender','mobile','dept','CGPA']
		super().__init__(f,fieldnames=fieldnames);


parser = ArgParser(description='Add student data to database')
parser.add_argument('--first_name',required=True)
parser.add_argument('--last_name',required=True)
parser.add_argument('--roll_no',required=True)
parser.add_argument('--gender',required=True)
parser.add_argument('--mobile',required=True)
parser.add_argument('--dept',required=True)
parser.add_argument('--CGPA',required=True)
#obj = parser.parse_args(sys.argv[1:])
obj = vars(parser.parse_args(sys.argv[1:]))

for par in obj.keys():
	if(par!='first_name'):
		obj[par]=' '+obj[par]

#print(obj)
if os.path.exists('student_database.csv'):
	with open('student_database.csv','a',newline='') as csvfile:
		addWriter=writeCSV(csvfile)
		addWriter.writerow(obj)
	#pass
	#with open('student_database.csv','w',)
else:
	#print("Doesnt exist")
	with open('student_database.csv','a',newline='') as csvfile:
		addWriter=writeCSV(csvfile)
		#headerDict={}
		#headerDict[first_name]='First Name'
		headerDict={'first_name': 'First Name', 'last_name': ' Last Name', 'roll_no': ' Roll Number', 'gender': ' Gender', 'mobile': ' Mobile', 'dept': ' Dept', 'CGPA': ' CGPA'}
		addWriter.writerow(headerDict)
		addWriter.writerow(obj)

print("Successfully Added!!")
