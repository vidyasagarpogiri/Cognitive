1. Download [windows SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk) to get "makecert.exe":
2. Navigate to the makecert.exe directory on cd C:\Program Files (x86)\Windows Kits\10\bin\x64
3. Make certificate using command: 
```
makecert -sky exchange -r -n "CN=P2SRootCert" -pe -a sha256 -len 2048 -ss My
```
4. Find certifate being made by opening  Manage user certificates> Certificates-Current User >Personal > Certificates
5. Upload the certificate to Azure by 
  *Click All Tasks, and then click Export. This opens the Certificate Export Wizard.
  *In the Wizard, click Next. Select No, do not export the private key, and then click Next.
  *On the Export File Format page, select Base-64 encoded X.509 (.CER)., and then click Next.
  *On the File to Export, Browse to the location to which you want to export the certificate. For File name, name the certificate file. Then, click Next.
  *Click Finish to export the certificate. You see The export was successful. Click OK to close the wizard
