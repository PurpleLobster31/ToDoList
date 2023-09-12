import customtkinter as ctk



class MyScrollableCheckboxFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []
        self.add_checkbox = ctk.CTkButton(master, text="Press to add new card.", command=create_card)
        
        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def create_card(self):
        dialog = ctk.CTkInputDialog(title="New Card", text="Type in the name of the card + final date:")
        text = dialog.get_input()
        if text:
            pass
            

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes
        
        
        
#App frame
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.after(0, lambda:self.state("zoomed"))
        
        #System settings
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.geometry("800x600")
        self.title("My Plans")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        #UI elements
        frames = []
       
        
app = App()
app.mainloop()