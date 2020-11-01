## MORSE CODE TRANSLATOR ##
# CREATED BY PUNIT, SUMIT, DEEPAK
# SUBMITED TO GAGANDEEP KAUR
# PROJECT = INT213 (Python Programming)

from tkinter import *
from tkinter import messagebox
import tkinter.font as tkfont
root = Tk() 

bgphoto = PhotoImage(file = r"C:\\Users\\hacke\Desktop\\pythonproject\\Gradientblue.png")
infophoto = PhotoImage(file = r"C:\\Users\\hacke\Desktop\\pythonproject\\info.png")
exitphoto = PhotoImage(file = r"C:\\Users\\hacke\Desktop\\pythonproject\\EXIT.png")


# Dictionary representing the morse code chart 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
					'C':'-.-.', 'D':'-..', 'E':'.', 
					'F':'..-.', 'G':'--.', 'H':'....', 
					'I':'..', 'J':'.---', 'K':'-.-', 
					'L':'.-..', 'M':'--', 'N':'-.', 
					'O':'---', 'P':'.--.', 'Q':'--.-', 
					'R':'.-.', 'S':'...', 'T':'-', 
					'U':'..-', 'V':'...-', 'W':'.--', 
					'X':'-..-', 'Y':'-.--', 'Z':'--..', 
					'1':'.----', '2':'..---', '3':'...--', 
					'4':'....-', '5':'.....', '6':'-....', 
					'7':'--...', '8':'---..', '9':'----.', 
					'0':'-----', ', ':'--..--', '.':'.-.-.-', 
					'?':'..--..', '/':'-..-.', '-':'-....-', 
					'(':'-.--.', ')':'-.--.-'} 

 
def clearAll() : 
	 
	language1_field.delete(1.0, END) 
	language2_field.delete(1.0, END) 

def convert() : 
	message = language1_field.get("1.0", "end")[:-1] 

	language2_field.insert('end -1 chars', encrypt(message.upper()))
	
def convert2() : 
	message = language1_field.get("1.0", "end")[:-1] 

	language2_field.insert('end -1 chars', decrypt(message))

def encrypt(message): 
	cipher = '' 
	for letter in message: 
		if letter != ' ': 
	
			# morse codes for different characters 
			cipher += MORSE_CODE_DICT[letter] + ' '
		else: 

			cipher += ' '
	
	return cipher 
	
# Function to decrypt the string 
# from morse to english 
def decrypt(message): 
	
	
	# last morse code 
	message += ' '
	
	decipher = '' 
	citext = '' 
	for letter in message: 
	
		# checks for space 
		if (letter != ' '): 
	
			# counter to keep track of space 
			i = 0
	
			# storing morse code of a single character 
			citext += letter 
	
		# in case of space 
		else: 
			
			i += 1
	
			
			if i == 2 : 
	
				# adding space to separate words 
				decipher += ' '
			else: 
	
				
				decipher += list(MORSE_CODE_DICT.keys())[ 
							list(MORSE_CODE_DICT .values()).index(citext)] 
				citext = '' 
	
	return decipher.lower()


def openEnc():
	encWindow = Toplevel()
	Label(encWindow, image=bgphoto).place(relwidth = 1,relheight = 1)
	encWindow.geometry("775x460") 

	toplabel1 = Label(encWindow, text = '          MORSE ENCRYPTOR    ',fg = 'yellow', bg="black",font = ("orbitron",30,"bold")) 
	toplabel1.grid(row = 0, column = 0,) 		

	global language1_field,language2_field
	language1_field = Text(encWindow, height = 5, width = 25, font = "orbitron") 
	language2_field = Text(encWindow, height = 5, width = 25, font = "orbitron")
									
	language1_field.grid(row = 1, column = 0, pady=30) 
	language2_field.grid(row = 2, column = 0, ) 

	clrbutton = Button(encWindow, text = "CLEAR", width = 10, height = 2, bg = "grey", 
					fg = "black", command = clearAll, font=("orbitron",10,"bold"),relief="raised",bd=5) 
	
	clrbutton.grid(row = 1, column = 1)

	conbutton = Button(encWindow, text = "CONVERT", width = 10, height = 2, bg = "grey", fg = "black",
					command = convert, font=("orbitron",10,"bold"),relief="raised",bd=5) 
		
	conbutton.grid(row = 2, column = 1)

