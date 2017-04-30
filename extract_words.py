import nltk, re, pprint
from nltk import word_tokenize

# f = open('tweets.txt','r')

# f = str(f.read())

# tweets = f.split('&&')

# D = {}
# for tweet in tweets:
# 	try:
# 		tweet,datetime = tweet.split("~~")
# 		tweetid,tweet = tweet.split("***")
# 		print tweet,"\n\n"
# 		for each_word in tweet.split():
# 			try:
# 				D[each_word] = D[each_word]+1
# 			except:
# 				D[each_word]=1
# 	except:
# 		continue


# print D

f = open('onlytext.txt','r').read().decode('UTF-8').lower()
tokens = word_tokenize(f)
print (tokens)

from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
stop.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','#','@','rt','&','!','~'])
tokens = [i for i in tokens if i not in stop]
print len(tokens)
print tokens
