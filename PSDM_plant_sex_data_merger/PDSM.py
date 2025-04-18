import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import ImageTk, Image
import pd_back_end
import n2_backend_pd

# colors
button_color = "#faebd9"
text_color = "#fff5e5"
basf_color = '#f8991d'

# main
def main():
    root = PDSM_App()
    root.mainloop()

class PDSM_App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("PDSM")
        self.geometry("550x500")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)  # Allow column 1 to expand
        self.columnconfigure(3, weight=0)
        self.columnconfigure(11, weight=0)

        self.configure(background=basf_color)
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure('TCombobox', fieldbackground=text_color, background=button_color, selectforeground=button_color)
        style.map('TCombobox', fieldbackground=[('readonly', button_color)])

        # logo/ image basf
        try:
            logo_path = "basf-logo-9.png"
            logo = Image.open(logo_path)
            logo = logo.resize((200, 100))
            logo = ImageTk.PhotoImage(logo)
            self.iconphoto(False, logo)
            logo_label = ttk.Label(self, image=logo, background=basf_color)
            logo_label.image = logo
            logo_label.grid(row=0, column=0, columnspan=3, pady=1)

        except tk.TclError as e:
            print("Error:", e)

        # Name
        def create_bordered_label(master, text, row, column, columnspan=3):
            label_frame = tk.Frame(master, borderwidth=1, background="white")
            label_frame.grid(row=row, column=column, columnspan=columnspan, sticky="nsew", padx=5, pady=5)
            label = tk.Label(label_frame, text=text, font=("Helvetica", 14,), background=basf_color, fg=text_color)
            label.pack(fill="both", expand=True)
            return label_frame

        psdm = create_bordered_label(self, "Plant Sex Data Merger", row=1, column=0, columnspan=10)

        self.add_file_path()

    def add_file_path(self):
        style = ttk.Style()
        style.configure("Custom.TFrame", background=basf_color)

        # List frame voor de bestanden
        list_frame = ttk.Frame(self, style="Custom.TFrame")
        list_frame.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=5, pady=(10, 5))

        # Listbox (midden in het frame)
        self.listbox = tk.Listbox(list_frame, width=50, height=10, bg="white")
        self.listbox.grid(row=0, column=1, sticky="nsew")

        # Verticale scrollbar (rechts van de Listbox)
        v_scroll = ttk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        v_scroll.grid(row=0, column=2, sticky="ns")

        # Horizontale scrollbar (onder de Listbox)
        h_scroll = ttk.Scrollbar(list_frame, orient="horizontal", command=self.listbox.xview)
        h_scroll.grid(row=1, column=1, sticky="ew")

        # Koppel scrollbars aan Listbox
        self.listbox.config(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

        list_frame_button = ttk.Frame(self, style="Custom.TFrame")
        list_frame.grid(row=3, column=0,  sticky="nsew", pady=(10, 5))

        # upload CSV knop
        upload_xls_file_button = tk.Button(self, text=" + CSV file ", background=button_color,
                                           command=self.select_file)
        upload_xls_file_button.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        # Verwijder-knop (links onderaan)
        remove_file_button = tk.Button(self, text="Delete", background=button_color, width=8, height=1,
                                       command=self.remove_file)
        remove_file_button.grid(row=4, column=0, sticky="ns", padx=10, pady=5)

        # Maak de kolommen en rijen dynamisch
        list_frame.columnconfigure(1, weight=1)
        list_frame.rowconfigure(0, weight=1)

        # option
        self.date_check = tk.BooleanVar()

        date_check_box = tk.Checkbutton(self, text='Add date if empty',variable=self.date_check, onvalue=True, offvalue=False, background=basf_color)
        date_check_box.grid(row=5, column=0, sticky="w", padx=10, pady=15)

        upload_xls_file_button = tk.Button(self, text="Merge data", background=button_color,
                                           command=self.send_data_to_backend)
        upload_xls_file_button.grid(row=6, column=1, sticky="w", padx=10, pady=5)


    def select_file(self):
        # Open file dialog to select file
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

        if file_path:
            # Add the file path to the listbox
            self.listbox.insert(tk.END, file_path)

    def remove_file(self):
        # Get the selected file in the listbox
        selected_index = self.listbox.curselection()

        if selected_index:
            # Remove the selected file from the listbox
            self.listbox.delete(selected_index)
        else:
            # Show a message if no file is selected
            messagebox.showwarning("No file selected", "Please select a file to remove.")

    def send_data_to_backend(self):
        paths = []
        all_paths = self.listbox.get(0, tk.END)
        for p in all_paths:
            paths.append(p)
        edit_date = self.date_check.get()

        if len(paths) >= 1:
            n2_backend_pd.receive_data(paths, edit_date)

        else:
            messagebox.showwarning("No files to merge", "There are no files in the list to merge.")
            return




if __name__ == "__main__":
    main()
