import pandas as pd
import re
from allennlp.predictors.predictor import Predictor
import allennlp_models.rc
from flask import Flask, render_template, request
app = Flask(__name__)


predictor_20 = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/bidaf-elmo-model-2020.03.19.tar.gz")


#predictor_18 = Predictor.from_path('bidaf-elmo-model-2018.11.30-charpad.tar.gz')
#predictor_17 = Predictor.from_path('bidaf-model-2017.09.15-charpad-allennlpv1.0.tar.gz')

f = open('corona_new.txt','r')
text = f.read()
text = re.sub('\n','',text)
text = text.lower()

@app.route('/')
def index():
    return render_template('index_2.html')


@app.route('/QA_page')
def QA_page():
    return render_template('index.html')

@app.route('/main_page')
def main_page():
    question = request.args.get('topic')
    #question = request.args.get('question')
    answer = qna(text, question)
    return render_template('index.html', answer = answer)

def qna(text, question):
    context = text
    result_20 = predictor_20.predict(passage = context, question = question)
    #result_17 = predictor_17.predict(passage = context, question = question)

    #if len(result_18) >= len(result_18):
     #   return result_18['best_span_str']
    #else:
     #   return result_17['best_span_str']
    return result_20['best_span_str']



    

if __name__ == '__main__':
    app.run(debug=True)
#app.run(host = '10.26.34.190', port = 9100, debug = True)