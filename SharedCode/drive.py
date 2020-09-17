from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# id container ---- this dictionary will contain all the folder ids
file_locator = {
    "sharing": "1V8za1ulCVItrgH38sEW69yLsI65gebTQ"
}

# this object here will help us in connection to google drive
gauth = GoogleAuth()
# loaded pre-exiting credentials file
gauth.LoadCredentialsFile("user_secrets.txt")

# connecting to the google drive
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


def show_shared(id):
    """this function will show the content inside the shared code"""
    drive = GoogleDrive(gauth)
    file = drive.ListFile({'q': "'" + file_locator["sharing"] + f"' in parents and title = '{id}' and trashed=false"}).GetList()
    print(file[0].GetContentString())
    return file[0].GetContentString()


