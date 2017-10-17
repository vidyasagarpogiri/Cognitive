# Code Usage
- Transcibe_v1.py: Batch processing of the .wav audio files from local folder using google speech-to-text API, use it in gcloud shell, the <transcribe_gcs(gcs_uri)> function is not working properly yet
```
python C:\Users\luopa\Desktop\Cognitive\transcribe2.py C:/Users/luopa/Desktop/Cognitive/azure_audioclips
```
- blobxfer.py: Used in command prompt for interaction with Azure Blob, use it in command prompt
```
python C:\Users\luopa\Desktop\Cognitive\blobxfer.py synapsediag693 bootdiagnostics-pauline-b3337233-6ea6-4969-83fb-6c9aa4dc38f8 C:\Users\luopa\Desktop\Cognitive --subscriptionid 438f52a6-38d6-4dcd-964c-9c6d97b3877f438f52a6-38d6-4dcd-964c-9c6d97b3877f --storageaccountkey sIfK/fOUQePs/NI2eETgDUhXVrr+gNQ4/3Ni4hg0ObLGOBDbXytZLFbeWYUljTHJRqIDt5xYkyXWi47V2BdEdg== --managementcert C:\Users\luopa\Desktop\Cognitive\Azure_Blob_Cert.cer --remoteresource pauline.b3337233-6ea6-4969-83fb-6c9aa4dc38f8.screenshot.bmp --download
```
- google_speech_streaming.py: Used for transcribing recording in real-time, use in gcloud shell, wait for 2-3 seconds and start speaking to the microphone, set ```interim_results=False``` to get the complete result after the completion of speech. Note that if <interim_results> is set to True, speaking without pausing after each sentence will lead to messy result being produced. There is also an **one miniute** limitation on the maximum length of speech each time.
```
python C:\Users\luopa\Desktop\Cognitive\google_speech_streaming.py
```
- download_from_azure.py: Used for downloading audio files to local machine
- upload_result_azure.py: Used for uploading the transcription results from local machine back to Azure file storage


# Python Library
- azure-storage
- auzure-servicemanagement-legacy
- azure-common
- blobxfer
- argparse
- pydub

# Process for Demo
1. Use **download_from_azure.py** to fetch all files sitting in the target directory to a local directory
2. Run **Transcribe_v1.py** in Google Cloud SDK Shell to convert stereo .wav files to mono .wav files. In the meanwhile the mono files will be read in and being passed to google speech-to-text API. The results will be generated as .txt file for each audio files.
```
python C:\Users\luopa\Desktop\Cognitive\transcribe2.py C:/Users/luopa/Desktop/Cognitive/azure_audioclips
```
3. Upload the result to Azure file storage using **upload_result_azure.py**

# Reference
Azure Blob Storage: https://docs.microsoft.com/en-us/azure/storage/blobs/storage-python-how-to-use-blob-storage
