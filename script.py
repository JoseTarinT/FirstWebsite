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
    else:
        return render_template("succes.html", year = year, links = links)
    

if __name__=="__main__":
    app.run(debug=True) # 'debug=True' will print out possible Python errors on the web page helping us trace the errors.
                        # However, in a production environment, you would want to set it to False as to avoid any security issues.