def openDrcy():
	drcyWindow = Toplevel()
	Label(drcyWindow, image=bgphoto).place(relwidth = 1,relheight = 1)
	drcyWindow.geometry("775x460") 

	toplabel1 = Label(drcyWindow, text = '          MORSE DECRYPTOR    ',fg = 'yellow', bg="black",font = ("orbitron",30,"bold")) 
	toplabel1.grid(row = 0, column = 0,) 		

	global language1_field,language2_field
	language1_field = Text(drcyWindow, height = 5, width = 25, font = "orbitron") 
	language2_field = Text(drcyWindow, height = 5, width = 25, font = "orbitron")
									
	language1_field.grid(row = 1, column = 0, pady=30) 
	language2_field.grid(row = 2, column = 0, ) 

	clrbutton = Button(drcyWindow, text = "CLEAR", width = 10, height = 2, bg = "grey", 
					fg = "black", command = clearAll, font=("orbitron",10,"bold"),relief="raised",bd=5) 
	
	clrbutton.grid(row = 1, column = 1)

	conbutton = Button(drcyWindow, text = "CONVERT", width = 10, height = 2, bg = "grey", fg = "black",
					command = convert2, font=("orbitron",10,"bold"),relief="raised",bd=5) 
		
	conbutton.grid(row = 2, column = 1)

def info():
	infoWindow = Toplevel()
	Label(infoWindow, bg="black").place(relwidth = 1,relheight = 1)
	infoWindow.geometry("850x300") 

	toplabel1 = Label(infoWindow, text = '        ABOUT MORSE    ',fg = 'yellow', bg="black",font = ("orbitron",30,"bold")) 
	toplabel1.grid(row = 0, column = 0,) 	
	infolabel = Label(infoWindow, text ='''\n\nMorse code is a method used in telecommunication to encode text characters as standardized sequences 
of two different signal durations, called dots and dashes or dits and dahs. Morse code is named after
Samuel Morse, an inventor of the telegraph.The International Morse Code encodes the 26 English letters
A through Z, some non-English letters, the Arabic numerals and a small set of punctuation and procedural
signals (prosigns). There is no distinction between upper and lower case letters.Each Morse code symbol
is formed by a sequence of dots and dashes. The dot duration is the basic unit of time measurement in Morse code
transmission. The duration of a dash is three times the duration of a dot. Each dot or dash within a character
is followed by period of signal absence, called a space, equal to the dot duration. The letters of a word are
separated by a space of duration equal to three dots, and the words are separated by a space equal to seven dots.'''
   ,fg = 'White', bg="black",font = ("orbitron",10,"bold")) 
	infolabel.grid(row = 1, column =0 ) 	

def close(): root.destroy()

# Driver code 
if __name__ == "__main__" : 
	
	# Set the background colour of GUI window 
	Label(root, image=bgphoto).place(relwidth = 1,relheight = 1)
	
	# Set the configuration of GUI window (WidthxHeight) 
	root.geometry("715x460") 

	# set the name of tkinter GUI window 
	root.title("Translator") 
	
	# Create Welcome to Morse Code Translator label 
	headlabel = Label(root, text = '  MORSE CODE TRANSLATOR  ',fg = 'yellow', bg="black",font = ("orbitron",30,"bold")) 
	
	
	headlabel.grid(row = 0, column = 0,columnspan =3) 		

	 

	button1 = Button(root, text = "ENCRYPTOR\n\nENG  --->  MORSE", width = 20, height = 5, bg = "grey", fg = "black",
								command = openEnc, font=("orbitron",15,"bold"),relief="raised",bd=5) 
		
	button1.grid(row = 4, column = 0,padx=20) 
	
	
	button2 = Button(root, text = "DECRYPTOR\n\nMORSE  --->  ENG", width = 20, height = 5, bg = "grey", 
					fg = "black", command = openDrcy, font=("orbitron",15,"bold"),relief="raised",bd=5) 
	button2.grid(row = 4, column = 2,pady = 75) 
		
	button3 = Button(root,image = infophoto, compound = LEFT,text = " INFO", width = 67, height = 30, bg = "DarkBlue",
					fg = "white", command = info, font=("orbitron",10,"bold"),relief="sunken",bd=5) 
	button3.grid(row = 5, column = 0) 

	button4 = Button(root,image = exitphoto ,compound = LEFT,text = " EXIT", width = 77, height = 30, bg = "grey",
					fg = "white", command = close, font=("orbitron",10,"bold"),relief="sunken",bd=5) 
	button4.grid(row =5, column = 2)
	

	root.mainloop() 
