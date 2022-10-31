from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = request.args.get('name')
    return render_template('new.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)