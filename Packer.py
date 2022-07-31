#################################################################################################
#
# Application : File Packer.
# Description : It is used to Pack files into single file.
# Functions   : 1.Entry Function, 2.FilePacker, 3.Pack, 4.Checksum and 5.CreateFile.
# Input       : Directory ,file name .
# Output      : Packed data of many files into one file.
# Author      : Pranay Vasant Huskal.
#
#################################################################################################

# Required Python Packages
import os
import pathlib
import hashlib
# ------------------------------------------------------------------------------------------------------------

# Function to Travel directory
def FilePacker(Directory,Name):
    """
    Function is used to travel directory to get the file names.
    Parameter: Directory to travel,String for output file name.
   
    """
    Extension =['.txt','.c','.cpp','.java','.py']
    
    path = os.getcwd()
    Filepath = os.path.join(path,Name)
    fd = CreateFile(Filepath)                             # Function call to create output file.
    fd1 = open('Log.txt', 'a')                            # create a log file on current directory.
    Count=0   
    for Folder,Subfolder,FileName in os.walk(Directory):
        
        for file in FileName:
            ext = pathlib.Path(file).suffix
        
        if (ext in Extension):                            # filter for  specific extension file.
            Count = Count + 1
            name = os.path.join(Directory, file)          # File name with path
            size = os.path.getsize(name)                  # size of file
            
            fd1 .write(f"File Name: {file}\n Size of file: {size}\n")            # lof file details.
            
            Pack(name,size,Filepath)                    # Call to pack function for packing file into one file.
            
    print(Count,"Files are packed")
    fd.close()
    fd1.close()
# ------------------------------------------------------------------------------------------------------------


# Function to pack files in one File.
def Pack(File,Size,Outfile):
    """
    Function is used to pack file into output file with its name and data.
    parameter : 1. File which get packed, 2.Size of that file. 3.Combined file in which file get packed.
    """
    fdout = open(Outfile,'a')                           # open output file in append mode.
    fdin = open(File,'r')                               # input file open in read mode.
    FileName = os.path.basename(File)
    print(FileName)
    
    Header = (FileName + " " + str(Size))               # Header string created.       
    Data = fdin.read()                                  # data of input file.
    n = len(Header)
    
    for i in range(n+1,101):
        Header = Header + " "                           # update Header.
        
    
    fdout.write(Header)                               # Write Header in output file.
    fdout.write(Data)                                 # write Data of output file. 
    fdout.close()
    fdin.close()
    
# ------------------------------------------------------------------------------------------------------------    
    
#Function to create a File:
def CreateFile(path):
    """
    Function is used to create output file.
    Parameter : Path to create output file.
    Return : output file
    """
    
    return open(path,'a')
    
# ------------------------------------------------------------------------------------------------------------    
    
def main():
    """
    Entry Function.
    Input: Takes Directory name and string for outputfile namefrom user.
    """
    
    Directory = input('Entre the folder name: ')

    Name = input("Provide output file name for packing: ")
    
    FilePacker(Directory ,Name)
    
# ------------------------------------------------------------------------------------------------------------


# Main starter.
if __name__ == "__main__":
    print("Functions details")
    print("Function FilePacker:",FilePacker.__doc__)
    print("Function CreateFile:",CreateFile.__doc__)
    print("Function Pack:",Pack.__doc__)
    
    main()
    
# ------------------------------------------------------------------------------------------------------------