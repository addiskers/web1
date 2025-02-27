from flask import Flask, render_template

app = Flask(__name__)

# Define routes
@app.route('/')
@app.route('/index.html') 
def index():
    return render_template('index.html')

@app.route('/about-us.html')
def about_us():
    return render_template('about-us.html')

@app.route('/loans.html')
def loans():
    return render_template('loans.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/news.html')
def news():
    return render_template('news.html')

@app.route('/elements.html')
def elements():
    return render_template('elements.html')

if __name__ == '__main__':
    app.run(debug=True)
