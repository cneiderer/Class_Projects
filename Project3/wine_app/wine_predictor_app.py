import flask
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import pickle

#---------- MODEL IN MEMORY ----------------#

# Load pickled model
#PREDICTOR = pickle.load(open('svm_model.pkl', 'rb'))
PREDICTOR = pickle.load(open('logistic_model.pkl', 'rb'))

#---------- URLS AND WEB PAGES -------------#

# Initialize the app
app = flask.Flask(__name__)

# Homepage
@app.route("/")
def viz_page():
    """
    Homepage: serve our visualization page, awesome.html
    """
    with open("awesome.html", 'r') as viz_file:
        return viz_file.read()

# Get an example and return it's score from the predictor model
@app.route("/score", methods=["POST"])
def score():
    """
    When A POST request with json data is made to this uri,
    Read the example from the json, predict probability and
    send it with a response
    """
    # Get decision score for our example that came with the request
    data = flask.request.json
    x = np.matrix(data["example"])
    score = PREDICTOR.predict_proba(x)
    # Put the result in a nice dict so we can send it as json

    results = {"score1": score[0, 0],
               "score2": score[0, 1],
               "score3": score[0, 2]}
    print(results)
    return flask.jsonify(results)

#--------- RUN WEB APP SERVER ------------#

# Start the app server on port 80
# (The default website port)
app.run(host='0.0.0.0')
app.run(debug=True)
