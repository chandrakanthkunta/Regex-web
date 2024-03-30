from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test_regex', methods=['POST'])
def test_regex():
    regex_pattern = request.form['regex_pattern']
    test_string = request.form['test_string']
    matched = re.findall(regex_pattern, test_string)
    return render_template('index.html', matched=matched)
    if matched:
        result = "matched"
    else:
        result = "not matched"
    return render_template('index.html',matched=matched)


@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    regex_pattern = r'^[A-Za-z0-9._]+@[A-Za-z0-9.]+\.[A-z]{2,3}$'
    is_valid = re.match(regex_pattern, email)
    if is_valid:
        result =  email," is Valid Email"
    else:
        result = email , " is Invalid Email"
    return render_template('index.html', email_result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
