# WHY = separate the python code from the HTML code and make it scalable! 
# 1. utilize route variables to get data from the URL

# standard flask boilerplate

# import the Flask server object
from flask import Flask, request, render_template
import json, requests

# create new Flask instance and assign it a root directory of the 
# working file (should be named 'main.py')
app = Flask(__name__)

#create some routes
@app.route('/')
def displayHomepage():
    return render_template('homepage.html')

# @app.route('/formExample')
# def firstForm():
#     return render_template('form.html')

@app.route('/results', methods=['GET'])
def sw_character_results():
    character_id = request.args.get("id")

    swapi_url = f'https://swapi.py4e.com/api/people/{character_id}'
    response = requests.get(swapi_url)
    character_data = response.json()

    context = {
        'name': character_data.get('name'),
        'height': character_data.get('height'),
        'mass': character_data.get('mass'),
        'hair_color': character_data.get('hair_color'),
        'eye_color': character_data.get('eye_color')
    }
    
    return render_template('display_character.html', **context)

# @app.route('/compliments')
# def compliments():
#     compliments = [
#         'brave',
#         'witty',
#         'tenacious'
#     ]

#     context = {
#         'compliments': compliments
#     }

#     return render_template('compliments.html', **context)

# with open('exampleObj.json') as example_obj_file:
#     print("raw file printed = ", example_obj_file)
#     jsonData = json.load(example_obj_file)
#     print("just the json data printed = ", jsonData)

# @app.route("/jsonExample", methods=['GET'])
# def jsonRoute():
#     return jsonData

# the server can be accessed in your web browser using the URL localhost:3000/
if __name__ == '__main__':
    app.run(debug=True, port=3000)