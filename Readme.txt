Readme File for 3D action recognition using eigenjoints.

CONTENTS
-----------------------------------------
1. 'action_list.txt' - It contains the list of action files used by us.

1. 'eigen.py' - Our main python code. It takes 'action_list.txt' as input and computes eigenjoints for each action file. On line no. 231
	there is a variable called 'testing'. Set it to 1 if you want to do testing so that it does not recompute the eigenjoints of test action 
	files. Set it to 0 if you want to compute the eigenjoints.
	
2. 'eigenTesting.py' - Python file for carrying out testing. It takes the test action file as input. For e.g. if the test action file
	is "a01_s01_e03_skeleton.txt" then on the 7th line of eigenTesting.py replace "test_action_file" with "a01_s01_e03_skeleton.txt".
	give the full directory name there
	
NOTE: The files 'eigen.py', 'eigenTesting.py', 'action_list.txt' and test action files such as 'a01_s01_e03_skeleton.txt' should be in the 
same directory.

SOFTWARE REQUIREMENT:
-----------------------------------------
-> Python 2.7 or above

Following python libraries have to be installed for the code to work.
1) numpy
2) scikit-learn (Python's machine learning library)

DATASET
-----------------------------------------
MSR Action3D dataset(3D skeleton coordinates) can be downloaded from the following link:
http://research.microsoft.com/en-us/um/people/zliu/ActionRecoRsrc/