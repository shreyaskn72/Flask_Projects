from flask import *
from flask import request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template('index_task1.html')

if __name__ == '__main__':
    app.run(debug=True)
