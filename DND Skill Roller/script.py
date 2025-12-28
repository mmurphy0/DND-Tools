import random, sys
import tkinter as tk
from tkinter import messagebox, Toplevel

def reset():
    global strength_bonus, dexterity_bonus, constitution_bonus, intelligence_bonus, wisdom_bonus, charisma_bonus
    
    strength_bonus = 0
    dexterity_bonus = 0
    constitution_bonus = 0
    intelligence_bonus = 0
    wisdom_bonus = 0
    charisma_bonus = 0

    skills_win.destroy()


def saveskills():
    with open('DND Skill Roller/Skill Roll History.txt','a') as file:
        file.write('Character: ' + str(name) + '\n' + 'Strength: ' + str(strength_sum) + '\n' + 'Dexterity: ' + str(dexterity_sum) + '\n' + 'Constitution: ' + str(constitution_sum) + '\n' + 'Intelligence: ' + str(intelligence_sum) + '\n' + 'Wisdom: ' + str(wisdom_sum) + '\n' + 'Charisma: ' + str(charisma_sum) + '\n' + '----------' + '\n')
    
    messagebox.showinfo('Confirmation','Character Skills successfully saved') 
    reset()


def showskills():
    global skills_win

    skills_win = Toplevel()
    skills_win.title('DnD Skill Roller')
    skills_win.geometry('220x230+0+0')
    skills_win.resizable(False,False)

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

    strength_bonus_int = strength_bonus.get()
    dexterity_bonus_int = dexterity_bonus.get()
    constitution_bonus_int = constitution_bonus.get()
    intelligence_bonus_int = intelligence_bonus.get()
    wisdom_bonus_int = wisdom_bonus.get()
    charisma_bonus_int = charisma_bonus.get()

    dice = list(range(1,7))

    strength = []
    for i in range(4):
        rolled = random.choice(dice)
        strength.append(rolled)
    strength.sort()
    strength.pop(0)
    for i in strength:
        strength_sum = i + strength_sum + int(strength_bonus_int)

    dexterity = []
    for i in range(4):
        rolled = random.choice(dice)
        dexterity.append(rolled)
    dexterity.sort()
    dexterity.pop(0)
    for i in dexterity:
        dexterity_sum = i + dexterity_sum + int(dexterity_bonus_int)

    constitution = []
    for i in range(4):
        rolled = random.choice(dice)
        constitution.append(rolled)
    constitution.sort()
    constitution.pop(0)
    for i in constitution:
        constitution_sum = i + constitution_sum + int(constitution_bonus_int)

    intelligence = []
    for i in range(4):
        rolled = random.choice(dice)
        intelligence.append(rolled)
    intelligence.sort()
    intelligence.pop(0)
    for i in intelligence:
        intelligence_sum = i + intelligence_sum + int(intelligence_bonus_int)

    wisdom = []
    for i in range(4):
        rolled = random.choice(dice)
        wisdom.append(rolled)
    wisdom.sort()
    wisdom.pop(0)
    for i in wisdom:
        wisdom_sum = i + wisdom_sum + int(wisdom_bonus_int)

    charisma = []
    for i in range(4):
        rolled = random.choice(dice)
        charisma.append(rolled)
    charisma.sort()
    charisma.pop(0)
    for i in charisma:
        charisma_sum = i + charisma_sum + int(charisma_bonus_int)

    add_characterbonuses_win.destroy()
    showskills()

def skillbonus_typecheck():
    try:
        num1 = int(strength_bonus.get())
        num2 = int(dexterity_bonus.get())
        num3 = int(constitution_bonus.get())
        num4 = int(intelligence_bonus.get())
        num5 = int(wisdom_bonus.get())
        num6 = int(charisma_bonus.get())
        
        rollskills()
    except ValueError:
        messagebox.showerror('Error','Only numbers can be entered')


def skillbonus_presencecheck():
    if str(strength_bonus).strip():
        if str(dexterity_bonus).strip():
            if str(constitution_bonus).strip():
                if str(intelligence_bonus).strip():
                    if str(wisdom_bonus).strip():
                        if str(charisma_bonus).strip():
                            skillbonus_typecheck()
    else:
        messagebox.showerror('Error','All text boxes must have a number in. No bonus = 0')


