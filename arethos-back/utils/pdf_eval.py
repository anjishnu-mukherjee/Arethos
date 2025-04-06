from pdf2image import convert_from_path
from utils.imageAnalysis import analyze_image
import io
import fitz

def pdf_to_images(pdf_path, dpi=300):
    """Convert each page of a PDF into a list of images."""
    images = convert_from_path(pdf_path, dpi=dpi)  # Higher DPI = better quality
    return images

def generate_txt_from_pdf(pdf_path):
    text_data = []
    image_list = pdf_to_images(pdf_path)

    for image in image_list:
        image_bytes = io.BytesIO()
        image.save(image_bytes, format="PNG")
        image_bytes = image_bytes.getvalue()
        text_data.append(analyze_image(image_bytes))

    file_path = f"tmp/{pdf_path.split(".")[0]}.txt"
    with open(file_path, "w") as f:
        f.writelines(text_data)

    return file_path

def pdf_contains_images(pdf_path):
    """Check if the PDF contains any images."""
    try:
        with fitz.open(pdf_path) as pdf:
            for page_num in range(len(pdf)):
                images = pdf[page_num].get_images(full=True)  # Extract images
                if images:
                    return True  # Found at least one image
    except Exception as e:
        print(f"Error checking PDF for images: {e}")
    
    return False  # No images found

def extract_text_from_pdf(pdf_path):
    """Extract text from a machine-readable PDF."""
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text("text")  # Extracts plain text
        return text.strip()
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None
    
def convert_pdf_txt(pdf_path):
    """Get text data from PDF."""
    try:
        if pdf_contains_images(pdf_path):
            # If the PDF contains images, convert to images and analyze
            text_file_path = generate_txt_from_pdf(pdf_path)
        else:
        #    extract text from pdf file
            text = extract_text_from_pdf(pdf_path)
            if text:
                text_file_path = f"tmp/{pdf_path.split('.')[0]}.txt"
                with open(text_file_path, "w") as f:
                    f.write(text)
            else:
                print("No text found in the PDF.")
                return None


        return text_file_path

    except Exception as e:
        print(f"Error processing PDF: {e}")
        return None