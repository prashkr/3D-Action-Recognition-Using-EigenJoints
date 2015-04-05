#import pdb
import numpy
#import pickle
import os
import sys
import time
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
#from multiprocessing import Pool
#from pca import prinipleComponent
import time


###################

from numpy import mean,cov,double,cumsum,dot,linalg,array,rank,random
#from pylab import plot,subplot,axis,stem,show,figure

def principleComponent(A):
  A=A.T
  #print "A's shape:", A.shape   ## 3x990
    
  #  eigenvalues and eigenvectors computation

  M = (A-mean(A.T,axis=1)).T # Mean subtraction
  
  #print "M's shape:", M.shape   ## 990x3

  [eigenvalues,p_components] = linalg.eig(cov(M)) # attention:not always sorted
  eigenvalues = eigenvalues.real
  
  #print "latent's shape: ", latent.shape ## 990x1
  #print latent
  #print "coeff's shape: ", coeff.shape  ## 990x990
  
  eigenvectors = dot(p_components.T,M) # projection of the data in the new space
  eigenvectors = eigenvectors.real
  
  #print "score's shape: ", score.shape  ## 990x3
  #print score
  
  output = []     #output = random.rand(990,3)
  b=sorted(eigenvalues)
  for y in range(0, 128):	
    for x in range(0, 990):
        if(b[989-y]==eigenvalues[x]):
            output += [eigenvectors[x]]
            break
  output = array(output)
  #print output
  #print "output's shape is: ", output.shape, "\n\n"
  return output


###################


#pool = Pool()

action_lst = []

def file_len(fname): # no. of lines in a file
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def eigenjoints(file):
	nframes = file_len(file)/20 # no. of frames in file
	print file
	try:
		data = open(file, "r").read().split()
	except:
		print("File not found. System exiting")
		time.sleep(1)
		print('.')
		time.sleep(1)
		print('.')
		time.sleep(1)
		print('.')
		sys.exit()
	
	print file, nframes
        

 #######storing 3D coordinates in a 3-dimensional python list#############
	d=[[[0 for x in xrange(3)]for x in xrange(20)] for x in xrange(nframes)] 
	i=0
	p=0
	#flag=0
	while p<nframes :  
		for b in range(0, 20):
			c=0
			while c<3:
				if (i+1)%4 != 0:
					#print p, b, c, i, data[i]
					d[p][b][c] = data[i];
					c=c+1
	 			i= i+1;
		p =p+1;
        #print "Printing d: --------------- ", d     
        
############fcc calculation##########################
	fcc=[[[0 for x in xrange(3)]for x in xrange(190)]for x in xrange(nframes)]  
	i=0
	while i<nframes :
		j=0
		for a in range(0, 20):
			for b in range(0, a):
				if a!=b :
					for c in range(0, 3):
						fcc[i][j][c] = float(d[i][a][c])-float(d[i][b][c])
					j=j+1			
		i =i +1

############fci calculation##########################
	fci=[[[0 for x in xrange(3)]for x in xrange(400)]for x in xrange(nframes)]  
	i=0
	while i<nframes :
		k=0
		for a in range(0, 20):
			for b in range(0, 20):
					for c in range(0, 3):
						fci[i][k][c] = float(d[i][a][c])-float(d[0][b][c])
					k =k+1					
		i =i+1



############fcp calculation##########################
	fcp=[[[0 for x in xrange(3)]for x in xrange(400)]for x in xrange(nframes)]  
	i=1
	while i<nframes :
		k=0
		for a in range(0, 20):
			for b in range(0, 20):
					for c in range(0, 3):
						fcp[i][k][c] = float(d[i][a][c])-float(d[i-1][b][c])
					k =k+1					
		i =i+1

