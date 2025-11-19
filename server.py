import os
import json
from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='templates', static_folder='static')

def get_books():
    """Szuka przetworzonych książek w reader3_data"""
    books = []
    data_dir = 'reader3_data'
    
    if os.path.exists(data_dir):
        for folder in os.listdir(data_dir):
            folder_path = os.path.join(data_dir, folder)
            if os.path.isdir(folder_path):
                # Sprawdź czy istnieje plik book.pkl
                pkl_file = os.path.join(folder_path, 'book.pkl')
                if os.path.exists(pkl_file):
                    books.append({
                        'name': folder,
                        'path': folder_path
                    })
    return books

@app.route('/')
def index():
    books = get_books()
    if books:
        return f'<h1>Reader3</h1><ul>{"".join([f"<li>{b[\"name\"]}</li>" for b in books])}</ul>'
    else:
        return '<h1>Reader3 is running!</h1><p>No books found. Process an EPUB first.</p>'

@app.route('/api/books')
def api_books():
    return jsonify({'books': get_books()})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
