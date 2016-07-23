import ipdb
import os
import shutil


def rename_contentdm_files(data_root):
	data_root = os.path.normpath(data_root)
	output_dir = data_root + os.sep + 'renamed_files'
	if os.path.exists(output_dir):
		print('The directory {0} already exists!'.format(output_dir))
	if not os.path.exists(output_dir):
		os.mkdir(output_dir)
	for root, dir, files in os.walk(data_root):
		norm_root = os.path.normpath(root)
		for filename in files:
			path = os.path.join(norm_root, filename)
			if filename == 'index.txt':
				old_path = os.path.join(norm_root, filename)
				split = old_path.split('temp_copy')
				split_1 = split[1]
				renamed_file = split[1].replace('\\', '_')
				renamed_file = renamed_file[1:]
				new_path = os.path.join(output_dir, renamed_file)
				shutil.copy2(renamed_file, new_path)

rename_contentdm_files('C:\\Users\\Gesina Phillips\\Desktop\\temp_copy')