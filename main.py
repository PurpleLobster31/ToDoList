import customtkinter as ctk

global frame_text


class MyScrollableCheckboxFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, title):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.checkboxes = []
        
        # for i, value in enumerate(self.values):
        #     checkbox = ctk.CTkCheckBox(self, text=value)
        #     checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
        #     self.checkboxes.append(checkbox)
            
    def add_checkbox(self):
        dialog = ctk.CTkInputDialog(title="New Checkbox", text="Type in the name and due date: ")
        checkbox_text = dialog.get_input()
        if checkbox_text:
            checkbox = ctk.CTkCheckBox(self, text=checkbox_text)
            checkbox.grid(row=len(self.checkboxes), column=0, padx = 10, pady=(10,0), sticky="w")
            self.checkboxes.append(checkbox)
            self.get()
        
    
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
        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        #UI elements
        self.assignments_frame = MyScrollableCheckboxFrame(self, title="Assignments")
        self.assignments_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsew")
        self.assignments_button = ctk.CTkButton(self, text="Add Assignment", command=self.assignments_frame.add_checkbox)
        self.assignments_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        
        self.tests_frame = MyScrollableCheckboxFrame(self, title="Tests")
        self.tests_frame.grid(row=0, column=1, padx=(0,10), pady=(10,0),sticky="nsew")
        self.tests_button = ctk.CTkButton(self, text="Add Test",command=self.tests_frame.add_checkbox)
        self.tests_button.grid(row=3, column=1, padx=(0,10), pady=10, sticky="nsew")
            
        self.house_frame = MyScrollableCheckboxFrame(self, title="House Chores")
        self.house_frame.grid(row=0, column=2, padx=(0,10), pady=(10,0), sticky="nsew")
        self.house_button = ctk.CTkButton(self, text="Add House Chore", command=self.house_frame.add_checkbox )
        self.house_button.grid(row=3, column=2, padx=(0,10), pady=10, sticky="nsew")
        
        
        
app = App()
app.mainloop()