import customtkinter as ctk

class MyCheckboxFrame(ctk.CTkFrame):
    def __init__(self, master, values, title):
        super().__init__(master)
        self.values = values
        self.title=title
        self.checkboxes = []

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        
        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="nsew")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

class MyScrollableCheckboxFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, title, tests, assignments):
        super().__init__(master, label_text=title, orientation="horizontal")
        self.grid_columnconfigure((0,1), weight = 1)
        self.grid_rowconfigure(0, weight=1)
        self.tests = tests
        self.assignments = assignments
        
        self.assignments_frame = MyCheckboxFrame(self, self.assignments, "Assignments")
        self.assignments_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsew") 
        
        self.tests_frame = MyCheckboxFrame(self, self.tests, "Tests")
        self.tests_frame.grid(row=0, column=1, padx=(0,10), pady=(10,0), sticky="nsew") 
        
        
        
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
        tests = ["EDVT - 10/10", "BIOA - 11/10"]
        assignments = ["Read book - 08/10", "Draw sketch of a house - 12/11"]
        
        self.scrollable_frame = MyScrollableCheckboxFrame(self, title = "UFABC", tests=tests, assignments=assignments)
        self.scrollable_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        
app = App()
app.mainloop()