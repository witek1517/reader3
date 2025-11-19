import os
import json
from flask import Flask, jsonify

app = Flask(__name__)

def get_books():
    books = []
    data_dir = 'reader3_data'
    
    if os.path.exists(data_dir):
        for folder in os.listdir(data_dir):
            folder_path = os.path.join(data_dir, folder)
            if os.path.isdir(folder_path):
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
        book_list = '<br>'.join([b['name'] for b in books])
        return f'<h1>Reader3</h1><p>{book_list}</p>'
    else:
        return '<h1>Reader3 is running!</h1><p>No books found.</p>'

@app.route('/api/books')
def api_books():
    return jsonify({'books': get_books()})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
