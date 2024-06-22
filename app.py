from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    input_text = request.form['input_text']
    processed_text = input_text.upper()  # Example processing, you can modify this as needed
    return render_template('index.html', processed_text=processed_text)

if __name__ == '__main__':
    app.run(debug=True)
