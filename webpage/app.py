from flask import Flask, render_template, request
import pickle
import pandas as pd


with open('./models/poissons_model_regression.pkl', 'rb') as file:
    poisson_model = pickle.load(file)

with open('./models/rf_model_regression.pkl', 'rb') as file:
    rf_model = pickle.load(file)


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form_data = {
        'weathersit': '',
        'windspeed': '',
        'temp': '',
        'atemp': '',
        'humidity': '',
        'season': '',
        'isHoliday': False,
        'isWorkingday': False
    }
    if request.method == 'POST':
        form_data['weathersit'] = float(request.form.get('weathersit', ''))
        form_data['windspeed'] = float(request.form.get('windspeed', ''))
        form_data['temp'] = float(request.form.get('temp', ''))
        form_data['atemp'] = float(request.form.get('atemp', ''))
        form_data['humidity'] = float(request.form.get('humidity', ''))
        form_data['season'] = request.form.get('season', '')
        form_data['isHoliday'] = int('isHoliday' in request.form)
        form_data['isWorkingday'] = int('isWorkingday' in request.form)
        print(form_data)
        features = {
            'holiday': form_data['isHoliday'],
            'workingday': form_data['isWorkingday'],
            'weathersit': form_data['weathersit'],
            'temp': form_data['temp'],
            'atemp': form_data['atemp'],
            'hum': form_data['humidity'],
            'windspeed': form_data['windspeed'],
            'season_fall': 0,
            'season_spring': 0,
            'season_summer': 0,
            'season_winter': 0
        }
        if form_data['season'] ==  "fall":
            features['season_fall'] = 1
        elif form_data['season'] ==  "summer":
            features['season_summer'] = 1
        elif form_data['season'] ==  "winter":
            features['season_winter'] = 1
        elif form_data['season'] == "spring":
            features['season_spring'] = 1

        X_new = pd.DataFrame([features])
        rf_predictions = rf_model.predict(X_new)
        poisson_predictions = poisson_model.predict(X_new)
        pr_result = str(int(poisson_predictions[0]))
        rf_result = str(int(rf_predictions[0]))
    else:
        pr_result = "---"
        rf_result = "---"

    return render_template('index.html', form_data=form_data, pr_result=pr_result, rf_result=rf_result)

if __name__ == '__main__':
    app.run(debug=True)
