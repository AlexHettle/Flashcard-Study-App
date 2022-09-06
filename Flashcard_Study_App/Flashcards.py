from tkinter import *
import random
import csv


#A flashcard class that has values for the front of the card, the back
#of the card, and a variable that lets the program know whether the question
#side (front) or the answer side (back) is visible to the user.
class flashcard:
    def __init__(self, question, answer):
        self.question=question
        self.answer=answer
        self.side_up="Q"
#A function that flips the card for the user.
def flip(flashcard_list,the_canvas,index_of_card):
    the_canvas.delete("all")
    current_on_screen=flashcard_list[index_of_card]
    the_canvas.create_rectangle(0,0,500,500,fill="white",outline="")
    if(current_on_screen.side_up=="Q"):
        the_canvas.create_text(270,170,width=530,font="Times 20 italic bold",text=current_on_screen.answer)
        current_on_screen.side_up="A"
    else:
        the_canvas.create_text(270,170,width=530,font="Times 20 italic bold",text=current_on_screen.question)
        current_on_screen.side_up="Q"
    global card_index
    card_index=index_of_card
#A function that moves to the next card in the list and loops back to the
#beginning of the list if necessary
def next_card(flashcard_list,the_canvas,index_of_card):
    the_canvas.delete("all")
    the_canvas.create_rectangle(0,0,500,500,fill="white",outline = "")
    global card_index
    if(index_of_card+1>=len(flashcard_list)):
        next_card_on_screen=flashcard_list[0]
        card_index=0
    else:
        next_card_on_screen=flashcard_list[index_of_card+1]
        card_index=index_of_card+1
    the_canvas.create_text(270,170,width=530,font="Times 20 italic bold",text=next_card_on_screen.question)
    next_card_on_screen.side_up="Q"
#A function that moves to the previous card in the list and loops back to the
#end of the list if necessary
def prev_card(flashcard_list,the_canvas,index_of_card):
    the_canvas.delete("all")
    the_canvas.create_rectangle(0,0,500,500,fill="white",outline="")
    global card_index
    if(index_of_card-1<=-1):
        next_card_on_screen=flashcard_list[len(flashcard_list)-1]
        card_index=len(flashcard_list)-1
    else:
        next_card_on_screen=flashcard_list[index_of_card-1]
        card_index=index_of_card-1
    the_canvas.create_text(270,170,width=530,font="Times 20 italic bold",text=next_card_on_screen.question)
    next_card_on_screen.side_up="Q"
#takes in a list of flashcards, shuffles them, and prepares the GUI to
#display them
def finalize(flashcard_list):
    random.shuffle(flashcard_list)
    the_canvas = Canvas(window,width=550,height=370, highlightthickness=0)
    the_canvas.create_text(270,170,width=530,font="Times 20 italic bold",text=flashcard_list[0].question)
    global card_index
    card_index=0
    the_canvas.configure(bg="white")
    the_canvas.place(x=225,y=60)
    flip_button=Button(text="Flip Card",font=("fixedsys",30),command=lambda:flip(flashcard_list,the_canvas,card_index),bg="#2a19e3",fg="white")
    flip_button.pack(side=BOTTOM,pady=40)
    next_button=Button(text="Next",font=("fixedsys",30),command=lambda:next_card(flashcard_list,the_canvas,card_index),bg="#2a19e3",fg="white")
    next_button.place(x=640,y=491)
    prev_button=Button(text="Prev",font=("fixedsys",30),command=lambda:prev_card(flashcard_list,the_canvas,card_index),bg="#2a19e3",fg="white")
    prev_button.place(x=250,y=491)
#A function that attemts to read in a csv file of flashcards,
#creates a list of flashcard objects out of them, and passes them into the
#finalize function. Gives an error message if input is invalid.
def get_flashcards(entry,label,button):
    try:
        the_file=open(entry.get(),"r")
        entry.delete(0,END)
        the_file.seek(0)
        the_reader=csv.reader(the_file)
        header1=next(the_reader,None)
        flashcard_list=list()
        for line in the_reader:
            flashcard_list.append(flashcard(line[0],line[1]))
        label.destroy()
        entry.destroy()
        button.destroy()
        finalize(flashcard_list)
    except:
        label.configure(text="File does not exist.Try again")
        entry.delete(0,END)



#Sets up the GUI to take in a csv file to make the flashcards out of
def start_game():
    start_button.destroy()
    start_label.destroy()
    flashcard_entry=Entry(window,width=80,borderwidth=15)
    flashcard_entry.place(x=245,y=360)
    entry_label=Label(text="Please enter the path of the csv file that contains the flashcard pack you wish to use",font=("fixedsys",30),wraplength=590,bg="#6e17bf",fg="White",justify="center")
    entry_label.pack(pady=60)

    entry_button=Button(text="use flashcard set",font=("fixedsys",30),command=lambda:get_flashcards(flashcard_entry,entry_label,entry_button),bg="#2a19e3",fg="white",padx=73)
    entry_button.place(x=245,y=450)



#This section of code also sets up the GUI
window=Tk()
window.configure(bg="#6e17bf")
window.resizable(False, False)
window.geometry("1001x601")
window.title("Flashcard-App")
the_canvas = Canvas(window,width=1000,height=600, highlightthickness=0)
the_canvas.place(x=0,y=0)
the_canvas.create_rectangle(0,0,1000,600,fill="#1A17BF",outline="")
the_canvas.create_rectangle(10,10,990,590,fill="#BF17BC",outline="")
the_canvas.create_rectangle(20,20,980,580,fill="#1A17BF",outline="")
the_canvas.create_rectangle(30,30,970,570,fill="#6e17bf",outline="")
the_canvas.create_rectangle(40,40,80,560,fill="#BF17BC",outline="")
the_canvas.create_rectangle(100,40,140,560,fill="#BF17BC",outline="")
the_canvas.create_rectangle(160,40,200,560,fill="#BF17BC",outline="")
the_canvas.create_rectangle(920,40,960,560,fill="#BF17BC",outline="")
the_canvas.create_rectangle(860,40,900,560,fill="#BF17BC",outline="")
the_canvas.create_rectangle(800,40,840,560,fill="#BF17BC",outline="")
start_label=Label(text="FLASHCARDS",font=("fixedsys",155),bg="#6e17bf",fg="white",pady=90)
start_label.place(x=245,y=100)
start_button=Button(text="START STUDYING",font=("fixedsys",30),command=start_game,bg="#2a19e3",fg="white",anchor=CENTER,padx=99)
start_button.place(x=246,y=450)
window.mainloop()
