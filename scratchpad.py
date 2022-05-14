from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Quiz")
root.geometry("900x600")
bg = PhotoImage(file = "bigquiz background 2.png")
my_canvas1= Canvas(root,width="545", height="360")
my_canvas1.pack(fill="both", expand="True")
my_canvas1.create_image(0,0,image=bg, anchor="nw")
my_canvas1.create_text(470,200,text="QUIZ GAME", font=("Chamberi Super Display",40),fill="#E5EEFF")

def create_table():
    db = sqlite3.connect("Quizzes.db")
    cur = db.cursor()
    try:
         query = """CREATE TABLE IF NOT EXISTS
                    Quiz(quest VARCHAR(50),
                          opt1 VARCHAR(25),
                          opt2 VARCHAR(25),
                          opt3 VARCHAR(25),
                          opt4 VARCHAR(25),
                          correct CHAR,
                          theme VARCHAR(25))"""
         cur.execute(query)
    
    except:
         print("Failed to Create Table!")
    db.commit()
    db.close()

def playquiz ():
   pquiz_module = Toplevel()
   pquiz_module.title("Play the quiz")
   pquiz_module.geometry("900x600")
   bg1 = PhotoImage(file="big_bg.png")
   my_canvas2 = Canvas(pquiz_module, width="900", height="600")
   my_canvas2.pack(fill="both", expand="True")
   my_canvas2.create_image(0, 0, image=bg1, anchor="nw")
   my_canvas2.create_text(450, 80, text="PLAY A QUIZ", font=("Chamberi Super Display", 40), fill="#E5EEFF")
   my_canvas2.create_text(300, 200, text="Select a theme:", font=("Cambria", 20), fill="#E5EEFF")
   themes = ttk.Combobox(pquiz_module, width=30)
   themes['values'] = ( 'Animals',
                        ' Science',
                        ' Series Trivia',
                        ' Sports',
                       )

   themes.place(x="420", y="190")
   button3 = Button(pquiz_module, text="Start", bg="#c9e265", width="17", command=question,height=3)
   button3.place(x="400", y="270")
   pquiz_module.mainloop()

def question():
   question_module = Toplevel()
   question_module.title("Question")
   question_module.geometry("900x600")
   bg3 = PhotoImage(file="big_bg.png")
   my_canvas4 = Canvas(question_module, width="900", height="600")
   my_canvas4.pack(fill="both", expand="True")
   my_canvas4.create_image(0, 0, image=bg3, anchor="nw")
   my_canvas4.create_text(80, 130, text="Question", font=("Chamberi Super Display", 15), fill="#E5EEFF")
   my_canvas4.create_text(20, 180, text="A.", font=("Chamberi Super Display", 15), fill="#E5EEFF")
   my_canvas4.create_text(20, 220, text="B.", font=("Chamberi Super Display", 15), fill="#E5EEFF")
   my_canvas4.create_text(20, 260, text="C.", font=("Chamberi Super Display", 15), fill="#E5EEFF")
   my_canvas4.create_text(20, 300, text="D.", font=("Chamberi Super Display", 15), fill="#E5EEFF")
   my_canvas4.create_text(300, 340, text="Select your answer:", font=("Chamberi Super Display", 12), fill="#E5EEFF")
   answers = ttk.Combobox(question_module, width=27)
   answers['values'] = ('A',
                       'B',
                       'C',
                       'D',
                       )

   answers.place(x="400", y="330")
   button4 = Button(question_module, text="Submit", bg="#ff5757", width="10", command=question,height=3)
   button4.place(x="400", y="400")
   button5 = Button(question_module, text="Next", bg="#c9e265", width="10", command=question,height=3)
   button5.place(x="500", y="400")
   button6 = Button(question_module, text="Previous", bg="#c9e265", width="10", command=question,height=3)
   button6.place(x="300", y="400")
   question_module.mainloop()

def createquizt():
   ctquiz_module = Toplevel()
   ctquiz_module.title("Create a quiz")
   ctquiz_module.geometry("900x600")
   bg5 = PhotoImage(file="big_bg.png")
   my_canvas5 = Canvas(ctquiz_module, width="900", height="600")
   my_canvas5.pack(fill="both", expand="True")
   my_canvas5.create_image(0, 0, image=bg5, anchor="nw")
   my_canvas5.create_text(450, 80, text="CREATE A QUIZ", font=("Chamberi Super Display", 30), fill="#E5EEFF")
   my_canvas5.create_text(300, 160, text="Theme: ", font=("Chamberi Super Display", 15), fill="#E5EEFF")
   tentry = Entry(ctquiz_module,font=("Chamberi Super Display", 10),width=40)
   tentry_window = my_canvas5.create_window(350, 150, window=tentry, anchor=NW)
   submit_button = Button(ctquiz_module, text='Submit', bg="#c9e265", width="15",command= createquiz, height=3)
   submit_button.place(x="400", y="220")
   my_canvas5.create_text(100, 550, text="Status:", font=("Chamberi Super Display", 15), fill="#E5EEFF")
   ctquiz_module.mainloop()

