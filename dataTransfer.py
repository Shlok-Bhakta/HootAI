from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/teacher', methods=['GET', 'POST'])
def teacher():
    if request.method == 'POST':
        question = request.form.get('questionInput')
        blue_button = request.form.get('bluebutton')
        green_button = request.form.get('greenbutton')
        red_button = request.form.get('redbutton')
        orange_button = request.form.get('orangebutton')
        return render_template('Student.html', question=question, blue_button=blue_button, green_button=green_button, red_button=red_button, orange_button=orange_button)
    return render_template('Teacher.html')

if __name__ == '__main__':
    app.run(debug=True)