###############Printing fc's################################
	i=0
	while i<nframes :
		#for a in range(0, 190):
		#		print(fcc[i][a][0] ,fcc[i][a][1],fcc[i][a][2])
		#print("################################## frame",i )		
		i =i+1

	i=0
	while i<nframes :
		#for a in range(0, 400):
				#print(fci[i][a][0] ,fci[i][a][1],fci[i][a][2])
		#print("################################## frame",i )		
		i =i+1

	i=0
	while i<nframes :
		#for a in range(0, 400):
		#		print(fcp[i][a][0] ,fcp[i][a][1],fcp[i][a][2])
		#print("################################## frame",i )
		i =i+1

############fc feature calculation##########################
	fc = [[[0 for x in xrange(3)]for x in xrange(990)]for x in xrange(nframes)]
	#pdb.set_trace()
	for frame in range(0, nframes):
		i=-1
		j=-1
		k=-1
		for column in range(0, 990):
			if column <190:
				i=i+1
			elif column>=190 and column <590:
				j=j+1
			else:
				k= k+1
			for coordinates in range(0,3):
				if column < 190:
					#print "fcc", frame, column, coordinates, "i is:", i
					fc[frame][column][coordinates] = fcc[frame][i][coordinates]
				elif column>=190 and column <590:
					#print "fcp", frame, column, coordinates, "j is:", j
					fc[frame][column][coordinates] = fcp[frame][j][coordinates]
				else:
					#print "fci", frame, column, coordinates, "k is:", k
					fc[frame][column][coordinates] = fci[frame][k][coordinates]

	'''i=0
	for i in range(0, len(fc)):
		print "------------------------------------"
		print "frame", i, "start"

		for j in range(0, len(fc[i])):
			print "column ", j, "--", fc[i][j]

		print "frame", i, "end"
		print "------------------------------------"
	'''
############Normalization and PCA calculation##########################
	fc_array = numpy.array(fc)  #converting fc into a numpy array
	fc_array1 = numpy.zeros((nframes,128,3)) #creating an array for storing eigenjoints
	t_start = time.time()
        #fc_array1 = pool.map(principleComponent, fc_array)
	print "start time = ", t_start
	for i in range(0, nframes):
		#print "enter"
		fc_array[i] = normalize(fc_array[i], axis=1, norm='l1')   # L1 Normalization of eigenjoints
		#p = multiprocessing.Process(target=princomp, args=(fc_array[i],))
		#print fc_array[i].shape
		print "frame no. : ", i
		fc_array1[i] = principleComponent(fc_array[i])
		#result = pool.apply_async(princomp, [fc_array[i]])
		#fc_array1[i] = result.get()
		#print fc_array1[i]
		#pca = PCA(n_components=128)
		#p.close()
		#p.join()
		#pca.fit(fc_array[i])
		#fc_array[i] = pca.components_
	t_end = time.time()
	print "end time = ", t_end
	print "time taken  = ", (t_end-t_start)
	return fc_array1
	#pickle.dump(fc_array, open("./p.txt", "wb"))

	#print fc_array[0].size


testing = 1
if not testing:
	file = open("action_list.txt", "r")
	file_text = file.read()
	lst = file_text.split('\n')
	lst = lst[:-1]

	alist = []
	fno = 19
	i=0
	while i!= len(lst):
		actions = []
		if int(int(lst[i][1])*10 + int(lst[i][2])) != fno:
			fno += 1
		while int(int(lst[i][1])*10 + int(lst[i][2])) == fno:
			if lst[i][len(lst[i])-1] != '3':
				fname0 = lst[i] + "_skeleton"
				fname1 = fname0 + ".txt"
				fc_array = eigenjoints(fname1)
				actions += [fc_array]
				#print "-1"
			i+=1
			if i==len(lst):
				break
			#print "0"
			action1 = numpy.array(actions)
			#print "1"
		alist += [action1]
		direc = ''
		if fno < 10:
			direc = 'a0' + str(fno)
		else:
			direc = 'a' + str(fno)

		if not os.path.isdir(direc):
			os.mkdir(direc)
			filename = direc + '/eigenjoint'
			action1.dump(filename)

		#print "2"

	#print "3"
	alist = numpy.array(alist)
	#print "4"
	#pickle.dump(alist, './')
else:
	print "Testing Mode Enabled. Please unset the testing variable"
