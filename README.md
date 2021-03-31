# SY402_Lab8

Overview:
In this Lab, I will be taking the files on my system and running it through a hash.py script to recursively hash it. There will be some files that will be ignored in hashing. When hash.py is run, it will store at least, the filename with full path, the hash, and the date and time that it was observed. 

My Solution: 
For the first part, I checked to see if there was a file called "hashinfo.csv". And if there was, it moved onto the next part. 
The next part read through the lines of the file and split the file by the comma. It then assigned the second part of the list to a variable because that will be used later to check if there has been any changes made. The code runs through the system and prints out the files and directories of each thing in my system except for the list I created at the top of those that need to be ignored. Then I assgin variables to the file name, the hash, and the time so it can be printed out later. The earlier varibale of the hash is now checked against the hash here to see if it is the same. If not, the file name is appended to the file along with everything else. 
If there is not a file named "hashinfo.csv", then it goes through the same process where it runs through all the files and directories, printing out the hash and the time. 
