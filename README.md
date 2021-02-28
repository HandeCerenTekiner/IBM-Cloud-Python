# IBM-Cloud-Python
Architectue of Example IoT Systems IBM Cloud &amp; Python

1. PuTTY program was downloaded and connected with galera.ii.pw.edu.pl.
Host Name (or IP address) = galera.ii.pw.edu.pl
2. Deployed Node-Red Application.
3. Logged in PuTTY using galera server by student account information.
4. WinSCP is downloaded then server and personal computer were connected. 
5. CloudApp.py source code is edited by the help of NodePad++.
6. Python libraries are downloaded which one is necessary.
7. Deployed IBM Watson IoT Platform and the instructer is added as a member to see the codes. 
8. Generated new API key for the Python Application. 
All authentication Data is created personal.
**My data details:**
organization = "vabw38"
appId = "myPythonApp"
authKey = "a-vabw38-n4wl0nlwdz"
authToken = "z1XqWMb4hxAd_zW-7r"
Created visualization of the data Using IBM Watson Iot Platform dashboard, and **"scl enable rh-python36 bash"** on terminal of Python. Then** “python3.6 myPythonApp.py” ** is written on the console.


Our current system pretty much like the architecture of the example IoT system. But instead of using real sensor tags and gateways, we are using a data generating nodes to our IBM cloud platform. We used Simplelink CC2650 SensorTags from Texas Instruments and Raspberry PI 3B for gateway.Simplelink CC2650 SensorTag is from Texas Instruments and is widely used in our faculty’s laboratories, it can be modified using Code Composer Studio. On the other hand, Raspberry PI 3 model B is a single board computer itself with wireless Lan and Bluetooth connectivity. For this system we have used MQTT internet protocol. If we were used real hardwares, we have to use Bluetooth as well. Mostly we have used MQTT protocol because MQTT is a M2M (Machine to machine) message query transport protocol and it is designed for lightweight/fast publish/subscribe messaging transport. Our system is protected by several authentication factors and passwords, however, any of the leak of auth token, or passwords may result of misuse and leak of private information. If we were using real hardware’s, we also must secure them in a lockable storage with a highly secured network. To improve the security of our current system, we may ask user for authentication of API key every time when he is connected to the system and We have to generate and use new API keys and passwords regularly in case of steal of this information and expire long sessions and log every connections/login when necessary. Also, we should not put our organization ID and API key information directly inside our python code, instead it should be encrypted and not readable. A backup for previous messages may also helpful in case of crashes.
