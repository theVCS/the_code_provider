from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

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


# this will upload a file to drive with file_name as file_name and content as data
def upload(file_name, data):
    drive = GoogleDrive(gauth)
    file = drive.CreateFile({'title': file_name, 'parents': [{'id': '1dIPZn_MhHrBi-1YkhZuXKUSiawr3wEqC'}]})
    file.SetContentString(data)
    file.Upload()
    return file['id']


if __name__ == '__main__':
    print(upload("prince.c", "prince is a good boy"))
