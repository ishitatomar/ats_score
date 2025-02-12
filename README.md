Hello everyone,

I recently completed a project that allows users to upload their resumes in PDF format and automatically calculate the ATS (Applicant Tracking System) score. This score is an indication of how well a resume matches with the requirements based on word frequency analysis.

Features:
- Interactive GUI: Built with Python's Tkinter library for a smooth and user-friendly experience.
- PDF Upload: Users can easily upload their resumes in PDF format.
- ATS Score Calculation: The ATS score is calculated based on the frequency of words used in the resume, excluding common stop words.
- Error Handling: Message boxes are used to notify users of unexpected errors, ensuring a smooth interaction.
  
Technologies Used:
- Python
- Tkinter (for GUI)
- PyMuPDF (for PDF text extraction)
- Regular Expressions (for text processing)
- Collections.Counter (for word frequency analysis)
  
Outcome:
The application computes the ATS score based on the most relevant terms from the resume. The result is displayed instantly on the interface, providing users with insights into how their resume might perform in an Applicant Tracking System.

