import ipdb
import os
import shutil


def init():
	data_root = 'C:\\Users\\Gesina Phillips\\Desktop\\supp'
	data_root = os.path.normpath(data_root)
	output_dir = data_root + os.sep + 'renamed_files'
	min_file_size = 1000
	counts = contentdm_data_extractor(data_root, output_dir, min_file_size)
	if counts:
		print('copied {0} files, {1} files too small'.format(counts[0], counts[1]))

# TODO: let user input override directory; default to directory script lives in
def contentdm_data_extractor(data_root, output_dir, min_file_size):
	skipped_count = 0
	renamed_count = 0
	if os.path.exists(output_dir):
		print('The directory {0} already exists!'.format(output_dir))
		return
	else:
		os.mkdir(output_dir)
	for root, dir, files in os.walk(data_root):
		norm_root = os.path.normpath(root)
		for filename in files:
			outcome = extract_file(norm_root, filename, min_file_size, output_dir)
			if outcome == 'success':
				renamed_count += 1
			elif outcome == 'toosmall':
				skipped_count += 1
	return renamed_count, skipped_count
				
def extract_file(norm_root, filename, min_file_size, output_dir):
	current_path = os.path.join(norm_root, filename)
	if not filename == 'index.pdf':
		return 'wrongname'
	elif os.path.getsize(current_path) < min_file_size:
		return 'toosmall'
	split = current_path.split('supp')
	renamed_file = split[1].replace('\\', '_')  # it's an escaped backslash dummy
	renamed_file = renamed_file[1:]
	new_path = os.path.join(output_dir, renamed_file)
	shutil.copy2(current_path, new_path)
	return 'success'

init()