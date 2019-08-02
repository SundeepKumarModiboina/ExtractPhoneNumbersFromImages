# Extract Phone Numbers From Images

The main aim of this script is to extract the Mobile Numbers from the image files.
There are two inputs given to the script.

1. Input Folder where the image files are present
2. Output file path

## Procedure
All the image files from whcih the mobile numbers need to be extracted are placed in a folder
and the folder path is one of the input that needs to be given.

The script goes through the given input folder path and checks for the image files and prepares the list of image files
present in the folder. 
It then iterates through these files and converts the image file content to string format.
We then process the string data and search for all the mobile numbers present in it.
The phone numbers are then written to the text file.
