import sqlite3, json
import pymupdf


def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.
        page_number (int, optional): The specific page number to extract text from. 
                                     If None, extracts from all pages.

    Returns:
        str: The extracted text from the PDF.
    """
    try:
        doc = pymupdf.open(pdf_path)
        text = []
        for page in doc:
            text.append(page.get_text())
        return text
    except Exception as e:
        print(f"An error occurred while reading the PDF: {e}")
        return ""


def init_db(DB):
    """
    Initializes the database by creating necessary tables.
    """
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    cursor.executescript('''
                   PRAGMA foreign_keys=ON;

                   CREATE TABLE IF NOT EXISTS entry (
                       id INTEGER PRIMARY KEY,
                       type TEXT DEFAULT '[]',
                       tags TEXT DEFAULT '[]',
                       language TEXT NOT NULL,
                       lemma TEXT DEFAULT '[]',
                       origin_lemma TEXT DEFAULT '[]',
                       definition TEXT DEFAULT '[]',
                       example TEXT DEFAULT '[]',
                       special_info TEXT NOT NULL,
                       source_list INTEGER NOT NULL,
                       source_page INTEGER NOT NULL
                   ); 

                   CREATE VIRTUAL TABLE IF NOT EXISTS entry_fts USING fts5(
                       lemma, definition, type, tags, language, source_list,
                       content="", tokenize="unicode61"
                   );        
    ''')
    
    conn.commit()
    conn.close()


