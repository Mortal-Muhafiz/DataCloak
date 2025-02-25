import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from encryption import extract_data, hide_data  # Import the function we created
from ttkbootstrap import Style
import time

# Initialize Main Window
root = tk.Tk()
root.title("DataCloak")
root.config(bg="black")
root.resizable(True, True)

# Function to center window
def center_window(window, width=600, height=400):
    """Centers the given window on the desktop screen."""
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

# Apply centering
center_window(root, 800, 600)

# Tesla Font (or fallback)
TESLA_FONT = ("Magnetar", 35, "bold")
BUTTON_FONT = ("Montserrat", 14, "bold")
HEADING_FONT = ("Montserrat", 20, "bold")

# Splash Screen Elements
splash_label = tk.Label(root, text="DataCloak", fg="white", bg="black", font=TESLA_FONT)
splash_label.pack(expand=True)

# Smooth Fade-in Effect
def fade_in():
    for i in range(0, 21):  # Increase steps for smoothness
        root.attributes("-alpha", i / 20)  
        root.update()
        time.sleep(0.05)

# Button Hover Effect
def on_enter(event):
    event.widget.config(bg="#0077b6", fg="white")  # Professional Blue Hover

def on_leave(event):
    event.widget.config(bg="#1a1a1a", fg="white")  # Dark Grey Default

style = ttk.Style()
style.configure("Accent.TButton", font=("Arial", 12), padding=8)
style.configure("Secondary.TButton", font=("Arial", 11), padding=6)

# Transition to Main Menu
def show_main_menu():
    splash_label.destroy()  # Remove splash label

    # Main Menu UI
    welcome_label = ttk.Label(root, text="Welcome to DataCloak", font=HEADING_FONT, foreground="black")
    welcome_label.pack(pady=20)

    btn_frame = tk.Frame(root, bg="black")
    btn_frame.pack(expand=True)

    button_style = {
        "font": BUTTON_FONT,
        "fg": "white",
        "bg": "#1a1a1a",  # Dark Grey Professional Look
        "width": 18,
        "height": 1,  # Reduced Height for Sleeker Look
        "borderwidth": 0,
        "relief": "flat",
        "highlightthickness": 2,
        "highlightbackground": "#0077b6",  # Subtle Blue Outline
        "highlightcolor": "#0077b6",
        "cursor": "hand2",
    }

    # Hide Data Button
    hide_btn = tk.Button(btn_frame, text="🛡️ Hide Data", **button_style, command=show_hide_screen)
    hide_btn.pack(pady=10, ipadx=10, ipady=5)
    hide_btn.bind("<Enter>", on_enter)
    hide_btn.bind("<Leave>", on_leave)

    # Extract Data Button
    extract_btn = tk.Button(btn_frame, text="📂 Extract Data", **button_style, command=show_extract_screen)
    extract_btn.pack(pady=10, ipadx=10, ipady=5)
    extract_btn.bind("<Enter>", on_enter)
    extract_btn.bind("<Leave>", on_leave)

    # Footer Text
    footer_label = ttk.Label(root, text="Secure Your Secrets with DataCloak", font=("Montserrat", 10, "bold"), foreground="black", background="white")
    footer_label.pack(side="bottom", pady=10)

def back_to_main():
    # Destroy all widgets inside root
    for widget in root.winfo_children():
        widget.destroy()
    
    # Call function to reload the main menu
    show_main_menu()
    
# Placeholder Functions for Hide & Extract Screens
def show_hide_screen():
    # Clear the main window
    for widget in root.winfo_children():
        widget.destroy()
    
    # Create a frame for Hide Data screen
    hide_frame = tk.Frame(root, bg="black")
    hide_frame.pack(fill="both", expand=True)

    # Header Label (Centered at Top)
    heading_label = ttk.Label(root, text="🔒 Hide Data", font=HEADING_FONT, foreground="black")
    heading_label.place(relx=0.5, rely=0.1, anchor="center")
    
    # Add border (80% width of window)
    ttk.Separator(root, orient="horizontal").place(relx=0.5, rely=0.15, anchor="center", relwidth=0.8)

    # Frame for Input Fields (Centered)
    form_frame = tk.Frame(root, bg="black")
    form_frame.place(relx=0.5, rely=0.4, anchor="center")
    
    # Function to browse files
    def select_message_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        msg_file_entry.delete(0, tk.END)
        msg_file_entry.insert(0, file_path)

    def select_cover_file():
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        cover_file_entry.delete(0, tk.END)
        cover_file_entry.insert(0, file_path)

    def select_output_folder():
        folder_path = filedialog.askdirectory(title="Select Destination Folder")
        output_folder_entry.delete(0, tk.END)
        output_folder_entry.insert(0, folder_path)

    # Create Input Fields
    ttk.Label(form_frame, text="Message File:", foreground="black").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    msg_file_entry = ttk.Entry(form_frame, width=40)
    msg_file_entry.grid(row=0, column=1, padx=10, pady=5)
    ttk.Button(form_frame, text="📂 Browse", command=select_message_file).grid(row=0, column=2, padx=10, pady=5)

    ttk.Label(form_frame, text="Cover File:", foreground="black").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    cover_file_entry = ttk.Entry(form_frame, width=40)
    cover_file_entry.grid(row=1, column=1, padx=10, pady=5)
    ttk.Button(form_frame, text="📂 Browse", command=select_cover_file).grid(row=1, column=2, padx=10, pady=5)

    ttk.Label(form_frame, text="Output Folder:", foreground="black").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    output_folder_entry = ttk.Entry(form_frame, width=40)
    output_folder_entry.grid(row=2, column=1, padx=10, pady=5)
    ttk.Button(form_frame, text="📂 Browse", command=select_output_folder).grid(row=2, column=2, padx=10, pady=5)

    ttk.Label(form_frame, text="Encryption Algorithm:", foreground="black").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    algorithm_combo = ttk.Combobox(form_frame, values=["AES-128"], state="readonly", width=38)
    algorithm_combo.grid(row=3, column=1, padx=10, pady=5)
    algorithm_combo.current(0)  # Default selection

    ttk.Label(form_frame, text="Password:", foreground="black").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    password_entry = ttk.Entry(form_frame, width=40, show="*")
    password_entry.grid(row=4, column=1, padx=10, pady=5)

    ttk.Label(form_frame, text="Confirm Password:", foreground="black").grid(row=5, column=0, padx=10, pady=5, sticky="w")
    confirm_password_entry = ttk.Entry(form_frame, width=40, show="*")
    confirm_password_entry.grid(row=5, column=1, padx=10, pady=5)

    # Function to handle hiding data
    def handle_hide_data():
        message_file = msg_file_entry.get()
        cover_file = cover_file_entry.get()
        output_folder = output_folder_entry.get()
        algorithm = algorithm_combo.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        if not message_file or not cover_file or not output_folder or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required!")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        try:
            output_path = hide_data(message_file, cover_file, output_folder, algorithm, password, confirm_password)
            messagebox.showinfo("Success", f"Data hidden successfully!\nStego image saved at:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to hide data: {str(e)}")

    hide_btn = ttk.Button(hide_frame, text="🔐 Hide Data", command=handle_hide_data, width= 30)
    hide_btn.place(relx=0.5, rely=0.64, anchor="center")

    back_btn = ttk.Button(hide_frame, text="⬅ Back to Menu", command=back_to_main, width= 25)
    back_btn.place(relx=0.5, rely=0.7, anchor="center")

    # Add Border Before Footer
    ttk.Separator(root, orient="horizontal").place(relx=0.5, rely=0.75, anchor="center", relwidth=0.8)

    # Footer Text
    footer_label = ttk.Label(root, text="Secure Your Secrets with DataCloak", font=("Montserrat", 10, "bold"), foreground="black", background="white")
    footer_label.pack(side="bottom")

