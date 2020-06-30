from flask import Flask,redirect, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = request.form
        email = form['email']
        password = form['password']
        print(email, password)
        if email == 'bua0409@gmail.com' and password == '123':
            return redirect('/survey')
        else:
            print('login failed')
            return render_template('login.html')    
@app.route('/sport')
def web_sport():
    return ' =))))'

@app.route('/redirect')
def go_to_google():
    return redirect('https://www.google.com/')

@app.route('/say-hi/<string:name>')
def say_hi(name):    
    return 'hello {}'.format(name)

@app.route('/add-number/<int:number_1>/<int:number_2>')
def get_sum(number_1, number_2):
    total = number_2 + number_1
    return 'the sum is {}'.format(str(total))    

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'GET':
        return render_template('survey.html')
    elif request.method == 'POST':
        form = request.form
        answer_1 = form['question_1']
        answer_2 = form['question_2']
        print(answer_1, answer_2)    
        return 'thank you'

if __name__ == '__main__':
    app.run()    

