#Copyright (c) 2023 Cirrus Aircraft
"""
This software is provided under the MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

#run this script from avibrief-dataset/

import os

def filepath_replace(json_file):
  # Read in the file
  cur_wdir = os.getcwd()
  filedata = ""
  with open(json_file, 'r') as file:
    filedata = file.read()
  #Replace the target string
  print("replacing '*' with:", cur_wdir)
  filedata = filedata.replace("*", cur_wdir)
  # Write the file out again
  with open(('dev_' + json_file), 'w') as file:
    file.write(filedata)

print("Configuring ss_test_manifest.json")
filepath_replace("/manifest_files/ss_test_manifest.json")
print("Configuring ss_train_manifest.json")
filepath_replace("/manifest_files/ss_train_manifest.json")
print("Configuring ss_val_manifest.json")
filepath_replace("/manifest_files/ss_val_manifest.json")
print("Configuring ws_test_manifest.json")
filepath_replace("/manifest_files/ws_test_manifest.json")
print("Configuring ws_train_manifest.json")
filepath_replace("/manifest_files/ws_train_manifest.json")
print("Configuring ws_val_manifest.json")
filepath_replace("/manifest_files/ws_val_manifest.json")