# pfpCapstone
MIDN Dan Beverly, Nick Falsey, Young Kim, Eugene Om, and Gage Vernon's AY22 SCY Capstone

Welcome to our capstone!

# Description
This capstone was inspired by our work in SY202: Cyber Systems Engineering. There are several valid security concerns surrounding many legacy industrial control systems (ICS) and supervisory control and data acquisition (SCADA) systems. With limited ability to install or upgrade modern intrusion detection and prevention systems, industrial system security can be difficult to ensure. 

Using PFP Cybersecurity's implementation of an artificial intelligence integrity-assurance software and hardware suites, we wanted to determine the viability of incorporating monitoring capabilities to everything from modern IOT devices to larger-scale ICS and SCADA systems. You can read more about their developments here: https://www.pfpcyber.com/

In addition, read more about our backgroud research, implementation, and testing in our capstone report.

# System Design
![systemSchematic](https://user-images.githubusercontent.com/60118678/161191715-77e60928-6add-40e7-8f99-04fb18b73ff6.png)
The system is suprisingly simple, and we estimate it to be reasonably scalable for what our research entailed. On the defensive system, the PFP Cybersecurity pMon 751 uses its sensor to monitor the CPU of the Raspberry Pi3. Its live results are read by PFP's server, which is running on the localhost. 

Using the API designed in conjunction with the server, we run workingRemediation.py also on the defensive system. It constantly reads stream output from the server and compares results, looking for an abnormal signal. Upon receiving such a signal, it sends the reboot signal to the Pi.

On the Pi, the receive.py program is running, listening for the reboot signal. When the Pi successfully reboots, it sends its own signal back to the defensive system.

Also on the Pi, we concurrently run badram.py at a random point. This simulates an attack or otherwise erroneous behavior of the system, triggering the feedback system. When badram.py starts, it sends its own signal back to the defensive host to signal that an 'attack' has started. 

The signals aid in the overall function of the system, but also in timing. When badram.py first starts, it sends a signal to the defensive sytem to begin timing. When the defensive system detects the anomaly and sends the reboot signal, it gets it first metric of remediation time. Then, when the Pi successfully reboots, it gets its second metric of total reboot time. The reboot time is very specific to the system itself (the Pi in this case), but this framework could be used for any number of systems to get further data.

# Testing Flow
Our testing procedure went as follows:
  1. On defensive host (Linux laptop): PowerFingerprinting pMon751 running and sending results into the P3Server
  2. On target host (Pi): receive.py running and waiting to recieve signal from the defensive host
  3. On defensive host (Linux laptop): begin running workingRemediation.py, which is waiting for detected strange activity
  4. On target host (Pi): begin running badram.py, overloading the CPU with a lot of activity

Assuming everything works as intended, the Pi recieves the 'reboot' signal and the simulated attack is averted.

# Video
https://user-images.githubusercontent.com/60118678/160965346-85df41bd-d830-411d-98bb-81d9ed6d8deb.mp4

