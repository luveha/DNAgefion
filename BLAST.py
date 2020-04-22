from selenium import webdriver

def BLAST():
    browser = webdriver.Firefox()
    browser.get('https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome')
    knap = browser.find_element_by_css_selector('#b1') #blastknap
    textarea = browser.find_element_by_css_selector('#seq') #input
    textarea.send_keys(removeSpace(str(DNAinputBox.get())))
    knap.click()

#BLAST
BLASTbutton = Button(program, text='BLAST!!', command=BLAST, bg='white', fg='blue')


