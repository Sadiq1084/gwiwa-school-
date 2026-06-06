from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    news = [
        "Admission for 2026 is now open",
        "Mid-term exams start next Monday", 
        "Parents meeting this Friday 2PM"
    ]
    return render_template('index.html', school_name="Government junior Arabic secondary school Gwiwa ", news=news)

if __name__ == '__main__':
    app.run()
