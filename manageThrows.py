import playerData as pd


# def checkGameAndScore(player, throw, num):
def checkGameAndScore(player, dart):
	''' Check for the game and if killer, score for player
		otherwise score for others who dont have 3 od the throw
	'''
	scoreList = []
	listID = 0
	for p in pd.playerList:
		count = getItemCount(p, dart)
		if count < 3:
			scoreList.append(listID)
		listID += 1
	return scoreList

	'''match game:
		case 'Killer':
			canScore = False
			for p in pd.playerList:
				count = getItemCount(p, dart)
				if count < 3:
					scoreList.append(player)
			print('Killer')
		
		case 'Cutthroat':
			for p in pd.playerList:
				count = getItemCount(p, dart)
				if count < 3:
					scoreList.append(player)
			print('Cutthroat')'''
	

def handleNoCountNumbers(player, throw, dort):
	''' if the number is 9 or less and not a D or T
		then the throw can be discarded, otherwise
		if it is a D or T and player has 3D or 3T then can score
	'''
	canAddScore = False
	canScore = 0
	num = 0
	if dort == 'D':
		canScore = getItemCount(player, 'DD')
		if canScore < 3:
			addToDict(player, 'DD', 1)
		num = throw * 2
	elif dort == 'T':
		canScore = getItemCount(player, 'TT')
		if canScore < 3:
			addToDict(player, 'TT', 1)
		num = throw * 3
	if canAddScore and canScore == 3:
		addToDict(player, throw, num)
	
def splitThrow(throw):
	''' Return Double, Treble, Bed or None & Number thrown
		return -> 'Double', 19 - 'Bed', None - 'Double', Bull
	'''
	if throw == 'Bed':
		return 'Bed', None
	elif throw == 'TT':
		return 'Treble', None
	elif throw[0] == 'T':
		return 'Treble', throw[1:]
	elif throw == 'DD':
		return 'Double', None
	elif throw[0] == 'D':
		return 'Double', throw[1:]
	elif throw[0] == 'Bed':
		return 'Bed', throw[1:]
	else:
		return None, throw

def checkOtherDicts(player, dart):
	''' 
		Check all other players dict for the dart thrown
		if < 3 then I can score
		if game = Killer then add to players score
		otherwise add to other players score
	'''
 
	canScore = False
	for p in pd.playerList:
		count = 0
		if p == player:
			continue
		else:
			count = getItemCount(p, dart)
			if count < 3:
				canScore = True
				break
	return canScore

def getItemCount(player, dart):
	''' 
		Check player dict for the dart thrown
		must not be 1,2,3,4,5,6,7,8,9 unless D or T
		--> return count
	'''
	dict = player
	count = 0
	count = dict.get(dart)
	return count

def addToDict(player, throw, num):
	'''
		Add the num to the players dict for the throw

	'''
	dict = player
	dict[throw] = dict.get(throw, 0) + num

def handleBedThrow(player, throw):
	''' 
		Check if I have all 3 Beds
		Yes, calculate the score and add to my total
		No, add 1 bed to my Bed count
		'''
	count = getItemCount(player, throw)
	dict = player
	count = 0
	score = 0
	count = getItemCount(player, 'Bed')
	if count < 3:
		addToDict(player, 'Bed', 1)
	elif count == 3:
		count = getItemCount(player, throw)
		darts = throw[1:]
		for d in darts:
			if d[0] == 'D':
				score +=  2 * int(d[1:])
			elif d[0] == 'T':
				score +=  3 * int(d[1:])
			else:
				score += int(d)
		addToDict(player, 'Score', score)

def handleDDouble(player, throw):
	dict = player
	count = 0
	canScore = False
	numCounter = 1
	count = getItemCount(player, throw)
	while count < 3 and numCounter > 0:
		addToDict(player, throw, 1)
		count = getItemCount(player, throw)
		numCounter -= 1
	if numCounter > 0:
		canScore = checkOtherDicts(player, throw)
		if canScore:
			addToDict(player, throw, 1)
			numCounter -= 1

def handleDBullThrow(player, throw):
	dict = player
	count = 0
	numCounter = 2
	count = getItemCount(player, throw)
	while count < 3 and numCounter > 0:
		addToDict(player, throw, 1)
		count = getItemCount(player, throw)
		numCounter -= 1
	
	if numCounter > 0:
		canScore = checkOtherDicts(player, throw)
		if canScore:
			while numCounter > 0:
				addToDict(player, 'Score', 25)
				numCounter -= 1

