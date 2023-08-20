import os
from pathlib import Path

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

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
        return auth

    def list_files(self):
        file_list = self.gd.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        return file_list

    def upload_file(self, file_path, filename = None, gdrive_path = None):
        if gdrive_path is not None:
            folderName = gdrive_path
            folders = self.gd.ListFile(
                {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
            for folder in folders:
                if folder['title'] == folderName:
                    folder_id = folder['id']
            if filename is None:
                file = self.gd.CreateFile()
            else:
                file = self.gd.CreateFile({'title': filename})
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