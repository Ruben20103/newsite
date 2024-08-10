import random
from flask import Flask

app = Flask(__name__)

facts = ["Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.",
          "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",
          "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время."]

cointoss = ["heads", "tails"]

@app.route("/random_facts")
def random_facts():
    random_facts = random.choice(facts)
    return f'<h1>{random_facts}</h1>'

@app.route("/")
def random_cointoss():
    return 'Welcome to the site. Here you can know random facts about technological dependencies also you can see a random coin toss:<a href="/random_facts">Посмотреть случайный факт!</a>, <a href="/random_cointoss">See the coin toss!</a> '
app.run(debug=True)


@app.route("/random_cointoss")
def random_cointoss():
    random_cointoss = random.choice(cointoss)
    return f'<h2>{random_cointoss}</h2>'
