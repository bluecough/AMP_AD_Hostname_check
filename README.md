AMP_AD_Hostname_check
=====================

This script will allow you to get a list of computer names in your AzureAD and compare those to connectors in Cisco's Secure Endpoints.

##Assumption
==========

- AzureAD Connect is installed in your environment and you are sync'ing your devices to your Azure Tenant

##Getting AzureAD List of Machines
================================

- Open a powershell on your Windows 10 workstation and make sure you install the AzureAD module

```
PS c:\Users\user> Install-Module -name AzureAD
```
