import urllib
import json

print '\n'
print "*"*75
print '\t'*5 + 'DICTIONARY'
print "*"*75

word = raw_input("\nEnter word to search : ")
url= "https://glosbe.com/gapi/translate?from=eng&dest=eng&phrase="+word+"&format=json&pretty=true"
result=json.load(urllib.urlopen(url))

if not result["authors"]:
	print "\nPlease check the word!!!"
else:
	print "\nMeaning : "+result["tuc"][0]["meanings"][0]["text"]
print"\n"
