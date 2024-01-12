import datetime
import tkinter as tk
from tkinter import font

def create_swim_table(root, data):
    
    

    num_rows = len(data)
    num_cols = len(data[0])
    people = []

    custom_font = font.Font(family="Helvetica", size=12)

    for _ in range(2):
        empty_row = ["" for _ in range(num_cols)]
        data.insert(0, empty_row)

        
    def validate_input(char):
        if len(char) <=1 and char == "a" or char == "c" or char == "s" or char == "p":
            return True
        else:
            return False
        


    for i in range(num_rows):
        row_people = []
        for j in range(num_cols):
            entry = tk.Entry(root, width=10, borderwidth=2, font=custom_font, justify='center')
            entry.grid(row=i + 2, column=j)
            entry.insert(tk.END, data[i][j])
            entry['validate'] = 'key'
            entry['validatecommand'] = (entry.register(validate_input), '%p')
           
            row_people.append(entry)

        people.append(row_people)
        

    return people



root = tk.Tk()
root.title("Swim Registration")
root.geometry("550x600")

label_text = "Swim Numbers"
label = tk.Label(root, text=label_text, font=("Helvetica", 18, "bold"))
label.grid(row=0, columnspan=7)

custom_font = font.Font(family="Helvetica", size=12)
swim_label = tk.Label(root, text="Swim Type: ", font = custom_font, justify='center')
swim_label.grid(row=0, column= 0)

swim_type = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
swim_type.grid(row=0, column=1)



table_data = [["", "", "", "", "", "",]]
table_data.append(["", "", "", "", "", "",])
table_data.append(["", "", "", "", "", "",])
table_data.append(["", "", "", "", "", "",])
table_data.append(["", "", "", "", "", "",])
table_data.append(["", "", "", "", "", "",])
table_data.append(["", "", "", "", "", "",])
table_data.append(["", "", "", "", "", "",])
table_data.append(["", "", "", "", "", "",])
table_data.append(["", "", "", "", "", "",])
table_data.append(["", "", "", "", "", "",])




input_boxes = create_swim_table(root, table_data)

blank_label = tk.Label(root, text="")
blank_label.grid(row=22, columnspan=7)

adult_label = tk.Label(root, text="Adults: ")
adult_label.grid(row=23, column=0)

num_of_adults = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
num_of_adults.grid(row=23, column=1)

child_label = tk.Label(root, text="Children: ")
child_label.grid(row=24, column=0)

num_of_children = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
num_of_children.grid(row=24, column=1)

senior_label = tk.Label(root, text="Seniors: ")
senior_label.grid(row=25, column=0)

num_of_seniors = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
num_of_seniors.grid(row=25, column=1)

pass_label = tk.Label(root, text="Passes: ")
pass_label.grid(row=26, column=0)

num_of_passes = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
num_of_passes.grid(row=26, column=1)

adult_cost_label = tk.Label(root, text="Adult Cost: ")
adult_cost_label.grid(row=23, column=2)

adult_cost = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
adult_cost.grid(row=23, column=3)

child_cost_label = tk.Label(root, text="Child Cost: ")
child_cost_label.grid(row=24, column=2)

child_cost = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
child_cost.grid(row=24, column=3)

senior_cost_label = tk.Label(root, text="Senior Cost: ")
senior_cost_label.grid(row=25, column=2)

senior_cost = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
senior_cost.grid(row=25, column=3)

pass_cost_label = tk.Label(root, text="Pass Cost: ")
pass_cost_label.grid(row=26, column=2)

pass_cost = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
pass_cost.grid(row=26, column=3)

total_cost = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
total_cost.grid(row=27, column=3)

total_label = tk.Label(root, text="Total: ")
total_label.grid(row=27, column=2)

total_people_attended_label = tk.Label(root, text="People: ")
total_people_attended_label.grid(row=28, column=2)

total_people_attended = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
total_people_attended.grid(row=28, column=3)





def retrieve_data(data):
    retrieve_data = []
    for row in input_boxes:
        row_data = []
        
        for entry in row:
            row_data.append(entry.get())
        retrieve_data.append(row_data)
    print(retrieve_data)

def count_people():
    adults = 0
    children = 0
    seniors = 0
    passes = 0

    
    
    

    for row in input_boxes:
        for entry in row:
            if entry.get() == 'a' or entry.get() == 'A':
                adults += 1
            elif entry.get() == 'c' or entry.get() == 'C':
                children += 1
            elif entry.get() == 's' or entry.get() == 'S':
                seniors += 1
            elif entry.get() == 'p' or entry.get() == 'P':
                passes += 1
            

        
    num_of_adults = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
    num_of_adults.grid(row=23, column=1)
    num_of_adults.insert(tk.END, adults)

    num_of_children = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
    num_of_children.grid(row=24, column=1)
    num_of_children.insert(tk.END, children)

    num_of_seniors = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
    num_of_seniors.grid(row=25, column=1)
    num_of_seniors.insert(tk.END, seniors)

    num_of_passes = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
    num_of_passes.grid(row=26, column=1)
    num_of_passes.insert(tk.END, passes)

    adult_cost = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
    adult_cost.grid(row=23, column=3)
    adult_cost.insert(tk.END, adults * 3.50)

    child_cost = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
    child_cost.grid(row=24, column=3)
    child_cost.insert(tk.END, children * 2.50)

    senior_cost = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
    senior_cost.grid(row=25, column=3)
    senior_cost.insert(tk.END, seniors * 3.25)

    pass_cost = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
    pass_cost.grid(row=26, column=3)
    pass_cost.insert(tk.END, passes * 0.00)

    total_cost = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
    total_cost.grid(row=27, column=3)
    total_cost.insert(tk.END, (adults * 3.50) + (children * 2.50) + (seniors * 3.25) + (passes * 0.00))

    total_people_attended = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 12), justify='center')
    total_people_attended.grid(row=28, column=3)
    total_people_attended.insert(tk.END, adults + children + seniors + passes)

def reset():
    for row in input_boxes:
        for entry in row:
            entry.delete(0, tk.END)

    num_of_adults.delete(0, tk.END)
    num_of_children.delete(0, tk.END)
    num_of_seniors.delete(0, tk.END)
    num_of_passes.delete(0, tk.END)
    adult_cost.delete(0, tk.END)
    child_cost.delete(0, tk.END)
    senior_cost.delete(0, tk.END)
    pass_cost.delete(0, tk.END)
    total_cost.delete(0, tk.END)
    total_people_attended.delete(0, tk.END)

      
custom_font = font.Font(family="Helvetica", size=12)


calculate_button = tk.Button(root, text="Calculate", command=count_people, font=custom_font)
calculate_button.grid(row=28, column=0)

reset_button = tk.Button(root, text="Reset", command=reset, font=custom_font)
reset_button.grid(row=28, column=1)


def update_date():
    date = datetime.datetime.now().strftime("%m/%d/%Y")
    date_label = tk.Label(root, text=date, font=custom_font)
    date_label.grid(row=0, column=4)
    date_label.config(text=date)
    date_label.after(1000, update_date)

update_date()



        

    










    
root.mainloop()
