from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello GWIWA School! Your app is live 🚀"

if __name__ == '__main__':
    app.run()
