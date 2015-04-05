from eigen import eigenjoints,file_len
import sys
import os
from operator import itemgetter
import numpy

test_file = "test_action_file" # put the test action file name here

test_eigenjoint = test_file[:-4]

if not os.path.isfile(test_eigenjoint):
    test_eigenjoints_array = eigenjoints(test_file)
    test_eigenjoints_array.dump(test_eigenjoint)
else:
    test_eigenjoints_array = numpy.load(test_eigenjoint)
print len(test_eigenjoints_array)

file_path = ''
total_actions = 20
action_no = 1
NBNN_array = [0]*total_actions

while action_no <= total_actions:
	if action_no<10:
		file_path = "C:\\Ubuntu_Files\\MSRAction3DSkeleton(20joints)\\a0" + str(action_no) + "/eigenjoint"
	else:
		file_path = "C:\\Ubuntu_Files\\MSRAction3DSkeleton(20joints)\\a" + str(action_no) + "/eigenjoint"
	#print file_path
	action_array = numpy.load(file_path)
	#NBNN(action_array)	
	print "##############NBNN############"
        #global NBNN_array
        #global action_no
        #global test_eigenjoints_array
        print "Action no:", action_no
	#act_file_index = -1
	#train_frame_no_index = -1
	for test_frame_no in range(len(test_eigenjoints_array)):
		test_eigenjoints = test_eigenjoints_array[test_frame_no]
		#print test_eigenjoints
		min = sys.maxint
		for act_file in range(len(action_array)):
			for train_frame_no in range(len(action_array[act_file])):
			        #print "Test file frame no. : ", test_frame_no
			        #print "Train frame no.: ", train_frame_no
                                #print "Action File: ", act_file			        
				train_eigenjoint = action_array[act_file][train_frame_no]
				#print train_eigenjoint
				dist = numpy.linalg.norm(test_eigenjoints - train_eigenjoint)
				#print "Dist is: ", dist
				if dist < min:
					min = dist
		NBNN_array[action_no - 1] += min
		#print NBNN_array[action_no - 1]
        print NBNN_array, "\n\n"
	action_no += 1


#######
print "NBNN_array is : ", NBNN_array
#matched_action_index = min(enumerate(NBNN_array), key=itemgetter(1))[0]
min = sys.maxint
matched_action_index = -1
for i in range(len(NBNN_array)):
    if NBNN_array[i]<=min:
        min = NBNN_array[i]
        matched_action_index = i
print "Matched Action class:", matched_action_index+1    #Test file action class

