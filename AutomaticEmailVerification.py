import requests
import re

def fetch(emailAddress,body=1,subject=1,sender=1,link=1):
    result = requests.get("http://temp-mail.org/", cookies={"mail":emailAddress.replace("@","%40")}).text
    matchedTable = re.search('(?<=<table id=\"mails\" class=\"table table-striped\">)((.|\s)*?)(?=</table>)', result)
    if matchedTable == None:
        exit("No Email Table Found on "+ emailAddress)
    data = matchedTable.group(0)
    matchedBody = re.search("(?<=<tbody>)((.|\s)*?)(?=<\/tbody>)", data)
    if matchedBody == None:
        exit("No Email Table Body Found on "+ emailAddress)
    data = matchedBody.group(0)
    matchedMails = re.findall("(?<=<tr>)((.|\s)*?)(?=<\/tr>)",data)
    if len(matchedMails) == 0:
        exit("No Emails Found on "+ emailAddress)
    toReturn = []
    for mail in matchedMails:
        link_data = ""
        sender_data = ""
        subject_data = ""
        body_data = ""

        if link:
            link_data = re.search('(?<=href=\")((.|\s)*?)(?=\")',mail[0].strip()).group(0)
        if sender:
            sender_data = re.search('(?<=&lt;)((.|\s)*?)(?=&gt;)',mail[0].strip()).group(0)
        if subject:
            subject_data = re.search('(?<=class=\"title-subject\">)((.|\s)*?)(?=</a>)',mail[0].strip()).group(0)
        if body:
            request = requests.get(link)
            if(request.status_code == 200):
                body_re = re.search("(?<=<div class=\"pm-text\">)((.|\s)*?)(?=</div>\s*?<div class=\"adblockMailView pm-info\">)",request.text)
                if body_re != None:
                    body_data = mess_re.group(0)
        toReturn.append({
            "link": link_data,
            "body": body_data,
            "sender": sender_data,
            "subject": subject_data
        })
    return toReturn

def getAvailableDomains():
    url = "https://temp-mail.org/en/option/change/"
    startingText = '<select name="domain" class="form-control" id="domain">'
    endingText = '</select>'
    expression = '(?<='+startingText+')(.|\s)*?(?='+endingText+')'
    request = requests.get(url)
    if(request.status_code == 200):
        data = request.text
        searchForSelect = re.search(expression,data)
        if searchForSelect != None:
            data = searchForSelect.group(0).strip()
            startingText = '<option value="'
            endingText = '">'
            expression = '(?<='+startingText+')(.*)(?='+endingText+')'
            searchForOptions = re.findall(expression,data)
            if searchForOptions != None:
                data = searchForOptions
                return data
            else:
                exit("Can't Search For Options")
        else:
            exit("Can't Search For Select")
    else:
        exit("Can't Fatch the url "+url)

def getADomain():
    return getAvailableDomains()[0]
# Source: https://github.com/imlolman/Automatic-Email-Verification