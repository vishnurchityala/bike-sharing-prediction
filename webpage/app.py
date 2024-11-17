from flask import Flask, render_template, request
import pickle
import pandas as pd

# Load models
try:
    with open('./models/poissons_model_regression.pkl', 'rb') as file:
        poisson_model = pickle.load(file)
except Exception as e:
    poisson_model = None
    print(f"Error loading Poisson model: {e}")

try:
    with open('./models/rf_model_regression.pkl', 'rb') as file:
        rf_model = pickle.load(file)
except Exception as e:
    rf_model = None
    print(f"Error loading Random Forest model: {e}")

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
    
    pr_result = "---"
    rf_result = "---"
    
    if request.method == 'POST':
        try:
            # Collect form data
            form_data['weathersit'] = int(request.form.get('weathersit', ''))
            form_data['windspeed'] = float(request.form.get('windspeed', ''))
            form_data['temp'] = float(request.form.get('temp', ''))
            form_data['atemp'] = float(request.form.get('atemp', ''))
            form_data['humidity'] = float(request.form.get('humidity', ''))
            form_data['season'] = request.form.get('season', '')
            form_data['isHoliday'] = 'isHoliday' in request.form
            form_data['isWorkingday'] = 'isWorkingday' in request.form

            # Prepare features for prediction
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

            # Set the season values
            if form_data['season'] == "fall":
                features['season_fall'] = 1
            elif form_data['season'] == "summer":
                features['season_summer'] = 1
            elif form_data['season'] == "winter":
                features['season_winter'] = 1
            elif form_data['season'] == "spring":
                features['season_spring'] = 1

            # Create a DataFrame for prediction
            X_new = pd.DataFrame([features])

            # Prediction logic
            if rf_model:
                rf_predictions = rf_model.predict(X_new)
                rf_result = str(int(rf_predictions[0]))  # Convert prediction to string for display
            else:
                rf_result = "Error: RF model not loaded"

            if poisson_model:
                poisson_predictions = poisson_model.predict(X_new)
                pr_result = str(int(poisson_predictions[0]))  # Convert prediction to string for display
            else:
                pr_result = "Error: Poisson model not loaded"

        except Exception as e:
            print(f"Error processing form data: {e}")
            rf_result = pr_result = "Error processing input data"

    return render_template('index.html', form_data=form_data, pr_result=pr_result, rf_result=rf_result)

if __name__ == '__main__':
    app.run(debug=True)