def createquiz():
    
    create_table()
    
    db = sqlite3.connect("Quizzes.db")
    cur = db.cursor()
    
    def submit():
        dummytheme =  'xyz'
        db = sqlite3.connect("Quizzes.db")
        cur = db.cursor()

        cur.execute("INSERT INTO Quiz VALUES (:ques, :opt1, :opt2, :opt3, :opt4, :corr, :theme)",
                {
                   'ques' : qentry.get(),
                   'opt1' : opt1tb.get(),
                   'opt2' : opt2tb.get(),
                   'opt3' : opt3tb.get(),
                   'opt4' : opt4tb.get(),
                   'corr' : answers.get(),
                   'theme' : dummytheme
                 })
        
        qentry.delete(0, END)
        opt1tb.delete(0, END)
        opt2tb.delete(0, END)
        opt3tb.delete(0, END)
        opt4tb.delete(0, END)
        
        db.commit()
        db.close()
    
    cquiz_module = Toplevel()
    cquiz_module.title("Create a quiz")
    cquiz_module.geometry("900x600")
    bg2 = PhotoImage(file="big_bg.png")
    my_canvas3 = Canvas(cquiz_module, width="900", height="600")
    my_canvas3.pack(fill="both", expand="True")
    my_canvas3.create_image(0, 0, image=bg2, anchor="nw")
    my_canvas3.create_text(450, 80, text="CREATE A QUIZ", font=("Chamberi Super Display", 40), fill="#E5EEFF")

    '''my_canvas3.create_text(40, 120, text="Theme: ", font=("Chamberi Super Display", 8), fill="#E5EEFF")'''
    #theme_lb = Label(cquiz_module, text="Theme:")'''
    '''tentry = Entry(cquiz_module,font=("Chamberi Super Display", 8),width=40)
   
    theme = tentry.get()
    query = f"SELECT * FROM Quiz WHERE theme = '{theme}'"
    cur.execute(query)
   
    result = cur.fetchall()
    if result != []:
         print("Theme already exists")
        
    tentry_window = my_canvas3.create_window(100, 110, window=tentry, anchor=NW)'''
    
    question_counter = 0
    my_canvas3.create_text(50, 150, text="Question :", font=("Chamberi Super Display", 8), fill="#E5EEFF")
    #Q_label = Label(cquiz_module, text=" Question  : ")'''
    qentry = Entry(cquiz_module,font=("Chamberi Super Display", 8), width=70)
    qentry_window = my_canvas3.create_window(100, 140, window=qentry, anchor=NW)
    my_canvas3.create_text(50, 190, text="Option 1:", font=("Chamberi Super Display", 15), fill="#E5EEFF")
    my_canvas3.create_text(50, 230, text="Option 2:", font=("Chamberi Super Display", 15), fill="#E5EEFF")
    my_canvas3.create_text(50, 270, text="Option 3:", font=("Chamberi Super Display", 15), fill="#E5EEFF")
    my_canvas3.create_text(50, 310, text="Option 4:", font=("Chamberi Super Display", 15), fill="#E5EEFF")
    #Q1_lb = Label(cquiz_module, text="Option 1:")
    #Q2_lb = Label(cquiz_module, text="Option 2:")
    #Q3_lb = Label(cquiz_module, text="Option 3:")
    #Q4_lb = Label(cquiz_module, text="Option 4:")
    opt1tb = Entry(cquiz_module,font=("Chamberi Super Display", 8),width=40)
    opt2tb = Entry(cquiz_module,font=("Chamberi Super Display", 8),width=40)
    opt3tb = Entry(cquiz_module,font=("Chamberi Super Display", 8),width=40)
    opt4tb = Entry(cquiz_module,font=("Chamberi Super Display", 8),width=40)
    opt1tb_window= my_canvas3.create_window(100, 180, window=opt1tb, anchor=NW)
    opt2tb_window= my_canvas3.create_window(100, 220, window=opt2tb, anchor=NW)
    opt3tb_window= my_canvas3.create_window(100, 260, window=opt3tb, anchor=NW)
    opt4tb_window= my_canvas3.create_window(100, 300, window=opt4tb, anchor=NW)
    
    my_canvas3.create_text(350, 350, text="Select your answer:", font=("Chamberi Super Display", 15), fill="#E5EEFF")
    #status_lb = Label(cquiz_module, text="Status:")
    #clicked = StringVar()
    answers = ttk.Combobox(cquiz_module, width=10)
    answers['values'] = (' 1',
                        ' 2',
                        ' 3',
                        ' 4',
                        )

    answers.place(x="450", y="340")
    #clicked.set("Select your Answer")
    #drop = OptionMenu(cquiz_module, clicked, "Option A", "Option B", "Option C", "Option D")
    #my_canvas3.create_window(350, 80, cquiz_module=tentry, anchor=NW)
    #my_canvas3.create_window(80, 150, cquiz_module=qentry, anchor=NW)
    #my_canvas3.create_window(150, 200, cquiz_module=Q1_lb, anchor=NW)
    #my_canvas3.create_window(150, 250, cquiz_module=Q2_lb, anchor=NW)
    #my_canvas3.create_window(150, 300, cquiz_module=Q3_lb, anchor=NW)
    #my_canvas3.create_window(150, 350, cquiz_module=Q4_lb, anchor=NW)
 
    #my_canvas3.create_window(200, 150, cquiz_module=qentry, anchor=NW, width=450)
    #my_canvas3.create_window(300, 500, cquiz_module=submit_button, anchor=NW)
    #my_canvas3.create_window(300, 450, cquiz_module=drop, anchor=NW)
    #my_canvas3.create_window(300, 550, cquiz_module=status_lb, anchor=NW, width=200)
    submit_button = Button(cquiz_module, command = submit(), text='Submit',bg="#c9e265", width="10")
    submit_button.place(x="350", y="400")
    question_counter += 1
    db.commit()
    db.close()
    if question_counter == 10:
        cquiz_module.destroy()
        
    cquiz_module.mainloop()

button1= Button(root,text="Play a quiz", command=playquiz, bg="#ff5757", height=3, width=20)
button1.place(x="400",y="250")
button2= Button(root,text="Create a quiz", command=createquizt,bg="#c9e265",height=3, width=20)
button2.place(x="400",y="320")

root.mainloop()


