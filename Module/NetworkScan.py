import nmap, os, json, sys

"""
    Extract a list of vulnerable ports accessible on your network using nmap
"""

DEFAULT_ARGUMENT = "-T5 -F"
    
def scanNetwork(ip):
    print(ip + ' Scan Start')
    rtnData = None
    try:
        nm = nmap.PortScanner()
        nm.scan(hosts=ip, arguments=DEFAULT_ARGUMENT)
        print(ip + ' Scan Complete')
        rtnData = nm.csv()
    except Exception as e:
        print(e)
    return rtnData
    
def resultWriter(ip, text):
    try:
        if not os.path.isdir('./tmp'):
            os.mkdir('./tmp')
        with open('./tmp/' + str(ip).split('/')[0], "w") as file:
            file.write(text)
    except IOError as e:
        print(e)
        
def startScan(ip):
    rtn = scanNetwork(ip)
    resultWriter(ip, rtn)