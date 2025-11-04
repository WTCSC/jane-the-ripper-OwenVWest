# Jane the Ripper README:
### Requirements:
* Python3

### Installation:
* Download the "_JaneTheRipper.py_" File and the "_JaneTheTest.py_" File  
###### (make sure they are downloaded as python files)
* Open in IDE of choice
* run using python  
Or  
Run: "git clone https://github.com/WTCSC/jane-the-ripper-OwenVWest.git"

### Testing: 
To test that the program is running properly, run the command "pytest -s JaneTheTest.py"  

### Input examples:
###### (While having the "hashes.txt" and "wordlist.txt" files installed)
Using the provided "hashes.txt" file for the hash list input and the provided "wordlist.txt" file for the words list input aswell as using the md5 hash option should return:
* [+] Succeeded, fe546279a62683de8ca334b673420696 --> samsung
* [+] Succeeded, aa47f8215c6f30a0dcdb2a36a9f4168e --> daniel
* [+] Succeeded, f4f068e71e0d87bf0ad51e6214ab84e9 --> angel
* [+] Succeeded, a53f3929621dba1306f8a61588f52f55 --> edward
* [+] Succeeded, bf779e0933a882808585d19455cd7937 --> charlie
* [+] Succeeded, 21b72c0b7adc5c7b4a50ffcb90d92dd6 --> matrix
* [+] Succeeded, 40be4e59b9a2a2b5dffb918c0e86b3d7 --> welcome
* [+] Succeeded, c33367701511b4f6020ec61ded352059 --> 654321
* [+] Succeeded, eb0a191797624dd3a48fa681d3061212 --> master
* [+] Succeeded, e99a18c428cb38d5f260853678922e03 --> abc123
As the sucsessfull hash cracks.
###### If the input shown is "failure" that means the input you gave for the hash type is not a valid option for this program
Invalid file paths will cause the program to fail
### Functionality of the program:
![actiontreee](https://github.com/WTCSC/jane-the-ripper-OwenVWest/blob/main/decisiontree.png)
