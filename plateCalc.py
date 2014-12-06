"""
A quick script to calculate and display the number of kg plates 
on each side of a 45lb barbell. I am lazy and don't like to do
basic math at the gym. Also how I am staring to learn python.
"""
import math

kilogram = 2.20462262185
largestPlate = 20 #40 if the gym has it
barbell = 45 / kilogram

def getKg( weight ):	
	try:
		convertedWeight = float(weight)
		convertedWeight = convertedWeight / kilogram
	except:
		print("Enter a number dickweed.")
		return 0
	return convertedWeight

def getSide( weight ):
		singleSide = float(weight) / 2.00
		singleSide -= (barbell / 2.00)
		return(singleSide)

#Buckle up, it's recursion time
def getPlates( weight, plate ):
	plateCount = weight/plate
	remaningWeight = weight%plate
	
	if not(plateCount < 1):
		print("%0.1Fkg x %d" % (plate, plateCount))

	if(remaningWeight <= 0 or plate == 0.5):
		return

	if (plate < 5):
		getPlates(remaningWeight, (plate - 0.5))
	else:
		getPlates(remaningWeight, plate/2)

tableLines = "\n-------------------------\n"

while(True):
	user_input = input("Enter Weight in LBS: ")
	kgWeight = getKg(user_input)
	side = getSide(kgWeight)
	print(tableLines)
	print("Weights assume a 45lb bar")
	print("Weight per side: %0.1Fkg" % (side))
	print("-----Plates per side-----")
	getPlates(side,largestPlate)
	print(tableLines)