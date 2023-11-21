import sys
import os
import glob
from os.path import exists, basename,join
from pathlib import Path


top_folder="*\\*\\tests"
for test_dir in glob.glob(top_folder):
	target_file = join(test_dir,"__init__.py")
	print(target_file)
	if not exists(target_file):
		print(f"adding __init__.py to {test_dir}")
		Path(target_file).touch()