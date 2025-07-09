#syntax
'''
fileobj=open(filename[,access_model])

access modes:-

r- default mode for opening a file which open the file for reading only

rb - open the file for reading in binary mode

r+ - opens both for reading and writing

w - opens writing format creates a new file if it does not exist or truncates the file to zero length if it exists

wb - opens writing in binary format creates a new file if it does not exist or truncates the file to zero length if it exists

w+ - opens both for reading and writing creates a new file if it does not exist or truncates the file to zero length if it exists

wb+ - opens both for reading and writing in binary format creates a new file if it does not exist or truncates the file to zero length if it exists

a - opens the file for appending at the end of the file without truncating it. If the file does not exist, it creates a new file

file obj attributes:-

fileobj.closed - ret- return true if the file is closed and false 

fileobj.mode - opening access 

fileobj.name - name of the file

'''



