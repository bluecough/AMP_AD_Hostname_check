## AMP AD Hostname Check
## Check AD and then call AMP to see if the hostname is also in AMP
## Authors: George Seeto, Chantel Strickland, Dave Schwartberg
##

import sys, requests, json

def main():
    # Get the input args
    client_id = sys.argv[1]
    api_key = sys.argv[2]
    csvfilename = sys.argv[3]

    host = "api.amp.cisco.com/v1"
    url = f"https://{client_id}:{api_key}@{host}/computers?hostname[]="

    # Read in CSV file
    csvfile = open(csvfilename, 'r')
    count = 0
    for line in csvfile:
        count += 1
        line = line.strip('\n')
        line = line.replace('"','')
        get_amp_host(line, url)

    #get_amp_host("Andromeda", url)

def get_amp_host(name, url):
    print(url + name)
    response = requests.get(url + name, verify=False)
    decode_response = response.json()
    try:
        print(decode_response['data'][0]['hostname'] + " | " + decode_response['data'][0]['connector_guid'])
    except:
        print("name " + name + " not found")

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
