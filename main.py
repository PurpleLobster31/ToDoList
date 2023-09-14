import customtkinter as ctk
import pickle
from CTkMessagebox import CTkMessagebox

def save_object(obj, filename):
    try:
        with open(filename, "wb") as file:
            pickle.dump(obj, file, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)

def load_object(filename):
    try:
        with open(filename, 'rb') as file:
            obj = pickle.load(file)
        return obj
    except Exception as e:
        print(f"Error while loading: {str(e)}")
        return []
    
class MyScrollableCheckboxFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, title, dump):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.dump=dump
        self.root=master
        self.checkboxes = []
        self.load_checkboxes()
        
    def set_checkboxes(self):
        for checkbox in self.checkboxes:
            checkbox.configure(command=self.root.calculate_progress)

    def save_checkboxes(self):
        checkbox_texts = []
        checkbox_states = []
        
        for checkbox in self.checkboxes:
            c_text = checkbox.cget("text")
            c_state = checkbox.get()
            checkbox_texts.append(c_text)
            checkbox_states.append(c_state)
        
        checkbox_dump = {checkbox_texts[i]: checkbox_states[i] for i in range(len(checkbox_texts))}
        save_object(checkbox_dump, self.dump)
        
         
    def load_checkboxes(self):
        self.checkboxes_dict = load_object(self.dump)
        for key in self.checkboxes_dict:
            checkbox = ctk.CTkCheckBox(self, text=key)
            if self.checkboxes_dict[key]==1:
                checkbox.toggle()
            checkbox.grid(row=len(self.checkboxes), column=0, padx = 10, pady=(10,0), sticky="w")
            self.checkboxes.append(checkbox)
            self.get()
    
    def add_checkbox(self):
        dialog = ctk.CTkInputDialog(title="New Checkbox", text="Type in the name and due date:\nFormat (Name - Date) or (Name)")
        
        #center window
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        width = 300
        height = 200
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        dialog.geometry("%dx%d+%d+%d" % (width, height, x, y))
        
        checkbox_text_unfiltered = dialog.get_input()   
        
        if checkbox_text_unfiltered:
            if " - " in checkbox_text_unfiltered:
                checkbox_text = checkbox_text_unfiltered.replace(" - ", "\n")
            else:
                checkbox_text = checkbox_text_unfiltered
                
            checkbox = ctk.CTkCheckBox(self, text=checkbox_text, command=self.root.calculate_progress)
            checkbox.grid(row=len(self.checkboxes), column=0, padx = 10, pady=(10,0), sticky="w")
            self.checkboxes.append(checkbox)
            self.get()
            self.root.calculate_progress()
            
        
    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes
    
    def clear(self):
        for checkbox in self.checkboxes:
            checkbox.destroy()
        
        self.checkboxes.clear()  
        self.root.calculate_progress()  
        
#App frame
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # self.after(0, lambda:self.state("zoomed"))
        
        #System settings
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width = 1280
        height = 800
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.title("My Plans")
        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        #UI elements
        #region Assignments
        self.assignments_frame = MyScrollableCheckboxFrame(self, title="Assignments", dump="assignments_checkboxes.dump")
        self.assignments_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsew")
        self.assignments_button = ctk.CTkButton(self, text="Add Assignment", command=self.assignments_frame.add_checkbox)
        self.assignments_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.clear_a_button = ctk.CTkButton(self, text = "Clear Cards", command=self.assignments_frame.clear)
        self.clear_a_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
        #endregion
        
        #region Tests
        self.tests_frame = MyScrollableCheckboxFrame(self, title="Tests", dump="tests_checkboxes.dump")
        self.tests_frame.grid(row=0, column=1, padx=(0,10), pady=(10,0),sticky="nsew")
        self.tests_button = ctk.CTkButton(self, text="Add Test",command=self.tests_frame.add_checkbox)
        self.tests_button.grid(row=3, column=1, padx=(0,10), pady=10, sticky="nsew")
        self.clear_t_button = ctk.CTkButton(self, text = "Clear Cards", command=self.tests_frame.clear)
        self.clear_t_button.grid(row=4, column=1, padx=(0,10), pady=10, sticky="nsew")
        #endregion
       
        #region House Chores     
        self.house_frame = MyScrollableCheckboxFrame(self, title="House Chores", dump="house_checkboxes.dump")
        self.house_frame.grid(row=0, column=2, padx=(0,10), pady=(10,0), sticky="nsew")
        self.house_button = ctk.CTkButton(self, text="Add House Chore", command=self.house_frame.add_checkbox)
        self.house_button.grid(row=3, column=2, padx=(0,10), pady=10, sticky="nsew")
        self.clear_h_button = ctk.CTkButton(self, text = "Clear Cards", command=self.house_frame.clear)
        self.clear_h_button.grid(row=4, column=2, padx=(0,10), pady=10, sticky="nsew")
        #endregion
        
        self.frames = [self.assignments_frame, self.tests_frame, self.house_frame]
        for frame in self.frames:
            frame.set_checkboxes()
        
        self.progress_text = ctk.CTkLabel(self, text="0%", font=("CTkDefaultFont", 15, "bold"))
        self.progress_text.grid(row=5, column=1, padx=10, pady=10, sticky="nsew")
        
        self.progress_bar = ctk.CTkProgressBar(self)
        self.progress_bar.grid(row=6, column=0, columnspan=3, sticky="nsew")
        self.calculate_progress()
        
        self.assignments_frame.update()
        self.tests_frame.update()
        self.house_frame.update()
    
    def on_closing(self):
        msg = CTkMessagebox(title="Exit?", message="Do you want to close the program?",
                            icon="question", option_1="No", option_2="Yes")
        response = msg.get()
        
        if response=="Yes":
            self.house_frame.save_checkboxes()
            self.tests_frame.save_checkboxes()
            self.assignments_frame.save_checkboxes()
            app.destroy()       
        else:
            pass
    
    def calculate_progress(self):
            total_activities = len(self.house_frame.checkboxes) + len(self.tests_frame.checkboxes) + len(self.assignments_frame.checkboxes)
            completed_activities = len(self.house_frame.get()) + len(self.tests_frame.get()) + len(self.assignments_frame.get())
            if total_activities==0:
                self.progress_text.configure(text="No activities on board.")
                self.progress_bar.set(1)
            else:
                per = completed_activities/total_activities
                text_per = int(per*100)
                self.progress_text.configure(text="{}% of activies completed!".format(text_per))
                self.progress_bar.set(per)

app = App()
app.protocol("WM_DELETE_WINDOW", app.on_closing)
app.mainloop()

