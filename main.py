import random
from flask import Flask
app = Flask(__name__)
from ingredients import ingredientsList
import gunicorn
@app.get("/")
def welcome_text():
    return {"Text":"Welcome in SelfBetterAPI"}
@app.get("/ingredientsList")
def get_ingredients_list():
    return ingredientsList
if __name__ == "__main__":
    app.run()
