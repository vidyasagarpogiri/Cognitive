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
# Python Library
- azure-storage
- auzure-servicemanagement-legacy
- azure-common
- blobxfer
- argparse
- pydub
