from flask import Flask, request, jsonify
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

app = Flask(__name__)

@app.get("/")
def validate():
    data = request.get_json()

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    service = Service(ChromeDriverManager().install())

    browser = webdriver.Chrome(service=service, options=options)

    browser.get("https://pre.ufcg.edu.br:8443/ControleAcademicoOnline/")

    return jsonify(data), 200

if __name__ == "__main__":
    app.run(debug=True)

