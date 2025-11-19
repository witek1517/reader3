from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    # Wczytaj listę przetworzonych książek
    books = []
    if os.path.exists('reader3_data'):
        for folder in os.listdir('reader3_data'):
            book_path = os.path.join('reader3_data', folder)
            if os.path.isdir(book_path):
                books.append(folder)
    
    return render_template('index.html', books=books)

@app.route('/api/books')
def get_books():
    books = []
    if os.path.exists('reader3_data'):
        for folder in os.listdir('reader3_data'):
            if os.path.isdir(os.path.join('reader3_data', folder)):
                books.append(folder)
    return jsonify({'books': books})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8123))
    app.run(host='0.0.0.0', port=port, debug=False)
