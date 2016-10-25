from bs4 import BeautifulSoup
from datetime import datetime
import webbrowser
import time
import re
from vaderSentiment.vaderSentiment import sentiment as vs
from sets import Set

start = time.time()

# soup = BeautifulSoup(open("/Users/markdawson/Dev/data-science-python/fb_data/messages.htm"), "html.parser")
soup = BeautifulSoup(open("../html/messages.htm"), "lxml")

number_of_messages = soup.find_all('p')
# Only focus right now on 2 person conversations

# def output(soup):

# 	thread = soup.find(attrs={"class":"thread"})

# 	while next_thread.next_sibling and i < 100000:
		
# 		messages = thread.children
# 		members = next(messages) # Members are always the first child of a thread

# 		for header in messages:
# 			# structure is 
# 			# header -> message -> header -> message -> header -> message

# 			user = header.find(attrs={"class":"user"})
# 			date_text = header.find(attrs={"class":"meta"}).text
# 			date_text = date_text + '00'
# 			date = datetime.strptime(date_text, "%A, %B %d, %Y at %I:%M%p %Z%z")
# 			message = next(messages)

# 			#increment
# 		i += 1
# 		thread = thread.next_sibling

def help():
	print('Available commands:')
	print('people()')
	print('convosWith(name)')
	print('messagesWith(name)')
	print('positiveWith(name)')
	print('negativeWith(name)')

def people():
	people = soup.find_all(attrs={"class":"user"})
	output = Set()
	for p in people:
		if p not in output:
			output.add(p.string)

	for p in output:
		print(p)

	print('Found messages from ' + str(len(output)) + " people.")

def convosWith(name,soup=soup):
	"""Get all threads with the name passed in"""
	
	threads = soup.find_all(attrs={"class":"thread"})
	convos = []
	for t in threads:
		ch = t.children
		members = next(ch)
		members_list = members.split(',')
		#print(members)
		# if len(members_list) == 2 and name in members_list[0]:
		if name in members_list[0]:
			convos.append(members.parent)
			print('')	
			print(members)
			print("(Thread started on " + next(ch).find(attrs={"class":"meta"}).string + ")")

	return #convos

def p(text):
	return "<p>" + str(text) + "</p>"

def messagesWith(name,soup=soup):
	
	threads = soup.find_all(attrs={"class":"thread"})
	convo = None
	for t in threads:
		messages = t.children
		members = next(messages)
		members_list = members.split(',')
		#print(members)
		if len(members_list) == 2 and name in members_list[0]:
			break

	filename = 'messagesWith_' + name + '.html'
	f = open(filename,'w')
	html_text = "<html><head></head><body><h1>Message Log</h1>"
				
	for header in messages:
		user = header.find(attrs={"class":"user"})
		date_text = header.find(attrs={"class":"meta"}).text
		date_text = date_text + '00'
		#date = datetime.strptime(date_text, "%A, %B %d, %Y at %I:%M%p %Z%z")
		message = next(messages)

		print(user.string)
		print(date_text)
		print(message.string)
		try:
			print(vs(message.string))
		except:
			print("Couldn't get sentiment")
		print("-------------")

		html_text += "<hr>"
		html_text += p(user.string)
		html_text += p(date_text)
		html_text += p(message)

	
	html_text+="</body></html>"

	f.write(html_text)
	f.close()

def negativeWith(name, soup=soup, emotion="neg"):
	return emotionWith(name, soup, emotion)

def positiveWith(name, soup=soup, emotion="pos"):
	return emotionWith(name, soup, emotion)

def emotionWith(name, soup, emotion):
	threads = soup.find_all(attrs={"class":"thread"})
	convo = None
	for t in threads:
		messages = t.children
		members = next(messages)
		members_list = members.split(',')
		#print(members)
		if len(members_list) == 2 and name in members_list[0]:
			break

	f = open('helloworld.html','w')
	html_text = "<html><head></head><body><h1>Message Log</h1>"
	
	# messages = [m for m in messages]	
	# # Eventually I'll want to create a list so that I can 
	# # give context for these messages		

	for header in messages:
		user = header.find(attrs={"class":"user"})
		date_text = header.find(attrs={"class":"meta"}).text
		date_text = date_text + '00'
		#date = datetime.strptime(date_text, "%A, %B %d, %Y at %I:%M%p %Z%z")
		message = next(messages)
		
		
		try:
			if vs(message.string)[emotion] > 0.2:
				print("----------")
				print(user.string)
				print(date_text)
				print(message.string)
				print(vs(message.string))
				print('')
		except:
			pass


end = time.time()
print('Processed ' + str(len(number_of_messages)) + ' messages in ' + str(int(end - start)) + ' seconds')
print('Type help() for a list of commands.')
