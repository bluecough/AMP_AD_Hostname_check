AMP_AD_Hostname_check
=====================

This script will allow you to get a list of computer names in your AzureAD and compare those to connectors in Cisco's Secure Endpoints.

Download the Windows [Executable](https://github.com/bluecough/AMP_AD_Hostname_check/releases/tag/v1)

## Assumption


- AzureAD Connect is installed in your environment and you are sync'ing your devices to your Azure Tenant

## Getting AzureAD List of Machines

- Open a powershell on your Windows 10 workstation and make sure you install the AzureAD module

```
PS c:\Users\user> Install-Module -name AzureAD
```
- Authenticate to your AzureAD tenant
```
PS c:\Users\user> Connect-AzureAD
```
- Now create a CSV list of computers using the following Powershell command
```
PS c:\Users\user> Get-AzureADDevice | Select-Object -Property DisplayName | Export-Csv -Path .\computers.csv
```

## Run the python Script
- Make sure the CSV is in the same directory as the executing script or alternatively run the Windows Executable.

```
amp_ad_hostname.exe <client_id> <client_secret> <csvfile_name>
```
