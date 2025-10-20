import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bengali to English Translator")
        self.root.geometry("600x400")
        
        # Configure style
        style = ttk.Style()
        style.configure("Custom.TButton", padding=6, font=("Arial", 10))
        style.configure("Custom.TLabel", font=("Arial", 12))
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Bangla text input
        ttk.Label(main_frame, text="Enter Bengali Text:", style="Custom.TLabel").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        self.bangla_text = tk.Text(main_frame, height=6, width=50, font=("Arial", 12))
        self.bangla_text.grid(row=1, column=0, pady=(0, 10), sticky=(tk.W, tk.E))
        
        # Translate button
        ttk.Button(main_frame, text="Translate", style="Custom.TButton",
                  command=self.translate).grid(row=2, column=0, pady=(0, 10))
        
        # English text output
        ttk.Label(main_frame, text="English Translation:", style="Custom.TLabel").grid(row=3, column=0, sticky=tk.W, pady=(0, 5))
        self.english_text = tk.Text(main_frame, height=6, width=50, font=("Arial", 12))
        self.english_text.grid(row=4, column=0, pady=(0, 10), sticky=(tk.W, tk.E))
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        
    def translate(self):
        try:
            # Get Bengali text
            bangla_text = self.bangla_text.get("1.0", tk.END).strip()
            
            if not bangla_text:
                messagebox.showwarning("Warning", "Please enter some text to translate!")
                return
            
            # Translate text
            translator = GoogleTranslator(source='bn', target='en')
            translation = translator.translate(text=bangla_text)
            
            # Clear previous translation and insert new one
            self.english_text.delete("1.0", tk.END)
            self.english_text.insert("1.0", translation)
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
