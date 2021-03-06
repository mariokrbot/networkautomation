import requests
import json
import urllib3
import csv

from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings
from requests.auth import HTTPBasicAuth  # for Basic Auth

DNAC_URL = 'https://sandboxdnac2.cisco.com'
DNAC_USER = 'devnetuser'
DNAC_PASS = 'Cisco123!'

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

DNAC_AUTH = HTTPBasicAuth(DNAC_USER, DNAC_PASS)


def pprint(json_data):
    """
    Pretty print JSON formatted data
    :param json_data: data to pretty print
    :return None
    """
    print(json.dumps(json_data, indent=4, separators=(' , ', ' : ')))


def get_dnac_jwt_token(dnac_auth):
    """
    Create the authorization token required to access Cisco DNA Center
    Call to Cisco DNA Center - /api/system/v1/auth/login
    :param dnac_auth - Cisco DNA Center Basic Auth string
    :return Cisco DNA Center Auth Token
    """

    url = DNAC_URL + '/dna/system/api/v1/auth/token'
    header = {'content-type': 'application/json'}
    response = requests.post(url, auth=dnac_auth, headers=header, verify=False)
    response_json = response.json()
    dnac_jwt_token = response_json['Token']
    return dnac_jwt_token


def get_all_device_info(dnac_jwt_token):
    """
    The function will return all network devices info
    :param dnac_jwt_token: Cisco DNA Center token
    :return: Cisco DNA Center device inventory info
    """
    url = DNAC_URL + '/dna/intent/api/v1/network-device'
    header = {'content-type': 'application/json', 'x-auth-token': dnac_jwt_token}
    all_device_response = requests.get(url, headers=header, verify=False)
    all_device_info = all_device_response.json()
    return all_device_info['response']


def main():
    """
    This script will create a device_report.csv file with information about the Cisco DNA Center managed devices:
    This report will include device:
      - hostname
      - device type
      - software version
      - management IP address
      - serial number
    """

    print('')
    #  obtain the Cisco DNA Center Auth Token
    dnac_token = get_dnac_jwt_token(DNAC_AUTH)

    # get the all device details from Cisco DNA Center
    all_device_list = get_all_device_info(dnac_token)

    # verify if Cisco DNA Center manages any devices and how many
    device_count = len(all_device_list)

    if device_count == [0]:
        print('\nCisco DNA Center does not manage any devices')
    else:
        print('\nCisco DNA Center manages this number of devices: ', device_count)

        # retrieve the information about the devices and write to file

        # save information to file
        output_file = open('device_report.csv', 'w', newline='')
        output_writer = csv.writer(output_file)

        # loop through all devices list to collect the information needed in the report
        for device in all_device_list:
            device_hostname = device['hostname']
            device_type = device['type']
            device_software_version = device['softwareVersion']
            device_management_ip = device['managementIpAddress']
            device_sn = device['serialNumber']
            device_info = [device_hostname, device_type, device_software_version, device_management_ip, device_sn]
            output_writer.writerow(device_info)
        output_file.close()
        print('\n\nFile "device_report.csv" saved')

    print('\n\nEnd of application "device_report.py" run')


if __name__ == "__main__":
    main()