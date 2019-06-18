import requests
def = input('Tell me a word you don\'t know')
try:
	int(def)
	print ('Error, not a word')
except:
	resp = requests.get('https://wordsapiv1.p.mashape.com/words/%s/definitions' % def)
	data = resp.json()
	print(data)

