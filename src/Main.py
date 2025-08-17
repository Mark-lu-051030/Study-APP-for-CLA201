import Database as db
import DataProcessing as dp

DB = r"P:\编程\python\Study-APP-for-CLA201\data\root_database.db"
pdf_path = "P:\编程\python\Study-APP-for-CLA201\data\The Greek Alphabet, Study Sheet-merged-merged (1).pdf"

data = db.extract_text_from_pdf(pdf_path)
print(data[-1])