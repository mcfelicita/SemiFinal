from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return(
        "Fullname: Mietchelle P. Felicits<br>"
        "Section: BSIT 3-A 2nd LAB<br>"
        "Subject System Integration and Architecture<br>"
        "Exam: Semi-Final Exam"
    )

if __name__ == '__main_':
    app.run(debug=True)
