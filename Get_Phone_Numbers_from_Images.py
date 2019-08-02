# ======================================================================================================================
# Objective : Extract the Phone Numbers from the image files (.jpg, .png )
# The main aim of this script is to scan the image files and convert the data to string format.
# From the converted string data, we extract the Phone Numbers and write the output to a text file.
# ======================================================================================================================


# Import the required set of libraries
import pytesseract as tes
from PIL import Image
import re
import os



# Include tesseract executable in your path
tes.pytesseract.tesseract_cmd = r"C:\Users\sundeepkm\AppData\Local\Tesseract-OCR\tesseract.exe"


# Pattern to get the phone numbers
pat = re.compile(r"[(\+)?, 4?]91\s*\d+\s*\d+")


def get_phone_numbers(input_folder, out_file_path):

	# Folder where the files are present
	folder_loc = input_folder

	# Defining an empty list to store the image files present in the input folder
	files = []

	# Get all the image files present in the input folder
	for file in os.listdir(folder_loc):
		# Look out for the files ending with extension .png / .PNG / .jpg / .JPG
		if (file.endswith(".png") or file.endswith(".PNG") or file.endswith(".jpg") or file.endswith(".JPG")):
			file_path = os.path.join(folder_loc, file)
			files.append(file_path)

	# Raise exception when there are no image files in the given input folder path
	if not (len(files)):
		raise Exception ("There are no image files in the given input folder path : {}".format(input_folder))



	# Open the file for writing
	fb = open(out_file_path,"w")

	# Take a empty list to store the numbers
	numbers = []


	# Loop through the image files present in the input folder
	for image_path in files:

		# Get the file name without the complete path
		filename = os.path.basename(image_path)
		print("Processing the file : {}".format(filename))

		# Create the image object
		image = Image.open(image_path)

		# pass image into pytesseract module and get the text out of the image
		# pytesseract is trained in many languages
		image_to_text = tes.image_to_string(image, lang='eng')

		# Findall the numbers present in the converted image.
		res = re.findall(pat, image_to_text)

		# If number starting with 491 , it is actually +91
		# So change the starting 4 with "+"
		for number in res:
			if number.startswith("491"):
				number = "+" + number[1:]

			numbers.append(number)
			# Write the number one after the other in the new file
			fb.write(number)
			fb.write("\n")

	# Close the file handler.
	fb.close()
	return True


if __name__ == "__main__":

	input_folder = r"Input Folder path where the images files are present"
	out_file_path = r"Path to the output file including the file name with extension .txt"

	res  = get_phone_numbers(input_folder,out_file_path)
	if(res):
		print("Completed processing the files")
