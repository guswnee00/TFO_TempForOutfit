from flask import Flask, render_template, request
import numpy as np
import joblib

# 플라스크 클래스명 지정
app = Flask(__name__)

# 모델 불러오기
summer_model = joblib.load(open('/Users/hyunjulee/project/SensibleTemp/data/pkl/s_multiple_ols.pkl', 'rb'))
winter_model = joblib.load(open('/Users/hyunjulee/project/SensibleTemp/data/pkl/w_multiple_ols.pkl', 'rb'))

# 에러 페이지
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# 첫 페이지
@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')


# 여름철 페이지
@app.route('/summer', methods=['GET', 'POST'])
def summer():
    if request.method == 'GET':
        return render_template('summer.html')
    
    if request.method == 'POST':
        try:
            data1 = float(request.form['Temperature'])
            data2 = float(request.form['Humidity'])
            array = np.array([[data1, data2]])
            pred = int(summer_model.predict(array).round(1))

            if pred > 34:
                return render_template('t34.html', pred=pred)
            elif pred > 27:
                return render_template('t27.html', pred=pred)
            elif pred > 22:
                return render_template('t22.html', pred=pred)
            elif pred > 19:
                return render_template('t19.html', pred=pred)
            elif pred > 16:
                return render_template('t16.html', pred=pred)
            elif pred > 11:
                return render_template('t11.html', pred=pred)
            else:
                return render_template('t8.html', pred=pred)
            
        except:
            return render_template('s_again.html')

# 겨울철 페이지
@app.route('/winter', methods=['GET', 'POST'])
def winter():
    if request.method == 'GET':
        return render_template('winter.html')
    
    if request.method == 'POST':
        try:
            data1 = float(request.form['Temperature'])
            data2 = float(request.form['WindSpeed'])
            array = np.array([[data1, data2]])
            pred = int(winter_model.predict(array).round(1))

            if pred > 8:
                return render_template('t7.html', pred=pred)
            elif pred > 4:
                return render_template('t4.html', pred=pred)
            elif pred > -5:
                return render_template('t-5.html', pred=pred)
            else:
                return render_template('t-15.html', pred=pred)
            
        except:
            return render_template('w_again.html')

if __name__ == "__main__":
    app.run(debug=True)