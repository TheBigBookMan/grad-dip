## Multi-Factor Auth (MFA)
- **Usernames and passwords**- used for logging in
- **Factors**- pieces of eveidence that prove identity
	- **Single factor auth**- one of these types of factors (usually username and password (knoweldge factor))
	- **Multi- factor aiuth**- multiple types of factors to login to an app
	- 4 types of factors to login- more factors you use is greater security and harder to fake an identity
		- **Knowledge**- factor that you know like username and password
		- **Possesssion**- something you have like a bank card, MFA device/app
		- **Inherent**- something you are, finger print, voice identification, iris scan
		- **Location**- physical location (coordinates) or network  when you're logging in
- AWS generates the secret key and additional information and needs to be added into a MFA (google authenticator etc)
	- secret key and additional info creates QR code
	- QR code scanned which adds the key and info within the app into the MFA
	- 2 users means 2 MFA- 2 different virtual devices for dfferent accounts/services
- Production use hardware

## Budget
- closely monitor spending and set alarms for spending so you don't go over
- can send pdfs and emails to an email about the alerts
- have to do in a production environment