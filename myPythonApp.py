# *****************************************************************************
# Copyright (c) 2014 IBM Corporation and other Contributors.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html 
#
# Contributors:
#   David Parker - Initial Contribution
# Modified for ESIT course by: 
#   Zbigniew Szymanski - 2020-06-07
# 
#DEVELOPED AND COMPLETED CODES 
# HANDE CEREN TEKINER - 308885
# *****************************************************************************
# Source:

import getopt
import signal
import time
import sys
import json
import ibmiotf.application
import seaborn as sns 

tableRowTemplate = "%-33s%-30s%s"
finished_work=False


#YOUR GLOBAL VARIABLES - begin

id = device_id,
aut_method = autMethod,
auth_key = a-vabw38-n4wl0nlwdz,
auth_token = z1XqWMb4hxAd_zW-7r,

url = 'https://node-red-htekiner.eu-gb.mybluemix.net/red/#flow/1f45fef6.4f8741'
page = requests.get(url)
dataContent = (page.content,'html.parser')
handle_data = data(id)
configFilePath = '/home/users/htekiner/cloudApp.py'
#YOUR GLOBAL VARIABLES - end


def mySubscribeCallback(mid, qos):
    if mid == statusMid:
        print("<< Subscription established for status messages at qos %s >> " % qos[0])
    elif mid == eventsMid:
        print("<< Subscription established for event messages at qos %s >> " % qos[0])
    
def myEventCallback(event):
    ed=event.data['d']
    print(ed)
    #YOUR CODE 1 - BEGIN

    client.connect()
    options = ibmiotf.application.ParseConfigFile(configFilePath)
    appClient = ibmiotf.application.Client(options)

    appClient.connect()
    appClient.subscribeToDeviceEvents()
    #...
    #if you are done with collecting data call stop_collecting
    #YOUR CODE 1 - END
    
def myStatusCallback(status):
    if status.action == "Disconnect":
        summaryText = "%s %s (%s)" % (status.action, status.clientAddr, status.reason)
    else:
        summaryText = "%s %s" % (status.action, status.clientAddr)
    print(tableRowTemplate % (status.time.isoformat(), status.device, summaryText))


def interruptHandler(signal, frame):
    client.disconnect()
    sys.exit(0)

def stop_collecting():
    global finished_work
    client.disconnect()

    #YOUR CODE 2 - BEGIN

    sns.set(color_codes=True)
    appClient = options.groupby('device_id').sort_values
    plt.title('Visualization Data')
    fig, ax = plt.subplot(figSize=(2,30));
    plt.show()


    #process and visualize collected data
    #...
    #YOUR CODE 2 - END

    finished_work=True

def usage():
    print(
        "simpleApp: Basic application connected to the IBM Internet of Things Cloud service." + "\n" +
        "\n" +
        "Options: " + "\n" +
        "  -h, --help          Display help information" + "\n"
    )

#only executed when code run as standalone program
if __name__ == "__main__":
    signal.signal(signal.SIGINT, interruptHandler)
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:I:a", ["help","deviceid=","appid="])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    #YOUR CODE 3 - BEGIN

    organization = "vabw38"
    appId = "myPythonApp"
    authKey = "a-vabw38-n4wl0nlwdz"
    authToken = "z1XqWMb4hxAd_zW-7r"

    #YOUR CODE 3 - END

    authMethod = None
    configFilePath = None
    deviceType = "ESIT_device_type"
    deviceId = "+"
    event = "+"
    
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-I", "--deviceid"):
            deviceId = a
        elif o in ("-a", "--appid"):
            appId = a
        else:
            assert False, "unhandled option" + o

    client = None
    options = {"org": organization, "id": appId, "auth-method": authMethod, "auth-key": authKey, "auth-token": authToken, "clean-session": True}
    try:
        client = ibmiotf.application.Client(options)
        # If you want to see more detail about what's going on, set log level to DEBUG
        # import logging
        # client.logger.setLevel(logging.DEBUG)
        client.connect()
    except ibmiotf.ConfigurationException as e:
        print(str(e))
        sys.exit()
    except ibmiotf.UnsupportedAuthenticationMethod as e:
        print(str(e))
        sys.exit()
    except ibmiotf.ConnectionException as e:
        print(str(e))
        sys.exit()

    
    print("(Press Ctrl+C to disconnect)")
    
    client.deviceEventCallback = myEventCallback
    client.deviceStatusCallback = myStatusCallback
    client.subscriptionCallback = mySubscribeCallback
    eventsMid = client.subscribeToDeviceEvents(deviceType, deviceId, event)
    statusMid = client.subscribeToDeviceStatus(deviceType, deviceId)

    print("=============================================================================")
    print(tableRowTemplate % ("Timestamp", "Device", "Event"))
    print("=============================================================================")
    

    while True:
        time.sleep(1)
        if finished_work==True:
            sys.exit(0)
        
