import bs4 as bs
import urllib.request

def get_items(name,lane):
	source = urllib.request.urlopen('http://champion.gg/champion/{}/{}'.format(name,lane)).read()
	soup = bs.BeautifulSoup(source,'lxml')

	skills = soup.find_all('div', class_='skill-selections')

	q = "<span>Q</span>"
	w = "<span>W</span>"
	e = "<span>E</span>"
	r = "<span>R</span>"

	leveling = ['','','','','','','','','','','','','','','','','','']

	def kkkk(id,tag,letter):
		level = [text for text in skills[id].find_all('div')]
		for i,qs in enumerate(level):
			qs = str(list(qs)[1])
			if tag == qs:
				leveling[i]= letter
	def buildorder(arrry):
		order = ""
		for i in range(len(arrry)):
			order += str(arrry[i])+","
		return order

	kkkk(1,q,"Q")
	kkkk(2,w,"W")
	kkkk(3,e,"E")
	kkkk(4,r,"R")
	mfbo = buildorder(leveling)
	kkkk(6,q,"Q")
	kkkk(7,w,"W")
	kkkk(8,e,"E")
	kkkk(9,r,"R")
	mwbo = buildorder(leveling)

	buildwrapper = soup.find_all('div', class_='build-wrapper')
	buildtext = soup.find_all('div', class_='build-text')

	def winrate(id):
		arrry = [text.text for text in buildtext[id].find_all('strong')]
		return  '=> {} Win Rate | {} Games'.format(arrry[0],arrry[1])

	items = [['Most Frequent Build '+winrate(7) , [url.get('data-id') for url in buildwrapper[0].find_all('img')]],
	         ['Highest Win % Build '+winrate(8) , [url.get('data-id') for url in buildwrapper[1].find_all('img')]],
	         ['Most Frequent Start '+winrate(9) , [url.get('data-id') for url in buildwrapper[2].find_all('img')]],
	         ['Highest Win % Start '+winrate(10) , [url.get('data-id') for url in buildwrapper[3].find_all('img')]],
	         ['Most Frequent - '+mfbo[:len(mfbo)-1], ['3340','3341','3364','3363','2055','3187','3185']],
	         ['Highest Win % - '+mwbo[:len(mfbo)-1] , ['2003','2031','2033','2138','2139','2140','2047']]]
	return items

def getchampions():
	source = urllib.request.urlopen('http://leagueoflegends.wikia.com/wiki/List_of_champions').read()
	soup = bs.BeautifulSoup(source, 'lxml')
	tables = soup.find_all('table')
	champions = []
	for td in tables[1].find_all('span'):
		a = td.get('data-champion')
		if a != None:
			champions.append(a)
	return champions

for champion in getchampions():
	items = get_items(champion,"Top")
	with open("{}/Recommended/{} Top.json".format(champion,champion), 'w') as f:
		f.write('''{\n  "title": "{}",\n  "type": "custom",\n  "map": "SR",  "mode": "any",\n  "priority": false,\n  "sortrank": {},\n  "champion": "{}",\n  "blocks": [\n    {\n      "items": [\n'''.format(champion+" Top Lane",1,champion))

		for item in items[2][1]:
			f.write('''        {\n          "count": 1,\n          "id": "{}"\n        },\n'''.format(item))
		f.write('''      ],\n      "type": "{}"\n    }\n    {\n      "items": [\n'''.format(items[2][0]))

		for item in items[3][1]:
			f.write('''        {\n          "count": 1,\n          "id": "{}"\n        },\n'''.format(item))
		f.write('''      ],\n      "type": "{}"\n    }\n    {\n      "items": [\n'''.format(items[3][0]))

		for item in items[0][1]:
			f.write('''        {\n          "count": 1,\n          "id": "{}"\n        },\n'''.format(item))
		f.write('''      ],\n      "type": "{}"\n    }\n    {\n      "items": [\n'''.format(items[3][0]))
		for item in items[1][1]:
			f.write('''        {\n          "count": 1,\n          "id": "{}"\n        },\n'''.format(item))
		f.write('''      ],\n      "type": "{}"\n    }\n    {\n      "items": [\n'''.format(items[3][0]))



#
# items = get_items("Akali","Top")
# for item in items[1]:
# 	print(item)
#
