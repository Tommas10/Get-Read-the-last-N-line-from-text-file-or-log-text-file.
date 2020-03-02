#!/usr/bin/env python

#This small auto Python scrip file - Get / Read the last N line from text file or log text file.
#Created by Tommas Huang
#Date: 2020-02-26
#Version: 3.0

#The OS module in python provides functions for interacting with the operating system. OS, comes under Python's standard utility modules.
import os
def get_last_n_lines(file_name, N):
    # Create an empty list to keep the track of last N lines
    list_of_lines = []
    # Open file for reading in binary mode
    with open('/Users/TommasHuang/Documents/log-2.txt', 'rb') as read_obj:
        # Move the cursor to the end of the file
        read_obj.seek(0, os.SEEK_END)
        # Create a buffer to keep the last read line
        buffer = bytearray()
        # Get the current position of pointer i.e eof
        pointer_location = read_obj.tell()
        # Loop till pointer reaches the top of the file
        while pointer_location >= 0:
            # Move the file pointer to the location pointed by pointer_location
            read_obj.seek(pointer_location)
            # Shift pointer location by -1
            pointer_location = pointer_location -1
            # read that byte / character
            new_byte = read_obj.read(1)
            # If the read byte is new line character then it means one line is read
            if new_byte == b'\n':
                # Save the line in list of lines
                list_of_lines.append(buffer.decode()[::-1])
                # If the size of list reaches N, then return the reversed list
                if len(list_of_lines) == N:
                    return list(reversed(list_of_lines))
                # Reinitialize the byte array to save next line
                buffer = bytearray()
            else:
                # If last read character is not eol then add it in buffer
                buffer.extend(new_byte)
 
        # As file is read completely, if there is still data in buffer, then its first line.
        if len(buffer) > 0:
            list_of_lines.append(buffer.decode()[::-1])
 
    # return the reversed list
    return list(reversed(list_of_lines))
 
def main():
    #print("*** Get Last N lines of a text file or log text file ***")
 
    #print('** Get last 3 lines of text file or log text file **')
 
    # Get last three lines from file 'sample.txt'
    #last_lines = get_last_n_lines("/Users/TommasHuang/Documents/log-2.txt", 3)
 
    #print('Last 3 lines of File:')
    # Iterate over the list of last 3 lines and print one by one
    #for line in last_lines:
    #    print(line)
 
    print('** Get last 120 lines of text file or log text file **')
 
    # get last five lines from the file
    last_lines = get_last_n_lines("/Users/TommasHuang/Documents/log-2.txt", 120)
 
    print('Last 120 lines of File:')
    # Iterate over the list of last 170 lines and print one by one
    for line in last_lines:
        print(line)
 
    #print('*** Get last line of text file or log text or log file***')
 
    # get last line of the file
    #last_lines = get_last_n_lines("/Users/TommasHuang/Documents/log-2.txt", 1)
 
    #print('Last Line of File:')
    #print(last_lines[0])
 
    print('*** Check if last line in file matches the given line ***')
 
    # get last line of the file
    last_lines = get_last_n_lines("/Users/TommasHuang/Documents/log-2.txt", 1)
 
    # Match the returned last line of file with the give string
    if last_lines[0] == 'This is the end of file' :
        print('Last Line matched')
 
    print('**** Check if last line in file contains given sub-string ****')
 
    sub_string_to_match = 'is'
 
    # Check if the last line of file contains the given sub-string or not
    if sub_string_to_match in get_last_n_lines("/Users/TommasHuang/Documents/log-2.txt", 1)[0]:
        print('Positive: Last Line contains the given sub string')
    else:
        print('Negative: Last Line do not contains the given sub string')
 
if __name__ == '__main__':
   main()