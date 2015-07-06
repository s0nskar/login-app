from pygithub3 import Github
import dropbox
from linkedin import linkedin

def menu_screen():
	print 'Want to login through???'
	print '1. Github'
	print '2. Dropbox'
	print '3. LinkedIn'

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

def Dropbox():
	app_key = #ADD APP KEY
	app_secret = #ADD APP SECRET

	flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

	authorize_url = flow.start()
	print 'First you have to authorize yourself'
	print '1. Go to: ' + authorize_url
	print '2. Click "Allow" or "login"(you might have to log in first)'
	code = raw_input("Enter the authorization code here: ").strip()

	access_token, user_id = flow.finish(code)

	client = dropbox.client.DropboxClient(access_token)
	print 'linked account: ', client.account_info()

def LinkedIn():
	API_KEY = #ADD API KEY
	API_SECRET = #ADD API SECRET
	RETURN_URL = 'http://localhost:8000'

	authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
	print authentication.authorization_url
	print 'open this url in browser and copy he authorization code'
	application = linkedin.LinkedInApplication(authentication)

	auth_code = raw_input("Enter authorization code: ")
	authentication.authorization_code = auth_code
	authentication.get_access_token()
	application.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations'])


done  = False
while not done:
	input = raw_input('')
	if input == '1':
		Github()
		done = True
	if input == '2':
		Dropbox()
		done = True
	if input == '3':
		LinkedIn()
		done = True
