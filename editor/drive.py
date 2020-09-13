from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# this object here will help us in connection to google drive
gauth = GoogleAuth()
# loaded pre-exiting credentials file
gauth.LoadCredentialsFile("user_secrets.txt")


if gauth.credentials is None:
    # Authenticating user if there was no credential file and then saving in file user_secrets
    gauth.LocalWebserverAuth()
    gauth.SaveCredentialsFile("user_secrets.txt")
elif gauth.access_token_expired:
    # Refresh credentials if expired
    gauth.Refresh()
else:
    # Initialize the saved credentials
    gauth.Authorize()

drive = GoogleDrive(gauth)
file1 = drive.CreateFile({'title': 'Hello.txt'})
file1.SetContentString('Hello')
file1.Upload()