def show_extract_screen():
    # Clear the main window
    for widget in root.winfo_children():
        widget.destroy()

    # Main Frame for Extract Data (Full Window)
    extract_frame = tk.Frame(root, bg="black")
    extract_frame.pack(fill="both", expand=True)

    # Header Label (Centered at Top)
    header_label = ttk.Label(root, text="📂 Extract Data", font=HEADING_FONT, foreground="black")
    header_label.place(relx=0.5, rely=0.1, anchor="center")

    # Border Line (Under Header, 80% Width)
    ttk.Separator(root, orient="horizontal").place(relx=0.5, rely=0.15, anchor="center", relwidth=0.8)

    # Form Frame (Centered in Window)
    form_frame = tk.Frame(root, bg="black")
    form_frame.place(relx=0.5, rely=0.4, anchor="center")

    # File Selection Functions
    def select_input_file():
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            input_file_entry.delete(0, tk.END)
            input_file_entry.insert(0, file_path)

    def select_output_folder():
        folder_path = filedialog.askdirectory(title="Select Destination Folder")
        if folder_path:
            output_folder_entry.delete(0, tk.END)
            output_folder_entry.insert(0, folder_path)

    # Input Stego File
    ttk.Label(form_frame, text="Input Stego File:", foreground="black").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    input_file_entry = ttk.Entry(form_frame, width=40)
    input_file_entry.grid(row=0, column=1, padx=10, pady=5)
    ttk.Button(form_frame, text="📂 Browse", command=select_input_file).grid(row=0, column=2, padx=10, pady=5)

    # Output Folder Selection
    ttk.Label(form_frame, text="Output Folder:", foreground="black").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    output_folder_entry = ttk.Entry(form_frame, width=40)
    output_folder_entry.grid(row=1, column=1, padx=10, pady=5)
    ttk.Button(form_frame, text="📂 Browse", command=select_output_folder).grid(row=1, column=2, padx=10, pady=5)

    # Password Entry
    ttk.Label(form_frame, text="Password:", foreground="black").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    password_entry = ttk.Entry(form_frame, width=40, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=5)

    # Function to Extract Data
    def extract_callback():
        stego_file = input_file_entry.get()
        output_folder = output_folder_entry.get()
        password = password_entry.get()

        if not stego_file or not output_folder or not password:
            messagebox.showerror("Error", "Please fill all fields!")
            return

        try:
            extracted_file_path = extract_data(stego_file, output_folder, password)
            messagebox.showinfo("Success", f"Data extracted successfully!\nSaved at: {extracted_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to extract data!\n{e}")

    # Extract Data Button (Centered Below Form)
    extract_btn = ttk.Button(root, text="🔓 Extract Data", command=extract_callback)
    extract_btn.place(relx=0.5, rely=0.6, anchor="center")

    # Back Button (Below Extract Button)
    back_btn = ttk.Button(root, text="⬅ Back", command=back_to_main)
    back_btn.place(relx=0.5, rely=0.7, anchor="center")

    # Footer Border (80% Width)
    ttk.Separator(root, orient="horizontal").place(relx=0.5, rely=0.75, anchor="center", relwidth=0.8)

    # Footer Text
    footer_label = ttk.Label(root, text="Secure Your Secrets with DataCloak", font=("Montserrat", 10, "bold"), foreground="black", background="white")
    footer_label.pack(side="bottom")

# Run Splash & Transition
fade_in()
root.after(1500, show_main_menu)  # Transition after 1.5s

# Start Tkinter Main Loop
root.mainloop()
