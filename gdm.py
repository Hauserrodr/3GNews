import os
from pathlib import Path

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client._helpers import scopes_to_string

from loguru import logger

# Find this script directory
script_dir = Path( __file__ ).parent.absolute()
base_dir = Path( __file__ ).parent.parent.absolute()


class GoogleDriveManager:
    def __init__(self):
        logger.info('Initializing GoogleDriveManager...')
        self.auth = self._generate_auth()
        self.gd = GoogleDrive(self.auth)
        self.list_files() # Just for triggering authentication when the bot starts!
        logger.success('Successfully authenticated and initialized GoogleDriveManager.')

    def _generate_auth(self):
        auth = GoogleAuth()
        # Try to load saved client credentials
        auth.LoadCredentialsFile(os.path.join(script_dir,"gdrive_creds.txt"))

        if auth.credentials is None:
            # Authenticate if they're not there

            # This is what solved the issues:
            auth.GetFlow()
            auth.flow.params.update({'access_type': 'offline'})
            auth.flow.params.update({'approval_prompt': 'force'})

            auth.LocalWebserverAuth()

        elif auth.access_token_expired:

            # Refresh them if expired

            auth.Refresh()
        else:

            # Initialize the saved creds

            auth.Authorize()

        # Save the current credentials to a file
        auth.SaveCredentialsFile(os.path.join(script_dir,"gdrive_creds.txt")  )
        return auth

    def list_files(self):
        file_list = self.gd.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        return file_list

    def list_files_in_folder(self, folderName):
        folders = self.gd.ListFile(
            {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
        for folder in folders:
            if folder['title'] == folderName:
                folder_id = folder['id']
                break
        query = f"'{folder_id}' in parents and trashed=false"
        file_list = self.gd.ListFile({'q': query}).GetList()
        return file_list

    def upload_file(self, file_path, filename = None, gdrive_path = None):
        folder_id = None
        if gdrive_path is not None:
            folderName = gdrive_path
            folders = self.gd.ListFile(
                {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
            for folder in folders:
                if folder['title'] == folderName:
                    folder_id = folder['id']
            if filename is None:
                file = self.gd.CreateFile({'parents': [{'id': folder_id}]})
            else:
                file = self.gd.CreateFile({'title': filename, 'parents': [{'id': folder_id}]})
        else:
            if filename is None:
                file = self.gd.CreateFile()
            else:
                file = self.gd.CreateFile({'title': filename})
        file.SetContentFile(file_path)
        file.Upload()
        file.InsertPermission({
            'type':  'anyone'
            ,'value': 'anyone'
            ,'role':  'reader'
        })
        # return file['alternateLink']
        embed_link = file['embedLink']
        image_id = embed_link.split('/d/')[-1].split('/')[0]
        src_link = f'https://drive.google.com/uc?export=view&id={image_id}'
        return src_link