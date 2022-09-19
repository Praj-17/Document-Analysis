#The pdf2image library can be used
#You can install it simply using,


#Once installed you can use following code to get images.

from encodings import utf_8
from pdf2image import convert_from_path
pages = convert_from_path("Injection Molding Handbook by Dominick V. Rosato P.E., Donald V. Rosato PH.D. (auth.), Dominick V. Rosato P. E., Donald V. Rosato PH.D., Marlene G. Rosato P. E. (eds.) (z-lib.org).pdf", 500)

#Saving pages in jpeg format

for i, page in enumerate(pages):
    page.save(f'Injection_Molding_Design_Guidelines_2017_images2//out{i}.jpg', 'JPEG')