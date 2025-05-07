import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return(
        "Fullname: Mietchelle P. Felicita<br>"
        "Section: BSIT 3-A 2nd LAB<br>"
        "Subject: System Integration and Architecture 1<br>"
        "Exam: Semi-Final Exam"
    )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
