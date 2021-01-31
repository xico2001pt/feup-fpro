"""
Sometimes we want to send the same email to many people. In such situation, the body of the email is the same for everyone except for some specific fields (e.g., name or address).

Given a file with a list of names (names) and another file with the template of the body of the email (mail_template), write a Python function mail_merge(names, mail_template) that merges together each name in names with the mail_template and returns a list with all emails. To do that, you should find the tag <name> in the mail template and replace it by each person name to obtain each element of the list.

For example, if we have these two files:

1. names.txt

João Correia Lopes
João Damas
Pedro Ferreira
Ricardo Cruz

2. template.txt

Dear <name>,
This is the body of the e-mail!
Regards,
FPRO Student

(Please do not open or save files using Notepad. Use Spyder or other modern editor that supports Unicode UTF-8 encoding. If necessary, open the file in Python with open(..., encoding='utf-8').)

    mail_merge("names.txt", "template.txt") should return the list ['Dear João Correia Lopes,\n\nThis is the body of the e-mail!\nRegards,\nFPRO Student', 'Dear João Damas,\n\nThis is the body of the e-mail!\nRegards,\nFPRO Student', 'Dear Pedro Ferreira,\n\nThis is the body of the e-mail!\nRegards,\nFPRO Student', 'Dear Ricardo Cruz,\n\nThis is the body of the e-mail!\nRegards,\nFPRO Student']

"""

def mail_merge(names, mail_template):
    emails = []
    with open(names) as n:
        with open(mail_template) as m:
            template = m.read()
            for name in n.readlines():
                emails.append(template.replace('<name>', name.strip()))
    return emails