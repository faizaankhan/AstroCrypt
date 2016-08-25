# ASTROCRYPT
 
 AstroCrypt is an cryptographic encryption-decryption tool written in Python which uses AES-CBC encryption technique. It uses the AES-256-CBC cipher and encodes the encrypted data with Base64. In simple terms, user can use the tool to encrypt their files whatsoever it may be, for example a text file , an image, an audio-video file , a pdf , or a typical openXML with a password and can keep them safe until it is decrypted using the same password.
 
# SOFTWARE REQUIREMENTS

A standalone version is available for the tool , still if you want to use the tool by 
using the source code you require to have the below packages in your system.

1. Python 2.7+
2. PyCrypto
3. Tkinter

For links and installation guideline follow the next topic.

# INSTALLATION


A.  Using the direct executable to run:

	A standalone executable file is being made available if user wants to run the tool without installing 
	other softwares as required.
	

B. Using the tool in a windows operating system by running the source code:


1. Download and install Python 2.7

	1.a. Download link : https://www.python.org/downloads/
	
	1.b. Add the Python27 folder in your Environment Variable list.
	
2.  Download and install Tkinter libraries

	2.a. Download link : http://www.activestate.com/activetcl/downloads
	
	2.b. Follow the instructions to install tkinter. Active tcl includes tcl, tk and other libraries required 
	
3. Download and install PyCrypto

	3.a. Download link : https://pypi.python.org/pypi/pycrypto
	
	3.b. Copy it to the Python27 folder , unzip the file, and run the following commands in the cmd after changing the current directory position to the PyCrypto folder.
	
	3.c. The modules are packaged using the Distutils, so you can simply run “python setup.py build” to build the package, and “python setup.py install” to install it.  
	
4. To run AstroCrypt

	4.a. Open cmd

	4.b. Change the current directory to the directory containing the AstroCrypt.py file.
	
	4.c. Run command : python AstroCrypt.py
	
  
  	
C. Using the tool in a Linux operating system by running the source code:

1. Install Tkinter

	1.a. In Ubuntu \ Debian \ Kali : sudo apt-get install python python-tk 
	
	1.b. In Fedora \ RedHat \ CentOS : sudo yum install tkinter
	

2. Download and install PyCrypto

	2.a. Run the following command :
	
		pip install pycrypto
		
3. To run AstroCrypt

	3.a. Open terminal
	
	3.b. Change the current directory to the directory containing  the AstroCrypt.py file.
	
	3.c. Run command : python AstroCrypt.py
	


