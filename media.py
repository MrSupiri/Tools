import os
def exe(cmd):
	f = os.popen(cmd)
	out = f.read()
	#print(out)
	return out

def fuck(out):

	artists = 'error'
	name = 'error'
	try:
		for o in out:
			if 'Artists                                  :' in o:
				artists = o.split(':')[1].strip(" ")
			elif 'Track name                               : ' in o:
				name = o.split(':')[1].strip(" ")
	except:
		pass
	return artists,name

files = exe('ls /mnt/usb/Music/Favourites')
lis = []
for file in files.split('\n'):
	try:
		out = exe("mediainfo '''/mnt/usb/Music/Favourites/"+file+"'''| grep -E 'Track name|Artists'| sort")
		out = out.split('\n')
		artists, name = fuck(out)
		filen = out.split('.')[-1]
		if name != "error" and name != "error":
			data = "%-100s"%(file[:100].format(width = 100))+" "+"================>"+" "+artists+" - "+name+"."+filen
			lis += [data]
	except:
		#print('ERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRROO - ',file)
		pass
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

for li in lis:
	print(li)








# out = exe("mediainfo '/mnt/usb/Music/Favourites/02-akon-beautiful_ft._colby_odonis_and_kardinal_offishall @ RAZE WAVE.COM.mp3'| grep -E 'Track name|Artists'| sort")
# out = out.split('\n')
# artists = out[1].split(':')[1].strip(" ")
# name = out[4].split(':')[1].strip(" ")



#print(artists," - ",name)
#print(artists)