def handleBullThrow(player, throw):
	dict = player
	count = 0
	numCounter = 1
	count = getItemCount(player, throw)
	while count < 3 and numCounter > 0:
		addToDict(player, throw, 1)
		count = getItemCount(player, throw)
		numCounter -= 1
	
	if numCounter > 0:
		canScore = checkOtherDicts(player, throw)
		if canScore:
			while numCounter > 0:
				addToDict(player, 'Score', 25)
				numCounter -= 1

def handleDoubleThrow(player, throw):
	if throw in pd.noScore:
		#  Check if Double or Treble
		# print('No Score')
		pass
	else:
		dict = player
		count = 0
		numCounter = 2
		count = getItemCount(player, throw)
		while count < 3 and numCounter > 0:
			addToDict(player, throw, 1)
			count = getItemCount(player, throw)
			numCounter -= 1
		if numCounter > 0:
			canScore = checkOtherDicts(player, throw)
			if canScore:
				while numCounter > 0:
					addToDict(player, 'Score', int(throw))
					numCounter -= 1

def handleTTreble(player, throw):
	dict = player
	count = 0
	numCounter = 1
	count = getItemCount(player, throw)
	while count < 3 and numCounter > 0:
		addToDict(player, throw, 1)
		count = getItemCount(player, throw)
		numCounter -= 1
	if numCounter > 0:
		canScore = checkOtherDicts(player, throw)
		if canScore:
			addToDict(player, throw, 1)
			numCounter -= 1

def handleTrebleThrow(player, throw):
	dict = player
	numCounter = 3
	count = 0
	count = getItemCount(player, throw)
	while count < 3 and numCounter > 0:
		addToDict(player, throw, 1)
		count = getItemCount(player, throw)
		numCounter -= 1

	if numCounter > 0:
		canScore = checkOtherDicts(player, throw)
		if canScore:
			while numCounter > 0:
				addToDict(player, 'Score', int(throw))
				numCounter -= 1

def retNumber(num):
	#if num[0] == 'D' and num[1] == 'D':
	if num[1] == 'D':
		return num
	elif num[1] == 'T':
		return num
	else:
		return num[1:]

def handleThrow(p, darts):
	# scoreOn = checkGameAndScore(p, '20')

	for d in darts:
		if d == 'Bed':
			handleBedThrow(p, 'Bed')
			break
		elif d == 'DBull':
			handleDBullThrow(p, 'Bull')
		elif d == 'Bull':
			actualNumber = d
			handleBullThrow(p, 'Bull')
		elif d == 'DD':
			handleDDouble(p,'DD')
		elif d == 'TT':
			handleTTreble(p,'TT')
		elif d[0] == 'D':
			'''To Do:
			Give option to take a Double or use the throw
			'''
			actualNumber = retNumber(d)
			if actualNumber in pd.noScore:
				handleNoCountNumbers(p, actualNumber, 'D')
			else:
				handleDoubleThrow(p, actualNumber)
		elif d[0] == 'T':
			'''To Do:
			Give option to take a Treble or use the throw
			'''
			actualNumber = retNumber(d)
			handleTrebleThrow(p, actualNumber)

		else:
			if d not in pd.noScore:
				count = getItemCount(p, d)
				if count < 3:
					addToDict(p, d, 1)
				else:
					canScore = False
					canScore = checkOtherDicts(p, d)
					if canScore:
						addToDict(p, 'Score', int(d))
						print(f'Add 1 x {d} to the players score')

def findAndUpdate(dict, throw):
	# Update the dictionary with 1 x X for the numbers thrown

	for key in throw:
		# Find the number & if D or T
		score = dict.get('Score')
		print(score)
		if key [0] == 'D' and key[1] == 'D':
			retNum = retNumber(key) + 1
			#count = dict.get(retNum)

		elif key [0] == 'T' and key[1] == 'T':
			retNum = retNumber(key)
			dict[retNum] = dict.get(retNum, 0) + 1
		elif key[0] == 'D':
			retNum = retNumber(key)
			dict[retNum] = dict.get(retNum, 0) + 2
		elif key[0] == 'T':
			retNum = retNumber(key)
			dict[retNum] = dict.get(retNum, 0) + 3
		else:
			dict[key] = dict.get(key, 0) + 1
			dict['Score'] = dict.get('Score', 0) + int(retNum)

def doMain(player, throw):
    handleThrow(player, throw)

if __name__ == '__main__':
	print(f'You are unable to run form here - manageThrows.py ')