import ipdb
import os


#for root, dir, files in os.walk('C:\\Users\\Gesina Phillips\\Desktop\\temp_copy'):
#	for filename in files:
#		if filename == 'index.txt':
#		ipdb.set_trace()
#			print(filename)

#path = 'C:\\Users\\Gesina Phillips\\Desktop\\temp_copy\\folder1\\'
#for filename in os.listdir(path):
#	if filename == 'index.txt':
#		os.rename (os.path.join(path, filename), os.path.join(path, 'indexlol.txt'))


# for root, dir, files in os.walk('C:\\Users\\Gesina Phillips\\Desktop\\temp_copy'):
	# for filename in files:
#		print(os.path.join(root, filename))
#		ipdb.set_trace(
		# if filename == 'index.txt':
			# old = os.path.join(root, filename)
			# new = os.path.join(root, 'indexlol.txt')
			# print(old)
			# print(new)
#			os.rename (old, new)

notes:

os.path.split('C:\\Users\\Gesina Phillips\\Desktop\\temp_copy\\folder3\\subdir4\\subsubdir4\\temp_copy\\subsubsubdir1')

>>> import os
>>> os.path.split('C:\\Users\\Gesina Phillips\\Desktop\\temp_copy\\folder3\\subdir4\\subsubdir4\\temp_copy\\subsubsubdir1')
('C:\\Users\\Gesina Phillips\\Desktop\\temp_copy\\folder3\\subdir4\\subsubdir4\\temp_copy', 'subsubsubdir1')
>>> path = 'C:\\Users\\Gesina Phillips\\Desktop\\temp_copy\\folder3\\subdir4\\subsubdir4\\temp_copy\\subsubsubdir1'
>>> path
'C:\\Users\\Gesina Phillips\\Desktop\\temp_copy\\folder3\\subdir4\\subsubdir4\\temp_copy\\subsubsubdir1'
>>> path.split('temp_copy')
['C:\\Users\\Gesina Phillips\\Desktop\\', '\\folder3\\subdir4\\subsubdir4\\', '\\subsubsubdir1']
>>> split = path.split('temp_copy')
>>> split
['C:\\Users\\Gesina Phillips\\Desktop\\', '\\folder3\\subdir4\\subsubdir4\\', '\\subsubsubdir1']
>>> del split[0]
>>> split
['\\folder3\\subdir4\\subsubdir4\\', '\\subsubsubdir1']
>>> 'temp_copy'.join(split)
'\\folder3\\subdir4\\subsubdir4\\temp_copy\\subsubsubdir1'
>>> muppets = ['kermit']
>>> '-'.join(muppets)
'kermit'
>>> muppets.append('piggy')
>>> '-'.join(muppets)
'kermit-piggy'

use os.path.normpath