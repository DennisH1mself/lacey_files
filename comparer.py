import os
set1_path = 'test_files/testset1'
set2_path = 'test_files/testset2'
set1_files = os.listdir(set1_path)
set2_files = os.listdir(set2_path)
set1_file_content = [{'path': file,'content': open(file, 'r').read()} for file in set1_files]
set2_file_content = [{'path': file,'content': open(file, 'r').read()} for file in set2_files]
for file1 in set1_file_content:
    for file2 in set2_file_content:
        if file1['content'] == file2['content']:
            print(file1['path'], file2['path'])