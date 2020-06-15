# Project Name: file automation
# Description: This program is for transferring files from one local server to a remote server.
# Author: Muhammad Sesay
# Written Date: 27TH April, 2020

import os
import fnmatch
from paramiko import SSHClient

# ssh = SSHClient()
# ssh.load_system_host_keys()

# Todo : Change the username and server ip
# ssh.connect('user@server:path')
# with SCPClient(ssh.get_transport()) as scp:
#     scp.put('my_file.txt', 'my_file.txt') # Copy my_file.txt to the server


def copy_data():
    '''
    This function copy file(s) from one server to a directory in a remote server
    '''

    # local variables
    file_lists = []
    src_dir = './current_server_dir'
    dest_dir = './remote_server_dir'

    # open the directory
    listOfFiles = os.listdir(src_dir)
    pattern = "*.idx" # binary file extension pattern
    
    # loop through the list of entries in the directory
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):

            # TODO: remove this print statement
            print ("binary files: ", entry)
            continue
        else:
            print(entry)
            file_lists.append(entry)

    # TODO: remove this print statement
    print('the list is:', file_lists)
    
    # loop through the file_lists list
    for src_file in file_lists:

        # TODO: remove from line 58 - 65  
        # join a file with the destination directory
        dest_file_location = os.path.join(dest_dir, src_file)

        # TODO: remove this print statement
        print(dest_file_location)

        # open the destionation directory for writing
        copy_file = open(dest_file_location, "w")

        # TODO: Uncomment line 68 -72
        # ssh.connect(server, username=username, password=password)
        # sftp = ssh.open_sftp()
        # sftp.put(localpath, remotepath)
        # sftp.close()
        # ssh.close()

        # TODO: run a check to remove duplicate files that have been already sent to the remote server dir

    # clear the list when the copy is done
    if copy_file:
        file_lists.clear()

    print('the list is empty:', file_lists)
        

if __name__=="__main__":
    copy_data()