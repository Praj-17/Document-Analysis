import fitz

DIGITIZED_FILE = "InjectionMoldedpart.pdf"
# SCANNED_FILE = ""

sentences = []


#OCR using default parameter:

# with fitz.open(DIGITIZED_FILE) as doc:
#     for page in doc:
#         text = page.get_text()
#         # print(text)

#OCR using 'Block' parameter:

with fitz.open(DIGITIZED_FILE) as doc:
    for page in doc:
        texts = page.get_text("text").split("\n")
        # print(text)
        for text in texts:
                # Splitting the text block into sentences and adding them to the list
                sentences.extend(text.split(". "))
                # print(sentences)
#OCR using 'words' parameter:

# with fitz.open(DIGITIZED_FILE) as doc:
#     for page in doc:
#         text = page.get_text("words")
#         # print(text)
#         for text in text:
#                 # Splitting the text block into sentences and adding them to the list
#                 sentences.extend(text.split(". "))
#                 print(sentences)