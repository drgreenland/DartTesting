import manageThrows as m
import playerData as pd

throw1 = ['TT', 'D19', 'T15', 'D18', 'Bull', 'T20', 'DBull', '12', '16', 'Bed', '17', 'T17', 'D17']
throw2 = [['Bed', 'D19', '19', 'T19'], ['TT', 'D19', 'T15'], ['T20', 'DBull', '12']]
# throw2 = ['Bed', '19', '19', 'T19']
throw1 = ['T20', 'D10', 'D9']
throw2 = ['TT', 'D19', 'T15']
throw3 = ['Bed', '17', 'T17', 'D17']
throw4 = ['T20', 'Bull', '12']
throw5 = ['T16', '10', 'D9']
throw6 = ['TT', 'T13', 'DD']
throw7 = ['Bed', '11', 'T11', 'D11']
throw8 = ['20', 'DBull', 'T12']

def doMain(player, throws):
	m.handleThrow(player, throws)
	print(f'After Changes:\n {player}')

if __name__ == '__main__':
	print(f'Before changes:\n {pd.p1}')
	doMain(pd.p1, throw1)
	doMain(pd.p1, throw2)
	doMain(pd.p1, throw3)
	doMain(pd.p1, throw4)
	doMain(pd.p1, throw5)
	doMain(pd.p1, throw6)
	doMain(pd.p1, throw7)
	doMain(pd.p1, throw8)
# throw1 = ['T20', 'D10', 'D9']
# throw2 = ['TT', 'D19', 'T15']
# throw3 = ['Bed', '17', 'T17', 'D17']
# throw4 = ['T20', 'Bull', '12']
# throw5 = ['T16', '10', 'D9']
# throw6 = ['TT', 'T13', 'DD']
# throw7 = ['Bed', '11', 'T11', 'D11']
# throw8 = ['20', 'DBull', 'T12']