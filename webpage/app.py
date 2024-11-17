from flask import Flask, render_template, request

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
        form_data['weathersit'] = request.form.get('weathersit', '')
        form_data['windspeed'] = request.form.get('windspeed', '')
        form_data['temp'] = request.form.get('temp', '')
        form_data['atemp'] = request.form.get('atemp', '')
        form_data['humidity'] = request.form.get('humidity', '')
        form_data['season'] = request.form.get('season', '')
        form_data['isHoliday'] = 'isHoliday' in request.form
        form_data['isWorkingday'] = 'isWorkingday' in request.form

        pr_result = "---"
        rf_result = "---"
    else:
        pr_result = "---"
        rf_result = "---"

    return render_template('index.html', form_data=form_data, pr_result=pr_result, rf_result=rf_result)

if __name__ == '__main__':
    app.run(debug=True)
