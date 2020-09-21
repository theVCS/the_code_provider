from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# id container ---- this dictionary will contain all the folder ids
file_locator = {
    "codeforces": {
        "c": "15N0wYUmgzYWMCnSCUFn3GBbywDVaJqyJ",
        "cpp": "1vZogqyO5yI5sDpLJpgOakT5Ur0kx01Ko",
        "python": "16ZfrzwMgZ_3poKQWAaDtQklVIHjw_-4b",
        "java": "1r3RnNGZArF5UQV2Obp3gGUrK9-XtFv9j",
    },
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


def upload(file_name, data, website, language):
    """this will upload a file to drive with file_name as title and content as data and return the file_name"""
    drive = GoogleDrive(gauth)
    file = drive.CreateFile({'title': file_name, 'parents': [{'id': file_locator[website][language]}]})
    file.SetContentString(data)

    # in-built function used to upload data to the drive
    file.Upload()
    return file['title']


def get_content(website, language, file_name):
    """this function will return the data inside the files which have title like file_name"""
    drive = GoogleDrive(gauth)
    file = drive.ListFile({'q': "'" + file_locator[website][language] + f"' in parents and title contains '{file_name}' and trashed=false"}).GetList()[0]
    return file.GetContentString()


def sharing_code(data, language, file_name):
    """this will upload a file to drive with file_name as title and content as data and return the file_name"""
    drive = GoogleDrive(gauth)
    file = drive.CreateFile({'title': file_name, 'parents': [{'id': file_locator["sharing"]}]})
    file.SetContentString(data)

    # in-built function used to upload data to the drive
    file.Upload()
    return file['title']


def show_shared(id):
    """this function will show the content inside the shared code"""
    drive = GoogleDrive(gauth)
    file = drive.ListFile({'q': "'" + file_locator["sharing"] + f"' in parents and title = '{id}' and trashed=false"}).GetList()
    return file[0].GetContentString()


def edit(data, website, language, file_name):
    """this will upload a file to drive with file_name as title and content as data and return the file_name"""
    drive = GoogleDrive(gauth)
    file = drive.ListFile({'q': "'" + file_locator[website][language] + f"' in parents and title contains '{file_name}' and trashed=false"}).GetList()[0]
    file.SetContentString(data)

    # in-built function used to upload data to the drive
    file.Upload()
    return file['title']


if __name__ == '__main__':
    # print(upload("file_name", "data", "codeforces", "c"))
    # print(upload("prince.c", "prince is a good boy"))
    get_content("codeforces", "c", "prince")

