# This will import all the widgets 
# and modules which are available in 
# tkinter and ttk module 
from tkinter import * 
from tkinter.ttk import *
import tkinter.font as tkfont

class NewWindow(Toplevel): 
      
    def __init__(self, master):  
        super().__init__(master = master) 
        self.title("Morse Code Encode") 
        self.geometry("350x350") 
        self.configure(bg='black')
        
        label = Label(self, text ="Morse code encoder") 
        label.pack()
        label.pack(side = TOP, pady = 15) 
        label.config(font=("Microsoft PhagsPa",25))
        label.configure(foreground="green",background="black")
        self.string=StringVar(master)
        self.result=StringVar(master) 
        label2=Label(self,text='Enter the string: ')
        label2.pack()
        label2.configure(foreground="yellow",background="black")
        text1=Entry(self,textvariable=self.string)
        text1.pack(pady = 15)
        button1=Button(self,text='Encrypt',command=self.encode)
        button1.pack(pady = 15)
        label21=Label(self,text='Result:')
        label21.pack()
        label21.configure(foreground="yellow",background="black")
        label3=Entry(self,textvariable=self.result)
        label3.pack(pady = 10)
    
    def encode(self):
        d1={' ':'|','a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..','0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'}
        a=str(self.string.get())
        b=''
        for i in a:
            if i in d1:
                b=b+d1[i]
            b=b+' '
        self.result.set(str(b))
        

class NewWindow2(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("Morse Code Decode") 
        self.geometry("350x350") 
        label = Label(self, text ="Morse code decoder") 
        label.pack()   
        label.config(font=("Microsoft PhagsPa",25))
        label.pack(side = TOP, pady = 15) 
        label.configure(foreground="green",background="black")
        self.configure(bg='black')
        self.string=StringVar(master)
        self.result=StringVar(master) 
        label2=Label(self,text='Enter the string: ')
        label2.pack()
        label2.configure(foreground="yellow",background="black")
        text1=Entry(self,textvariable=self.string)
        text1.pack()
        button2=Button(self,text='Decrypt',command=self.decode)
        button2.pack()
        label21=Label(self,text='Result:')
        label21.pack()
        label21.configure(foreground="yellow",background="black")
        label3=Entry(self,textvariable=self.result)
        label3.pack()
    

    def decode(self):
        d2={'|':' ','.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f','--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l','--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r','...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x','-.--':'y','--..':'z','-----':'0','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9'}
        a=str(self.string.get())
        a=a.split(" ")
        b=''
        for i in a:
            if i in d2:
                b=b+d2[i]
        self.result.set(str(b))

class NewWindow3(Toplevel): 
      
    def __init__(self, master):  
        super().__init__(master = master) 
        self.title("About Morse Code") 
        self.geometry("700x300") 
        self.configure(bg='black')
        label = Label(self, text ='''
        Morse code is a method used in telecommunication to encode text characters as standardized sequences 
of two different signal durations, called dots and dashes or dits and dahs. Morse code is named after
Samuel Morse, an inventor of the telegraph.The International Morse Code encodes the 26 English letters
A through Z, some non-English letters, the Arabic numerals and a small set of punctuation and procedural
signals (prosigns). There is no distinction between upper and lower case letters.Each Morse code symbol
is formed by a sequence of dots and dashes. The dot duration is the basic unit of time measurement in Morse code
transmission. The duration of a dash is three times the duration of a dot. Each dot or dash within a character
is followed by period of signal absence, called a space, equal to the dot duration. The letters of a word are
separated by a space of duration equal to three dots, and the words are separated by a space equal to seven dots
   ''') 
        label.config(font=("Microsoft PhagsPa",10))
        label.pack(side = TOP, pady = 20) 
        label.configure(foreground="yellow",background="black")




# creates a Tk() object 
master = Tk() 
  
# sets the geometry of  
# main root window 
master.geometry("700x450") 
master.title("Morse code translator")  
label = Label(master, text ="MORSE CODE TRANSLATOR") 
label.pack(side = TOP, pady = 30) 
label.config(font = ("orbitron",30,"bold"))
master.configure(bg='black')
label.configure(foreground="yellow",background="black")




# a button widget which will 
# open a new window on button click 
btn = Button(master,text ='Encode')

# Following line will bind click event 
# On any click left / right button 
# of mouse a new window will be opened 
btn.bind("<Button>",  
         lambda e: NewWindow(master)) 
  
btn.pack(pady = 15) 

btn2 = Button(master,  
             text ="Decode")
btn2.pack(pady = 15) 

btn2.bind("<Button>",  
         lambda e: NewWindow2(master)) 

btn3 = Button(master,  
             text ="About Morse")
btn3.pack(pady = 15) 

btn3.bind("<Button>",  
         lambda e: NewWindow3(master))          

# mainloop, runs infinitely 
mainloop() 
