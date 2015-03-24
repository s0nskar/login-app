from pygithub3 import Github

def menu_screen():
	print 'Want to login through???'
	print '1. Github'

def Github():
	uname = raw_input('Enter Username: ')
	passw = raw_input('Enter password: ')
	gh = Github(login=uname, password=passw)

	user = gh.users.get()
	repos = gh.repos.list().all()
	follower = gh.users.followers.list()
	emails = gh.users.emails.list()

	print user
	for items in repos:
		print items
	for items in follower:
		print items
	for items in emails:
		print items

done  = False
while not done:
	input = raw_input('')
	if input == '1':
		Github()
		done = True