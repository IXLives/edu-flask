from flask import Flask, render_template, abort

app = Flask(__name__)

pets = [
    {"id": 1, "name": "Stuie", "age": "5 weeks",
        "bio": "I am a tiny kitten rescued by the good people at Kitten Bizness. I love squeaky toys and cuddles."},
    {"id": 2, "name": "Karev", "age": "8 months",
     "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
    {"id": 3, "name": "Bruce", "age": "1 year",
     "bio": "I love barking. But, I love my friends more."},
    {"id": 4, "name": "Wayne", "age": "5 years", "bio": "Probably napping."},
]


@app.route('/')
def home():
    return render_template('home.html', pets=pets)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/details/<int:pet_id>')
def details(pet_id):
    pet = next((pet for pet in pets if pet['id'] == pet_id), None)
    if pet is None:
        abort(404, description='No Pet was Found with the given ID')
    return render_template('details.html', pet=pet)


if __name__ == '__main__':
    app.run(debug=True)