def add_characterbonuses():
    global add_characterbonuses_win, strength_bonus, dexterity_bonus, constitution_bonus, intelligence_bonus, wisdom_bonus, charisma_bonus

    add_characterbonuses_win = Toplevel()
    add_characterbonuses_win.geometry('235x250+0+0')
    add_characterbonuses_win.resizable(False,False)
    add_characterbonuses_win.title('DND Skill Roller')

    add_characterbonuses_title = tk.Label(
        add_characterbonuses_win,
        text='Add Character Bonuses',
        font=('Arial',20,'bold')
    )
    add_characterbonuses_title.grid(
        row=1,
        column=1,
        columnspan=2
    )

    add_characterbonuses_info = tk.Label(
        add_characterbonuses_win,
        text='No Bonus = 0',
        font=('Arial',15)
    )
    add_characterbonuses_info.grid(
        row=3,
        column=1,
        columnspan=2
    )

    strength_label = tk.Label(
        add_characterbonuses_win,
        text='Strength:',
        font=('Arial',15)
    )
    strength_label.grid(
        row=5,
        column=1
    )
    strength_bonus = tk.Entry(
        add_characterbonuses_win,
        font=('Arial'),
        width=5
    )
    strength_bonus.grid(
        row=5,
        column=2
    )

    dexterity_label = tk.Label(
        add_characterbonuses_win,
        text='Dexterity:',
        font=('Arial',15)
    )
    dexterity_label.grid(
        row=6,
        column=1
    )
    dexterity_bonus = tk.Entry(
        add_characterbonuses_win,
        font=('Arial'),
        width=5
    )
    dexterity_bonus.grid(
        row=6,
        column=2
    )

    constitution_label = tk.Label(
        add_characterbonuses_win,
        text='Constitution:',
        font=('Arial',15)
    )
    constitution_label.grid(
        row=7,
        column=1
    )
    constitution_bonus = tk.Entry(
        add_characterbonuses_win,
        font=('Arial'),
        width=5
    )
    constitution_bonus.grid(
        row=7,
        column=2
    )

    intelligence_label = tk.Label(
        add_characterbonuses_win,
        text='Intelligence:',
        font=('Arial',15)
    )
    intelligence_label.grid(
        row=8,
        column=1
    )
    intelligence_bonus = tk.Entry(
        add_characterbonuses_win,
        font=('Arial'),
        width=5
    )
    intelligence_bonus.grid(
        row=8,
        column=2
    )

    wisdom_label = tk.Label(
        add_characterbonuses_win,
        text='Wisdom:',
        font=('Arial',15)
    )
    wisdom_label.grid(
        row=9,
        column=1
    )
    wisdom_bonus = tk.Entry(
        add_characterbonuses_win,
        width=5,
        font=('Arial')
    )
    wisdom_bonus.grid(
        row=9,
        column=2
    )

    charisma_label = tk.Label(
        add_characterbonuses_win,
        text='Charisma:',
        font=('Arial',15)
    )
    charisma_label.grid(
        row=10,
        column=1
    )
    charisma_bonus = tk.Entry(
        add_characterbonuses_win,
        font=('Arial'),
        width=5
    )
    charisma_bonus.grid(
        row=10,
        column=2
    )

    continue_button = tk.Button(
        add_characterbonuses_win,
        text='Continue',
        font=('Arial'),
        width=20,
        command=skillbonus_presencecheck
    )
    continue_button.grid(
        row=12,
        column=1,
        columnspan=2
    )

    name_entry_win.destroy()


def name_entry_check():
    global name
    
    name = name_entry_win_entry.get()

    if name.strip():
        add_characterbonuses()
    else:
        messagebox.showinfo('Error','A Name must be entered')


def name_entry():
    global name_entry_win_entry, name_entry_win
    
    name_entry_win = Toplevel()
    name_entry_win.geometry('285x80+0+0')
    name_entry_win.resizable(False,False)
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

def reset_sum_values():
    global strength_sum, dexterity_sum, constitution_sum, intelligence_sum, wisdom_sum, charisma_sum

    strength_sum = 0
    dexterity_sum = 0
    constitution_sum = 0
    intelligence_sum = 0
    wisdom_sum = 0
    charisma_sum = 0

    name_entry()


def reset_bonus_values():
    global strength_bonus, dexterity_bonus, constitution_bonus, intelligence_bonus, wisdom_bonus, charisma_bonus
    
    strength_bonus = 0
    dexterity_bonus = 0
    constitution_bonus = 0
    intelligence_bonus = 0
    wisdom_bonus = 0
    charisma_bonus = 0

    reset_sum_values()


root = tk.Tk()
root.title('DND Skill Roller')
root.geometry('195x87+0+0')
root.resizable(False,False)

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
    command=reset_bonus_values
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