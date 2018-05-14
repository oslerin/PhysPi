# PhysPi
Code for the environmental monitoring system I developed and implemented for my fourth year honours project in physics at Carleton University.

***PLEASE NOTE THAT THIS REPO IS LARGELY INCOMPLETE AND MORE DETAILED DIAGRAMS AND TUTORIALS WILL BE ADDED IN THE COMING WEEKS***

***For an extremely detailed description of the project and the underlying physics, consult the PDF file in this repo which is my thesis paper for this project.***

# Background
The PhysPi is a temperature and humidity monitoring system currently in use at the Carleton University Department of Physics in Ottawa, ON to aid in the construction and testing of silicon microstrip sensors for the ATLAS-ITk upgrade at CERN's Large Hadron Collider (LHC).  In preparation for a high-luminosity upgrade to the LHC, the innermost part of the ATLAS detector is being reconstructed as the Inner Tracker (ITk) which will implement silicon microstrip and micropixel sensors for more accurate measurements in physics research.  Much of the construction of the microstrip sensors is happening at Carleton University, and involves materials which are extremely sensitive to even the slightest changes in the temperature and humidity of their surroundings.  Thus, it is necessary to implement a system which accurately measures, records and analyzes these changes.
# Hardware Overview
The PhysPi system first wires two digital temperature and humidity sensors (Sensirion SHT75 series) to an Arduino Uno board where values of time, date, temperature and humidity are taken. The Arduino is then connected in serial (USB) to a Rapsberry Pi 3B, which carries out the majority of the software procedures explained next.
# Software Overview
Initially, an Arduino Program (2sht.ino) defines the measurement of data from the sensors as well as the process by which this occurs.  Next, a program connects the Arduino to the Raspberry Pi (2sht.py). Next the 
