def property_tax():


	PropertyValue = float(input('Enter the actual value: '))
	AssessedValue = PropertyValue*.6
	PropertyTax = AssessedValue*(72/10000)
	
	print('Assessed value: ${:,.2f}' .format(AssessedValue, '.2f'))
	print('Property tax: $' + format(PropertyTax, '.2f'))

property_tax()	

def future_value():


	PresentValue = float(input('Enter the present value of the account in dollars: '))
	MonthlyInterestRate = float(input('Enter the monthly interest rate as a percentage: '))
	NumberMonths = float(input('Enter the number of months: '))
	AccountValue = PresentValue * (1 + MonthlyInterestRate*.01)**NumberMonths
	
	print('The information for your account is: ')
	print('Present Value: $' + format(PresentValue, '.2f'))
	print('Interest Rate: %' + format(MonthlyInterestRate, '.2f'))
	print('After 12 months, the value of your account will be $' + format(AccountValue, '.2f'))

future_value()

def genz_search():


	BoyList = open('BoyNames.txt', 'r')
	PopularBoy = BoyList.readlines()
	for i in range(len(PopularBoy)):
		PopularBoy[i] = PopularBoy[i].rstrip('\n')

	GirlList = open('GirlNames.txt', 'r')
	PopularGirl = GirlList.readlines()
	for i in range(len(PopularGirl)):
		PopularGirl[i] = PopularGirl[i].rstrip('\n')

	BoyName = input("Enter a boy's name, or N if you do not wish to enter a boy's name: ")
	GirlName = input("Enter a girl's name, or N if you do not wish to enter a girl's name: ")

 
	if BoyName == 'N': 
		print("You chose not to enter a boy's name.")

	elif BoyName in PopularBoy:
		print(BoyName + " is one of the most popular boy's names.")

	else:
		print(BoyName + " is not one of the most popular boy's names.")

	if GirlName == 'N':
		print("You chose not to enter a girl's name.")

	elif GirlName in PopularGirl:
		print(GirlName + " is one of the most popular girl's names.")

	else:
		print(GirlName + " is not one of the most popular girl's names.")

genz_search()

def prime_gen():


	UserInteger = input('Enter an integer greater than 1: ')

	for i in range(2, int(UserInteger) + 1):
		number = 0
		for j in range(2,i):

			if (i % j == 0):
				number = 1

		if (number == 0):
			print(i,'is prime.')
		elif ( number == 1):
			print(i,'is composite.')

prime_gen()

def get_word_dict(LineList):
	
	WordDict = {}
	for e in LineList:
		words = e.split(' ')
		count = 1
		for w in words:
			if w in WordDict:
				WordDict[w] += 1
			else:
				WordDict[w] = 1
	return(WordDict)

def write_index_file(WordDict):
	outputfile = open('index_j.txt', 'w')

	for key in sorted(WordDict):
		outputfile.write(key + ' ' + str(WordDict[key]))
		outputfile.write('\n')

	outputfile.close()
def main():
	inputfile = open('tirole_nobel.txt', 'r')
	LineList = inputfile.readlines()
	inputfile.close()
	for i in range(len(LineList)):
		LineList[i] = LineList[i].rstrip('\n')
	WordDict = get_word_dict(LineList)

	write_index_file(WordDict)

main()
def pow_recursive():	
	base = float(input('Enter a base number: '))
	power = float(input('Enter a positive whole number between 1 and 100: '))
	answer = recursion(base, power)
	base = format(float(base), '.1f')

	print(str(base) + ' raised to the power of ' + str(power) + ' is {:,.2f}' .format(answer, '.2f'))

def recursion(base, power):
	if power == 0:
		return 1
	else:
		return(base * recursion(base, power - 1))

pow_recursive()
