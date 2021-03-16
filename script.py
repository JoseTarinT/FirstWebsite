import os
import smtplib
from flask import Flask, render_template, request

# Configure app

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/registration')
def registration():
    return render_template("registration.html")

@app.route('/register', methods=["POST"])
def register():
    email = request.form.get("email")
    year = request.form.get("year")
    links = ["https://www.youtube.com/watch?v=OUTvglBTQ8Y", "https://www.youtube.com/watch?v=dg5XxDBFi0c",
             "https://www.youtube.com/watch?v=lBP7QQYN1IU", "https://www.youtube.com/watch?v=wA4ChhQ38GQ",
             "https://www.youtube.com/watch?v=Ji021RYgGXQ", "https://www.youtube.com/watch?v=bfnCOTgrl9g",
             "https://www.youtube.com/watch?v=DDAhqFhuSMU", "https://www.youtube.com/watch?v=Rtsp6KrRE8I",
             "https://www.youtube.com/watch?v=rtFGpfrdlMI", "https://www.youtube.com/watch?v=8xDIPTOGrwY",
             "https://www.youtube.com/watch?v=GfIIiHcOHCE"]
    if not email or not year:
        return "failure"
    if year == '2009-2010':
        text = ''.join(["This is the link of the final of ", year , links[0]])
    elif year == '2010-2011':
        text = ''.join(["This is the link of the final of ", year , links[1]])
    elif year == '2011-2012':
        text = ''.join(["This is the link of the final of ", year + links[2]])
    elif year == '2012-2013':
        text = ''.join(["This is the link of the final of ", year + links[3]])
    elif year == '2013-2014':
        text = ''.join(["This is the link of the final of ", year + links[4]])
    elif year == '2014-2015':
        text = ''.join(["This is the link of the final of ", year + links[5]])
    elif year == '2015-2016':
        text = ''.join(["This is the link of the final of ", year + links[6]])
    elif year == '2016-2017':
        text = ''.join(["This is the link of the final of ", year + links[7]])
    elif year == '2017-2018':
        text = ''.join(["This is the link of the final of ", year + links[8]])
    elif year == '2018-2019':
        text = ''.join(["This is the link of the final of ", year + links[9]])
    else:
        text = ''.join(["This is the link of the final of ", year + links[10]])
    
    # Send email to the user after registration
    subject = "Subject: You are registered."
    message = '{}\n\n{}'.format(subject, text)
    server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    server.starttls()
    server.login("joseluis_tt88@hotmail.com", os.getenv("EMPASSWORD")) # os.getenv() allows to access data store in local enviroment in your computer without show publicly.
    server.sendmail("joseluis_tt88@hotmail.com", email, message) # Here the 1º email is the 'from' email; 'email' is the variable that stores the email that user input and it is the 'to' email.
    return render_template("succes.html", year=year, links=links)
    

if __name__=="__main__":
    app.run(debug=True) # 'debug=True' will print out possible Python errors on the web page helping us trace the errors.
                        # However, in a production environment, you would want to set it to False as to avoid any security issues.
