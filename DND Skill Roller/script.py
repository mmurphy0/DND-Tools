import random, sys, time
import tkinter as tk
from tkinter import messagebox, Toplevel

#ToDo:
# add name entry after the continue button before rolling
#replace continue button on skills_win with export button

def saveskills():
    with open('DND Skill Roller/Skill Roll History.txt','a') as file:
        file.write('Character: ' + str(name) + '\n' + 'Strength: ' + str(strength_sum) + '\n' + 'Dexterity: ' + str(dexterity_sum) + '\n' + 'Constitution: ' + str(constitution_sum) + '\n' + 'Intelligence: ' + str(intelligence_sum) + '\n' + 'Wisdom: ' + str(wisdom_sum) + '\n' + 'Charisma: ' + str(charisma_sum) + '\n' + '----------' + '\n')
    
    messagebox.showinfo('Reminder!','Do not forget to add any stat bonuses your character has') 
    sys.exit()

def showskills():
    skills_win = Toplevel()
    skills_win.title('DnD Stat Roller')
    skills_win.geometry('220x230+0+0')

    strength_label = tk.Label(
        skills_win,
        text=(f'Strength: {strength_sum}'),
        font=('Arial',20)
    )
    strength_label.pack()

    dexterity_label = tk.Label(
        skills_win,
        text=(f'Dexterity: {dexterity_sum}'),
        font=('Arial',20)
    )
    dexterity_label.pack()

    constitution_label = tk.Label(
        skills_win,
        text=(f'Constitution: {constitution_sum}'),
        font=('Arial',20)
    )
    constitution_label.pack()

    intelligence_label = tk.Label(
        skills_win,
        text=(f'Intelligence: {intelligence_sum}'),
        font=('Arial',20)
    )
    intelligence_label.pack()

    wisdom_label = tk.Label(
        skills_win,
        text=(f'Wisdom: {wisdom_sum}'),
        font=('Arial',20)
    )
    wisdom_label.pack()

    charisma_label = tk.Label(
        skills_win,
        text=(f'Charisma: {charisma_sum}'),
        font=('Arial',20)
    )
    charisma_label.pack()

    export_button = tk.Button(
        skills_win,
        text='Export',
        font=('Arial'),
        width=10,
        command=saveskills
    )
    export_button.pack()

    back_button = tk.Button(
        skills_win,
        text='Back',
        font=('Arial'),
        width=10,
        command=skills_win.destroy
    )
    back_button.pack()

def rollskills():
    global strength_sum, dexterity_sum, constitution_sum, intelligence_sum, wisdom_sum, charisma_sum

    strength_sum = 0
    dexterity_sum = 0
    constitution_sum = 0
    intelligence_sum = 0
    wisdom_sum = 0
    charisma_sum = 0

    dice = list(range(1,7))

    strength = []
    for i in range(4):
        rolled = random.choice(dice)
        strength.append(rolled)
    strength.sort()
    strength.pop(0)
    for i in strength:
        strength_sum = i + strength_sum

    dexterity = []
    for i in range(4):
        rolled = random.choice(dice)
        dexterity.append(rolled)
    dexterity.sort()
    dexterity.pop(0)
    for i in dexterity:
        dexterity_sum = i + dexterity_sum

    constitution = []
    for i in range(4):
        rolled = random.choice(dice)
        constitution.append(rolled)
    constitution.sort()
    constitution.pop(0)
    for i in constitution:
        constitution_sum = i + constitution_sum

    intelligence = []
    for i in range(4):
        rolled = random.choice(dice)
        intelligence.append(rolled)
    intelligence.sort()
    intelligence.pop(0)
    for i in intelligence:
        intelligence_sum = i + intelligence_sum

    wisdom = []
    for i in range(4):
        rolled = random.choice(dice)
        wisdom.append(rolled)
    wisdom.sort()
    wisdom.pop(0)
    for i in wisdom:
        wisdom_sum = i + wisdom_sum

    charisma = []
    for i in range(4):
        rolled = random.choice(dice)
        charisma.append(rolled)
    charisma.sort()
    charisma.pop(0)
    for i in charisma:
        charisma_sum = i + charisma_sum

    name_entry_win.destroy()
    showskills()

def name_entry_check():
    global name
    
    name = name_entry_win_entry.get()

    if name.strip():
        rollskills()
    else:
        messagebox.showinfo('Error','A Name must be entered')

def name_entry():
    global name_entry_win_entry, name_entry_win
    
    name_entry_win = Toplevel()
    name_entry_win.geometry('285x80+0+0')
    name_entry_win.title('DND Skill Roller')

    name_entry_win_label = tk.Label(
        name_entry_win,
        text='Please enter your characters name below',
        font=('Arial',15)
    )
    name_entry_win_label.pack()

    name_entry_win_entry = tk.Entry(name_entry_win)
    name_entry_win_entry.pack()

    name_entry_win_submit_btn = tk.Button(
        name_entry_win,
        text='Submit',
        font=('Arial'),
        command=name_entry_check
    )
    name_entry_win_submit_btn.pack()

root = tk.Tk()
root.title('Welcome')
root.geometry('195x87+0+0')

root_title = tk.Label(
    root,
    text='DnD Skill Roller',
    font=('Arial',20,'bold')
)
root_title.grid(
    row=1,
    column=1,
    columnspan=2
)

start_button = tk.Button(
    root,
    text='Start',
    font=('Arial'),
    width=20,
    command=name_entry
)
start_button.grid(
    row=2,
    column=2,
    columnspan=2
)

exit_button = tk.Button(
    root,
    text='Exit',
    font=('Arial'),
    width=20,
    command=sys.exit
)
exit_button.grid(
    row=3,
    column=1,
    columnspan=2
)

root.mainloop()