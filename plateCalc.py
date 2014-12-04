"""
A quick script to calculate and display the number of kg plates 
on each side of a 45lb barbell. I am lazy and don't like to do
basic math at the gym. Also how I am staring to learn python.
"""
import math

kilogram = 2.20462262185
largestPlate = 20 #40 if the gym has it

def getKg( weight ):	
	try:
		convertedWeight = float(weight)
		#remove bar
		convertedWeight -= 45
		convertedWeight = convertedWeight / kilogram
	except:
		print("Enter a number dickweed.")
		return 0
	return convertedWeight

def getSide( weight ):
	singleSide = weight / 2.00
	return(math.floor(singleSide))

#Buckle up, it's recursion time
def getPlates( weight, plate ):
	plateCount = weight/plate
	remaningWeight = weight%plate
	
	if not(plateCount < 1):
		print("%0.1Fkg x %d" % (plate, plateCount))

	if(remaningWeight < 2.5):
		return

	if not(plate <= 2.5):
		getPlates(remaningWeight, plate/2)

tableLines = "\n-------------------------\n"

while(True):
	user_input = input("Enter Weight in LBS: ")
	side = getSide(weight)
	print(tableLines)
	print("Weights assume a 45lb bar")
	print("Weight per side: %dkg" % (side))
	print("-----Plates per side-----")
	getPlates(side,largestPlate)
	print(tableLines)