from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

conversion_rates = {
    'cm': {'m': 0.01, 'km': 0.00001, 'inches': 0.393701, 'feet': 0.0328084},
    'm': {'cm': 100, 'km': 0.001, 'inches': 39.3701, 'feet': 3.28084},
    'km': {'cm': 100000, 'm': 1000, 'inches': 39370.1, 'feet': 3280.84},
    'inches': {'cm': 2.54, 'm': 0.0254, 'km': 0.0000254, 'feet': 0.0833333},
    'feet': {'cm': 30.48, 'm': 0.3048, 'km': 0.0003048, 'inches': 12}
}

@app.route('/convert', methods=['GET'])
def convert():
    value = float(request.args.get('value'))
    from_unit = request.args.get('from_unit')
    to_unit = request.args.get('to_unit')

    if from_unit == to_unit:
        return jsonify({"result": f"No conversion needed. {value} {from_unit} is already the same."})

    if from_unit in conversion_rates and to_unit in conversion_rates[from_unit]:
        conversion_factor = conversion_rates[from_unit][to_unit]
        result = value * conversion_factor
        return jsonify({"result": f"{value} {from_unit} = {result} {to_unit}"})
    
    return jsonify({"error": "Invalid units or conversion not available."})

if __name__ == '__main__':
    app.run(debug=True)
