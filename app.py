from flask import Flask, json, request

app = Flask(__name__)

@app.route('/recipes', methods = ['GET'])
def recipes():
    f = open('data.json')
    data = json.load(f)
    f.close()
    return data['recipes'], 200

@app.route('/recipes/details/<recipe_name>', methods = ['GET'])
def details(recipe_name):
    f = open('data.json')
    data = json.load(f)

    for i in data['recipes']:
        if i['name'] == recipe_name:
            data = i['ingredients']

    f.close()
    return data, 200

@app.route('/recipes', methods = ['POST'])
def add_recipe():
    new_recipe = request.get_json()

    f = open('data.json')
    data = json.load(f)

    for i in data['recipes']:
        if i['name'] == new_recipe['name']:
            return 'Error: recipe already exists', 400

    data.update(new_recipe)
    f.close()

    return '', 200

@app.route('/recipes', methods = ['PUT'])
def edit_recipe():
    edit_recipe = request.get_json()
    f = open('data.json')
    data = json.load(f)

    for i in data['recipes']:
        if i['name'] == edit_recipe['name']:
            # make the update happen
            for key, val in data.items():
                edit_recipe[key] = val
            return "", 204

    f.close()
    return 'Error: recipe does not exist', 400