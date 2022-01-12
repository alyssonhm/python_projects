import os, shutil, re

###########################################################################################################################
# PROPOSTA DO FREELANCE
########################################################################################################################### 
# A python program that will copy and paste txt files that contain certain string. 
# The search string needs to allow OR as Boolean logic. I want to use " " for search strings that contain more than two words.
# Example:

# C:\Apple\file1.txt contains "hello everyone I am Jake"
# C:\Banana\file2.txt contains "hi everyone I am Jake"
# C:\Apple\file3.txt contains "hello everyone, I am Lisa"
# C:\Apple\file3.txt contains "good afternoon everyone, I am Lisa"

# Then I run
# python program.py "C:\" ""hello everyone" OR "hi everyone"" "C:\saved (hello everyone)"

# Then, the program should copy and paste file1.txt, file2.txt, file3.txt, but not file4.txt, to the folder "C:\saved (hello everyone)"
###########################################################################################################################

###########################################################################################################################
#
# Developer.: Alysson
# Date......: dec-04-2021
# Purpose...: Search for strings inside files with certain extensions and copy this files to another directory
# Obs.......: This script has been tested to work only .txt files, if you need other extensions, it can be adapted 
# Parameters:
#   sourceDir = Source Directory (Ex: '/home/user/soucerDir')
#   fileExt = File extension you want to analyze (Ex: '.txt')
#   searchString = String for search. Enclose the entire string in single quotes (Ex: '"string" OR "String" OR "STRING"')
#   destDir = Destination directory (Ex: '/home/user/destDir')
#
###########################################################################################################################


def searcher(sourceDir, fileExt, searchString, destDir):

    searchString = re.split('OR', searchString) # split string for search 
    
    for string in searchString:
        string = re.sub("\"","",string).strip() #replace special characters from string
        print(f'\nSearch ... {string}\n')    
    
        for files in os.listdir(sourceDir): # list all files in sourceDir
            
            if files.endswith(fileExt): # read only fileExt files
                
                if string in open(os.path.join(sourceDir, files)).read():
                    file = os.path.join(sourceDir, files) # identifing files to copy
                    
                    if not os.path.exists(destDir): 
                        os.makedirs(destDir) # create directory if not exists
                    
                    print(f'Copying file {file} to {destDir}')                
                    shutil.copy2(file,destDir) # copy file to destination directory



searcher('/home/python/bylearn/freelas', '.txt', '"JONAS silva sauro" OR "Retorna o caminho para o arquivo" OR "marcos"', '/home/python/bylearn/freelas/NOVAPASTA')