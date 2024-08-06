import os
set1_path = 'test_files/testset1/'
set2_path = 'test_files/testset2/'
set1_files = os.listdir(set1_path)
set2_files = os.listdir(set2_path)
set1_file_content = [{'path': filep,'content': open(filep, 'rb').read()} for filep in [set1_path + file for file in set1_files]]
set2_file_content = [{'path': filep,'content': open(filep, 'rb').read()} for filep in [set2_path + file for file in set2_files]]
class conX:
    resetStr = "\033[1;0m"

    colorsBold = {'y': "\033[1;33m", 'g': "\033[1;32m", 'b': "\033[1;34m", 'r': "\033[1;31m", 'p': "\033[1;35m"}
    colorsNormal = {'y': "\033[0;33m", 'g': "\033[0;32m", 'b': "\033[0;34m", 'r': "\033[0;31m", 'p': "\033[0;35m"}
    def pb(self, txt):
        print("\033[1;34m" + str(txt))
    def pg(self, txt):
        print("\033[1;32m" + str(txt))
    def pr(self, txt):
        print("\033[1;31m" + str(txt))
    def pp(self, txt):
        print("\033[1;35m" + str(txt))
    def py(self, txt):
        print("\033[1;33m" + str(txt))
    def clear(self):
        for i in range(1,50):
            print('\n')  
    def waitForSay(self, txt, promptText, color='y'):
        while True:
            x = input(self.colors['y'] + str(promptText) + self.resetStr)
            if x == txt:
                break
            else:
                continue
    def waitForEnterInvis(self):
        self.waitForSay('', '')
    def waitForEnter(self, txt):
        self.waitForSay('', txt)
con = conX()
def foundDirectMatch(file1path, file2path):
    response = con.colorsNormal['r'] + 'Direct Match (same name, same content): ' + con.colorsBold['r'] + file1path + con.colorsNormal['r'] + ' == ' + con.colorsBold['r'] + file2path + con.resetStr
    print(response)
def foundInDirectMatch(file1path, file2path):
    response = con.colorsNormal['r'] + 'Partial Direct Match (same content, similar name): ' + con.colorsBold['r'] + file1path + con.colorsNormal['r'] + ' == ' + con.colorsBold['r'] + file2path + con.resetStr
    print(response)
def foundContentMatch(file1path, file2path):
    response = con.colorsNormal['y'] + 'Content Match (same source code, different name): ' + con.colorsBold['y'] + file1path + con.colorsNormal['y'] + ' == ' + con.colorsBold['y'] + file2path + con.resetStr
    print(response)
def foundNameMatch(file1path, file2path):
    response = con.colorsNormal['y'] + 'Name Match (same name, different source code): ' + con.colorsBold['y'] + file1path + con.colorsNormal['y'] + ' == ' + con.colorsBold['y'] + file2path + con.resetStr
    print(response)
for file1 in set1_file_content:
    for file2 in set2_file_content:
        if file1['content'] == file2['content'] and file1['path'].split('/')[-1] == file2['path'].split('/')[-1]:
            foundDirectMatch(file1['path'], file2['path'])
        else:
            if file1['content'] == file2['content'] and (file1['path'].split('/')[-1] in file2['path'].split('/')[-1] or file2['path'].split('/')[-1] in file1['path'].split('/')[-1]):
                foundContentMatch(file1['path'], file2['path'])
            else:
                if file1['content'] == file2['content']:
                    foundInDirectMatch(file1['path'], file2['path'])
                else:
                    if file1['path'].split('/')[-1] == file2['path'].split('/')[-1]:
                        foundNameMatch(file1['path'], file2['path'])