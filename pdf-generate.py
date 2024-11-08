# Correct special characters by replacing curly quotes and em-dashes with standard ASCII equivalents
cleaned_content = content.replace("’", "'").replace("–", "-").replace("—", "-")

# Create PDF again with the cleaned content
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", "", 12)

# Write cleaned content to PDF
for line in cleaned_content.splitlines():
    # Set different font styles for headers and content
    if line.startswith("##"):
        pdf.set_font("Arial", "B", 12)  # Bold for main headers
    elif line.startswith("#"):
        pdf.set_font("Arial", "B", 14)  # Larger bold for section headers
    else:
        pdf.set_font("Arial", "", 10)  # Regular for normal text
    
    # Write line to PDF
    pdf.multi_cell(0, 10, line)
    pdf.ln(5)

# Save the PDF with cleaned content
pdf_output_path = "/mnt/data/Spring_Interview_Guide.pdf"
pdf.output(pdf_output_path)

# Create Word document with cleaned content
doc = Document()
doc.add_heading("Spring Framework Interview Preparation Guide for Programmers", 0)

# Add cleaned content to Word doc
for line in cleaned_content.splitlines():
    if line.startswith("##"):
        doc.add_heading(line, level=1)
    elif line.startswith("#"):
        doc.add_heading(line, level=2)
    elif line.strip():
        doc.add_paragraph(line)

# Save Word file with cleaned content
doc_output_path = "/mnt/data/Spring_Interview_Guide.docx"
doc.save(doc_output_path)

pdf_output_path, doc_output_path
