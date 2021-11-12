from docx import Document
from docx.shared import Inches

document = Document()
# Add profile picture
document.add_picture('profile_pic.jpg', width=Inches(2.0))

# Get input from the user
name = input('What is your name?')
phone_number = input('What is your phone number?')
email = input('What is your email address?')

document.add_paragraph(
    name + ' | ' + phone_number + ' | ' + email)

document.save('cv.docx')
