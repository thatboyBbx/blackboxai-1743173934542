import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from classifier import DocumentClassifier
from utils.file_utils import validate_file, create_category_folder
import os

class DocumentClassifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Offline Document Classifier")
        self.root.geometry("800x600")
        
        # Initialize classifier
        self.classifier = DocumentClassifier()
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        ttk.Label(main_frame, text="Document Classifier", font=("Helvetica", 16)).pack(pady=10)
        
        # Upload button
        upload_btn = ttk.Button(
            main_frame,
            text="Upload Document",
            command=self.upload_document
        )
        upload_btn.pack(pady=20)
        
        # Results frame
        self.results_frame = ttk.Frame(main_frame)
        self.results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(
            self.root,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def upload_document(self):
        file_path = filedialog.askopenfilename(
            title="Select Document",
            filetypes=[("Documents", "*.pdf *.docx *.txt")]
        )
        
        if not file_path:
            return
            
        try:
            # Validate file
            if not validate_file(file_path):
                raise ValueError("Invalid document format")
                
            # Classify document
            category = self.classifier.predict(file_path)
            
            # Organize file
            target_folder = create_category_folder(category)
            target_path = os.path.join(target_folder, os.path.basename(file_path))
            os.rename(file_path, target_path)
            
            # Show results
            self.show_results(file_path, category, target_path)
            self.status_var.set(f"Document classified as: {category}")
            
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_var.set("Error processing document")
    
    def show_results(self, file_path, category, target_path):
        # Clear previous results
        for widget in self.results_frame.winfo_children():
            widget.destroy()
            
        # Show classification results
        ttk.Label(self.results_frame, text="Classification Results:", font=("Helvetica", 12)).pack(anchor=tk.W)
        
        info = [
            f"File: {os.path.basename(file_path)}",
            f"Type: {category}",
            f"Location: {target_path}"
        ]
        
        for text in info:
            ttk.Label(self.results_frame, text=text).pack(anchor=tk.W, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = DocumentClassifierApp(root)
    root.mainloop()