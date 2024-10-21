import tkinter
from tkinter import Tk, Label, Text, Button, messagebox

font = ('Arial', 20, 'bold')
test_word = "the words are selected from list of commonly used words some typing speed tests use words with difficult spellings but think that is unfair want to measure typing speed not reading skill the lack of difficult words in this test also enables this site to be used as a typing game for kids"

test_word_list = test_word.split()

time = 60
timer_running = False
countdown_job = ''
user_list = []
edit_list = True



def countdown(time_left):
    global time, countdown_job
    if time_left > 0:
        timer.config(text=time_left)
        countdown_job = window.after(1000, countdown, time_left - 1)
    else:
        timer.config(text="Time's up!")
        my_input.config(state='disabled')
        compare_and_calculate(user_list, test_word_list)
    # timer.config(text=time_left)


def reset_timer():
    global time, timer_running, countdown_job, user_list
    if countdown_job is not None:
        window.after_cancel(countdown_job)
    my_input.delete('1.0', 'end')
    time = 60
    timer_running = False
    my_input.config(state='normal')
    timer.config(text=time)
    user_list = []


def check_text_box(event):
    global time, timer_running
    no = my_input.get('1.0', tkinter.END).strip()
    count = len(no)
    if count >= 1 and not timer_running:
        timer_running = True
        window.after(1000, countdown, time - 1)


def compare_and_calculate(user, computer):
    gotten_words = []
    correct_words = []
    mistyped_words = []
    for items in range(len(user)):
        if user[items] != computer[items]:
            correct_words.append(computer[items])
            mistyped_words.append(user[items])
        elif user[items] == computer[items]:
            gotten_words.append(user[items])
    sentence_for_cpm = ' '.join(gotten_words)
    CPM = len(sentence_for_cpm)
    WPM = (CPM / 5)
    messagebox.showinfo(title='Results',
                        message=f'CPM={CPM},\n WPM={round(WPM, 2)},\n The words you mistyped={mistyped_words}')


def edit(event):
    global user_list, edit_list
    no = len(my_input.get('1.0', tkinter.END).strip())
    if edit_list == True and no == 0:
        edit_list = False
        try:
            last_word = user_list[-1]
        except IndexError:
            pass
        else:
            index = len(user_list)-1
            print(index)
            print(user_list)
            print(last_word)
            my_input.insert('1.0', last_word)
            changed_word = my_input.get('1.0', tkinter.END).strip()
            go_on = determine_key(event)
            if go_on:
                user_list[index] = changed_word
                my_input.delete('1.0',tkinter.END)
                print(user_list)



def add_to_user_list(event):
    global user_list, test_word_list
    word = my_input.get('1.0', tkinter.END).strip()
    user_list.append(word)
    my_input.delete('1.0', 'end')

def determine_key(event):
    print(event.keysym)
    if event.keysym=='Shift_R':
        return True

window = Tk()
window.title('Speed Typing Tester')
window.minsize(width=600, height=600)

timer = Label(window, text=time, font=('Arial', 30))
timer.grid(row=0, column=0, pady=10)

my_label = Label(window, text=test_word, fg='black', font=font, wraplength=650)
my_label.grid(row=1, column=1)

header = Label(window, text='Speed typing Tester', font=('Arial', 30))
header.grid(row=0, column=1, pady=10)

my_input = Text(window, width=60, height=3, font=('Arial', 20), borderwidth=3)
my_input.grid(row=2, column=1, pady=30)
my_input.focus()

restart = Button(window, text='Restart', command=reset_timer)
restart.grid(row=3, column=2)

my_input.bind('<KeyRelease>', check_text_box)
my_input.bind('<space>', add_to_user_list)
my_input.bind('<BackSpace>', edit)

window.bind('<KeyPress>',determine_key)
window.mainloop()
