#connect to your storage account
from azure.storage.file import FileService
from azure.storage.file import ContentSettings
import os

file_service = FileService(account_name='eyc3blob', account_key='8lWwXYYTbRtpg02HRd/DiVrSfyF4xNqtGmUzIy1GkLLOG1tXsXGLZG2KbDCz3XerLM1xPV4nl62YgmhAYAAUTQ==')
generator = file_service.list_directories_and_files('eyc3file/speech')
for file in generator:
    print(file.name)
    file_service.get_file_to_path(share_name='eyc3file/speech',
                                  directory_name=None,
                                  file_name=file.name,
                                  file_path='C:/Users/luopa/Desktop/Cognitive/azure_audioclips'+'/'+file.name)