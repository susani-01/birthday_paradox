import datetime,random

def getBirthdays(numberOfBirthdays):
	"""Returns a list of nummber random date objects for birthdays."""
	birthdays=[]
	for i in range(numberOfBirthdays):
		startOfYear= datetime.date(2001,1,1)

		randomNumberOfDays=datetime.timedelta(random.randint(0,364))
		birthdays = startOfYear + randomNumberOfDays
		birthdays.append(birthday)

	return getBirthdays

	def getMatch(birthdays):
		"""returns tha date object of a birthdays that occur mor than one in the birthdays list."""

		if len(birthdays)==len(set(birthdays)):
			return None 


		for a,birthdayA in enumerate(birthdays):
			for b,birthdayB in enumerate(birthdays[a+1]):
				if birthdayA==birthdayB:
					return birthdayA

#display the intro:
print("""Birthday paradox by tony as it represent that in a group of N people there is the odd of having the matching birthday dates""")

MONTHS = ('Jan','Feb','March','April','May','June','Aug','sep','Oct','Nov','Dec')

while True:
	print("How many birthdays shall i genarate? (max 100)")
	response=input('> ')
	if response.isdecimal() and (0 < int(response) <= 100):
		numBDays=int(response)
		break

print()

#Generate and displays the birthdays:
print('Here are',numBDays,'birthdays:')

birthdays=getBirthdays(numBDays)
for i,birthday in enumerate(birthdays):
	if i!=0:

		#Display a comma for each birhday after the first birthdays


		print(', ',end='')
		monthName=MONTHS[birthday.month -1]
		dateText='{}{}'.format(monthName,birthday.day)
		print(dateText,end='')

print()
print()

match=getMatch(birthdays)

print('In this simulation, ', end='')

if match !=None:
	monthName=MONTHS[match.month -1]
	dateText='{}{}'.format(monthName,match.day)
	print("multiple people have a birthday on ", dateText)
else:
	print('there is no matching birthdays')
print()


print('Generating',numBDays,'random birthdays 100_000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100_000 simulations.')

simMatch=0
for i in range(100_000):
	if i%10_000==0:
		print(i,'simulations run...')
		birthdays=getBirthdays(numBDays)
		if getMatch(birthdays) !=None:
			simMatch=simMatch + 1

print('100,000')

#Display simulations

probability=round(simMatch/100_000*100,2)
print('out of 100_000 simulations of', numBDays,'people there was a '  )
print ('matching birthdays in that group',simMatch,'times. this means')
print('that ',  numBDays, 'people have a',probability,'% chance of')
print('having a matching birthday in their group.')
print('that\'s probably more than you would think!')


					
