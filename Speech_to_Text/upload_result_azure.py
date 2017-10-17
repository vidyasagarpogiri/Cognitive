#connect to your storage account
from azure.storage.file import FileService
from azure.storage.file import ContentSettings
import os

# Set up
directory = os.fsencode('C:/Users/luopa/Desktop/Cognitive/result')
file_service = FileService(account_name='eyc3blob', account_key='8lWwXYYTbRtpg02HRd/DiVrSfyF4xNqtGmUzIy1GkLLOG1tXsXGLZG2KbDCz3XerLM1xPV4nl62YgmhAYAAUTQ==')

# Create result directory
# file_service.create_directory(share_name='eyc3file/speech', directory_name='result')

# Looping through the documents
generator = file_service.list_directories_and_files('eyc3file/speech')
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)
    file_service.create_file_from_path(share_name='eyc3file/speech',
                                  directory_name='result',
                                  file_name=filename,
                                  local_file_path='C:/Users/luopa/Desktop/Cognitive/result'+'/'+filename)
