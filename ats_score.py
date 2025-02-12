import tkinter as tk
from tkinter import filedialog, messagebox
import fitz  # PyMuPDF
import re
from collections import Counter

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(pdf_file)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.lower()  # Convert to lowercase for matching

# Function to calculate ATS score
def calculate_ats_score():
    resume_file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])  # Open file dialog for PDF
    if not resume_file:
        messagebox.showerror("File Error", "Please select a PDF resume file.")
        return

    # Extract resume text
    try:
        resume_text = extract_text_from_pdf(resume_file)
    except Exception as e:
        messagebox.showerror("Error", f"Error reading the PDF file: {e}")
        return

    # Clean the resume text to remove any non-alphabetic characters
    resume_words = re.findall(r'\b\w+\b', resume_text)
    
    # Count the frequency of each word in the resume
    word_counts = Counter(resume_words)

    # Remove common stop words (basic list)
    stop_words = set([
        "the", "and", "to", "a", "in", "of", "on", "for", "with", "is", "it", "you", "that", "this", "from", "by", "be", "as", "at", "was", "an"
    ])
    filtered_word_counts = {word: count for word, count in word_counts.items() if word not in stop_words}

    # Convert filtered_word_counts back to a Counter object to use most_common
    filtered_word_counts = Counter(filtered_word_counts)

    # Calculate the ATS score as the percentage of the most frequent words in the resume
    ats_score = (len(filtered_word_counts) / sum(filtered_word_counts.values())) * 100 if filtered_word_counts else 0

    # Display the ATS score
    ats_score_label.config(text=f"ATS Score: {ats_score:.2f}%", fg="green")

# Create the main window
root = tk.Tk()
root.title("ATS Score Calculator")
root.geometry("500x400")
root.config(bg="#f4f4f9")  # Light background color for a modern look

# Create and place the widgets
title_label = tk.Label(root, text="ATS Score Calculator", font=("Helvetica", 18, "bold"), bg="#f4f4f9", fg="darkred")
title_label.pack(pady=20)

# Button to calculate the ATS score
calculate_button = tk.Button(root, text="Select Resume and Calculate ATS Score", command=calculate_ats_score,
                             bg="#4CAF50", fg="black", font=("Arial", 14, "bold"), relief="flat", height=3, width=30)
calculate_button.pack(pady=20)

# ATS score label
ats_score_label = tk.Label(root, text="ATS Score: 0%", font=("Arial", 14), bg="#f4f4f9")
ats_score_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
