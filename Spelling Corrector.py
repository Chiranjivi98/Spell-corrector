from tkinter import *
from textblob import TextBlob

#Functions to clear both the text entry
def clearAll():
    word1_field.delete(0,END)
    word2_field.delete(0,END)
    
#Function to get a corrected word
def correction():
    input_word=word1_field.get()
    blob_obj=TextBlob(input_word)
    corrected_word=str(blob_obj.correct())
    word2_field.insert(10,corrected_word)

if __name__ == "__main__":
    
    #Create a gui window
    root=Tk()

    #Set the background colour of GUI window 
    root.configure(background='black')
    #Set the configuration of GUI WINDOW(WidthxHeight)
    root.geometry("400x150")
    #set the name of tkinter GUI window
    root.title("Spell Corrector")

    #Create a label
    headlabel=Label(root,text='Welcome to Spell Corrector Application',
                    fg='black',bg="red")

    label1=Label(root,text="Input Word",
                 fg='black',bg='dark green')

    label2=Label(root,text="Corrected Word",
                 fg='black',bg='dark green')
    
    #grid method is used for placing
    #the widgets at respective positions
    #in table like structure
    headlabel.grid(row = 0,column = 1)
    label1.grid(row = 1,column = 0)
    label2.grid(row = 3,column = 0,padx = 10)

    #Create a text entry box
    word1_field=Entry()
    word2_field=Entry()

    #padx keyword argument to set along x-axis
    #pady keyword argument to set along y-axis
    word1_field.grid(row=1,column=1,padx=10,pady=10)
    word2_field.grid(row=3,column=1,padx=10,pady=10)

    button1=Button(root,text="Correction",bg="red",fg="black",
                   command=correction)
    
    button1.grid(row = 2,column = 1)

    button2=Button(root,text="Clear",bg="red",fg="black",
                   command=clearAll)
    
    button2.grid(row = 4,column = 1)

    #Start the GUI
    root.mainloop()

    
