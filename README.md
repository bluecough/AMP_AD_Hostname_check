AMP_AD_Hostname_Check
=====================

This script will allow you to get a list of computer names in your AzureAD or Local AD and compare those to connectors in Cisco's Secure Endpoints.

Download the Windows [Executable](https://github.com/bluecough/AMP_AD_Hostname_check/releases/tag/v1)

## Assumptions


- AzureAD Connect is installed in your environment and you are sync'ing your devices to your AzureAD Tenant.
- On premise AD Command is also below. However, you will need to have RSAT Tools installed on your Windows Desktop.

## Getting AzureAD List of Machines

- Open a powershell on your Windows 10 workstation and make sure you install the AzureAD module. You will need to run Powershell as an Administrator to install modules.

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

## Getting local AD list of machines
```
PS c:\Users\user> Import-Module -name ActiveDirectory
PS c:\Users\user> $cred = Get-Credential
PS c:\Users\user> Get-ADComputer -Filter * -credential $cred | Select-Object -Property Name | Export-Csv -Path .\computers.csv
```

## Run the python script or executable
- Make sure the CSV is in the same directory as the executing script or similarly run the Windows Executable. The client_id and client_secret can be gotten in the AMP console under the API menu drop down. You only need read access for that API key.

```
amp_ad_hostname.exe <client_id> <client_secret> <csvfile_name>
```
## Sample output
![](https://github.com/bluecough/AMP_AD_Hostname_check/blob/master/images/sample.png)

# Authors & Maintainers
George Seeto, Chantel Strickland, Dave Schwartzberg

# License
This project is licensed to you under the terms of the [Cisco Sample Code License](https://github.com/bluecough/AMP_AD_Hostname_check/blob/master/LICENSE)
