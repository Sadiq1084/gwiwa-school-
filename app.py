from flask import Flask, render_template

app = Flask(__name__)

# ===== EDIT YOUR SCHOOL INFO HERE ONLY =====
SCHOOL_NAME = "GOVERNMENT JUNIOR ARABIC SECONDARY SCHOOL, GWIWA"
MOTTO = "Knowledge, Discipline, Excellence"
PRINCIPAL_NAME = "Malam [Add Name Here]"
ADDRESS = "Gwiwa, Katsina State, Nigeria"
PHONE = "+234 800 000 0000"
EMAIL = "gwiwaschool@email.com"
YEAR_ESTABLISHED = "1995"

@app.route('/')
def home():
    return render_template('index.html',
        school_name=SCHOOL_NAME,
        motto=MOTTO,
        principal=PRINCIPAL_NAME,
        address=ADDRESS,
        phone=PHONE,
        email=EMAIL,
        year=YEAR_ESTABLISHED
    )

if __name__ == '__main__':
    app.run(debug=True)
