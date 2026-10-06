import re, pathlib, sys
sys.path.insert(0, '_source')
import importlib.util
spec = importlib.util.spec_from_file_location('bs', '_source/build_site.py')
print('need direct test instead')
