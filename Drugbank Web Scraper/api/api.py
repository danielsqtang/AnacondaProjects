from flask import Flask, request
import pandas as pd
import numpy as np

app = Flask(__name__)
app.config["DEBUG"] = True

drug_target = pd.read_csv('../drug_target.csv')

@app.route('/', methods=['POST', 'GET'])
def home():
    return "DrugBank WebScraper Project"


@app.route('/drugs', methods=['POST', 'GET'])
def drug_target_lookup():
    data = request.args.get('accession_number')
    result = []
    try:
        df = drug_target.loc[drug_target['accession_number'] == data]
        for target_name in df.target_name:
            result.append(target_name)
        return ', '.join([str(elem) for elem in result]) 
    except:
        return data + ' is not a valid accession_number'
        

if __name__ == '__main__':
    app.run()