import tkinter as tkinter

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Form Completer")

        
        

        self.input1_label = tkinter.Label(self.master, text="Open Swim:")
        self.input1_label.grid(row=0, column=0, padx=10, pady=10)

        self.input2_label = tkinter.Label(self.master, text="Family Swim:")
        self.input2_label.grid(row=1, column=0, padx=10, pady=10)

        self.input3_label = tkinter.Label(self.master, text="Lap Swim:")
        self.input3_label.grid(row=2, column=0, padx=10, pady=10)

        self.input4_label = tkinter.Label(self.master, text="Rental:")
        self.input4_label.grid(row=3, column=0, padx=10, pady=10)

        self.input5_label = tkinter.Label(self.master, text="Goggles:")
        self.input5_label.grid(row=5, column=0, padx=10, pady=10)

        self.input6_label = tkinter.Label(self.master, text = "Nose Plugs")
        self.input6_label.grid(row=4, column=0, padx=10, pady=10)

        self.input7_label = tkinter.Label(self.master, text = "Enter 0.25's: ")
        self.input7_label.grid(row=0, column=2, padx=10, pady=10)

        self.input8_label = tkinter.Label(self.master, text = "Enter 1.00's: ")
        self.input8_label.grid(row=1, column=2, padx=10, pady=10)

        self.input9_label = tkinter.Label(self.master, text = "Enter 2.00's: ")
        self.input9_label.grid(row=2, column=2, padx=10, pady=10)

        self.input10_label = tkinter.Label(self.master, text = "Enter 5.00's: ")
        self.input10_label.grid(row=3, column=2, padx=10, pady=10)

        self.input11_label = tkinter.Label(self.master, text = "Enter 10.00's: ")
        self.input11_label.grid(row=4, column=2, padx=10, pady=10)

        self.input12_label = tkinter.Label(self.master, text = "Enter 20.00's: ")
        self.input12_label.grid(row=5, column=2, padx=10, pady=10)

        self.input13_label = tkinter.Label(self.master, text = "Enter 50.00's: ")
        self.input13_label.grid(row=6, column=2, padx=10, pady=10)

        self.input14_label = tkinter.Label(self.master, text = "Enter 100.00's: ")
        self.input14_label.grid(row=7, column=2, padx=10, pady=10) 

        self.input15_label = tkinter.Label(self.master, text = "Minus Interact Total: ")
        self.input15_label.grid(row=8, column=2, padx=10, pady=10)

        self.input16_label = tkinter.Label(self.master, text = "Coin Subtotal: ")
        self.input16_label.grid(row=9, column=2, padx=10, pady=10)

        self.input17_label = tkinter.Label(self.master, text = "Cash Subtotal: ")
        self.input17_label.grid(row=10, column=2, padx=10, pady=10)

        self.grand_total = tkinter.Label(self.master, text = "Grand Total: ")
        self.grand_total.grid(row=11, column=2, padx=10, pady=10)

        
        self.interact_label = tkinter.Label(self.master, text="Interact:")
        self.interact_label.grid(row=6, column=0, padx=10, pady=10)

        self.total = tkinter.Label(self.master, text="Total")
        self.total.grid(row=9, column=0, padx=10, pady=10)

        


        

        

        self.input1_entry = tkinter.Entry(self.master)
        self.input1_entry.grid(row=0, column=1, padx=10, pady=10)

        self.input2_entry = tkinter.Entry(self.master)
        self.input2_entry.grid(row=1, column=1, padx=10, pady=10)

        self.input3_entry = tkinter.Entry(self.master)
        self.input3_entry.grid(row=2, column=1, padx=10, pady=10)

        self.input4_entry = tkinter.Entry(self.master)
        self.input4_entry.grid(row=3, column=1, padx=10, pady=10)

        self.input5_entry = tkinter.Entry(self.master)
        self.input5_entry.grid(row=5, column=1, padx=10, pady=10)

        self.input6_entry = tkinter.Entry(self.master) 
        self.input6_entry.grid(row=4, column=1, padx=10, pady=10)

        self.input7_entry = tkinter.Entry(self.master)
        self.input7_entry.grid(row=0, column=3, padx=10, pady=10)
        self.input7_entry.configure(state='disabled')
        quarter = self.input7_entry.get()

        self.input8_entry = tkinter.Entry(self.master)
        self.input8_entry.grid(row=1, column=3, padx=10, pady=10)
        self.input8_entry.configure(state='disabled')

        self.input9_entry = tkinter.Entry(self.master)
        self.input9_entry.grid(row=2, column=3, padx=10, pady=10)
        self.input9_entry.configure(state='disabled')

        self.input10_entry = tkinter.Entry(self.master)
        self.input10_entry.grid(row=3, column=3, padx=10, pady=10)
        self.input10_entry.configure(state='disabled')

        self.input11_entry = tkinter.Entry(self.master)
        self.input11_entry.grid(row=4, column=3, padx=10, pady=10)
        self.input11_entry.configure(state='disabled')

        self.input12_entry = tkinter.Entry(self.master)
        self.input12_entry.grid(row=5, column=3, padx=10, pady=10)
        self.input12_entry.configure(state='disabled')

        self.input13_entry = tkinter.Entry(self.master)
        self.input13_entry.grid(row=6, column=3, padx=10, pady=10)
        self.input13_entry.configure(state='disabled')

        self.input14_entry = tkinter.Entry(self.master)
        self.input14_entry.grid(row=7, column=3, padx=10, pady=10)
        self.input14_entry.configure(state='disabled')

        self.input15_entry = tkinter.Entry(self.master)
        self.input15_entry.grid(row=8, column=3, padx=10, pady=10)
        self.input15_entry.configure(state='disabled')

        self.input16_entry = tkinter.Entry(self.master)
        self.input16_entry.grid(row=9, column=3, padx=10, pady=10)
        self.input16_entry.configure(state='disabled')

        self.input17_entry = tkinter.Entry(self.master)
        self.input17_entry.grid(row=10, column=3, padx=10, pady=10)
        self.input17_entry.configure(state='disabled')

        self.grand_total_entry = tkinter.Entry(self.master)
        self.grand_total_entry.grid(row=11, column=3, padx=10, pady=10)
        self.grand_total_entry.config(state='readonly')
        
        

        self.interact_entry = tkinter.Entry(self.master)
        self.interact_entry.grid(row=6, column=1, padx=10, pady=10)
       
        self.total_entry = tkinter.Entry(self.master)
        self.total_entry.grid(row= 9, column=1, padx=10, pady=10)
        self.total_entry.config(state='readonly')

        

        

        self_calculate_button = tkinter.Button(self.master, text="Calculate", command=self.calculate)
        self_calculate_button.grid(row=9, column=0, padx=10, pady=10)
        

        self_subtotals_button = tkinter.Button(self.master, text="Get Subtotals", command=self.subtotals)
        self_subtotals_button.grid(row=10, column=0, padx=10, pady=10)


    def calculate(self):
        input1 = float(self.input1_entry.get())
        input2 = float(self.input2_entry.get())
        input3 = float(self.input3_entry.get())
        input4 = float(self.input4_entry.get())
        input5 = float(self.input5_entry.get())
        input6 = float(self.input6_entry.get())
        interact = float(self.interact_entry.get())
        
        


        
        
        interact = float(self.interact_entry.get())
        
        t = 200.00
        

        result = input1 + input2 + input3 + input4 + input5 + input6
        cash_owed = result
        
        amount_needed = result - t
        

        amount_owed = int(result // 100)
        amount_owed1 = int((result % 100) // 50)
        amount_owed2 = int(((result % 100)) %50 // 20)
        amount_owed3 = int((((result % 100)) %50 %20) // 10)
        amount_owed4 = int(((((result % 100)) %50 %20) %10) // 5)
        amount_owed5 = int((((((result % 100)) %50 %20) %10) %5) // 2)
        amount_owed6 = int(((((((result % 100)) %50 %20) %10) %5) %2) // 1)
        amount_owed7 = int((((((((result % 100)) %50 %20) %10) %5) %2) %1) // 0.25)

        
        
        

        self.input14_entry.config(state="normal")
        self.input14_entry.delete(0, tkinter.END)
        self.input14_entry.insert(0, amount_owed)
        self.input14_entry.config(state="readonly")

        self.input13_entry.config(state="normal")
        self.input13_entry.delete(0, tkinter.END)
        self.input13_entry.insert(0, amount_owed1)
        self.input13_entry.config(state="readonly")

        self.input12_entry.config(state="normal")
        self.input12_entry.delete(0, tkinter.END)
        self.input12_entry.insert(0, amount_owed2)
        self.input12_entry.config(state="readonly")

        self.input11_entry.config(state="normal")
        self.input11_entry.delete(0, tkinter.END)
        self.input11_entry.insert(0, amount_owed3)
        self.input11_entry.config(state="readonly")

        self.input10_entry.config(state="normal")
        self.input10_entry.delete(0, tkinter.END)
        self.input10_entry.insert(0, amount_owed4)
        self.input10_entry.config(state="readonly")

        self.input9_entry.config(state="normal")
        self.input9_entry.delete(0, tkinter.END)
        self.input9_entry.insert(0, amount_owed5)
        self.input9_entry.config(state="readonly")


        self.input8_entry.config(state="normal")
        self.input8_entry.delete(0, tkinter.END)
        self.input8_entry.insert(0, amount_owed6)
        self.input8_entry.config(state="readonly")


        self.input7_entry.config(state="normal")
        

        self.input7_entry.delete(0, tkinter.END)
        self.input7_entry.insert(0, amount_owed7)
        self.input7_entry.config(state="readonly")

        self.input15_entry.config(state="normal")
        self.input15_entry.delete(0, tkinter.END)
        self.input15_entry.insert(0, cash_owed)
        self.input15_entry.config(state="readonly")

        self.grand_total_entry.config(state="normal")
        self.grand_total_entry.delete(0, tkinter.END)
        self.grand_total_entry.insert(0, result)
        self.grand_total_entry.config(state="readonly")

        self.total_entry.config(state="normal")
        self.total_entry.delete(0, tkinter.END)
        self.total_entry.insert(0, result)
        self.total_entry.config(state="readonly")
        
        
        
        
        
       
    def subtotals(self):
       
        input7 = float(self.input7_entry.get())
        input8 = float(self.input8_entry.get())
        input9 = float(self.input9_entry.get())
        input10 = float(self.input10_entry.get())
        input11 = float(self.input11_entry.get())
        input12 = float(self.input12_entry.get())
        input13 = float(self.input13_entry.get())
        input14 = float(self.input14_entry.get())
        coin_count = input7 * 0.25 + input8 * 1.00 + input9 * 2.00
        cash_count = input10 * 5.00 + input11 * 10.00 + input12 * 20.00 + input13 * 50.00 + input14 * 100.00

        self.input16_entry.config(state="normal")
        self.input16_entry.delete(0, tkinter.END)
        self.input16_entry.insert(0, coin_count)
        self.input16_entry.config(state="readonly")

        self.input17_entry.config(state="normal")
        self.input17_entry.delete(0, tkinter.END)
        self.input17_entry.insert(0, cash_count)
        self.input17_entry.config(state="readonly")


    
        

        

if __name__ == "__main__":
    root = tkinter.Tk()
    app = Calculator(root)
    
    root.mainloop()