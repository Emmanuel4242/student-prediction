from flask import Flask, request, render_template

class Library:
    def __init__(self):
        self.book = []
        self.borrowed = []

    def add_book(self,title):
        self.book.append(title)

    def borrow_book(self,title):
        if title in self.book:
            self.book.remove(title)
            self.borrowed.append(title)

app = Flask(__name__)
library = Library()

@app.route("/", methods = ['POST','GET'])
def home():
    if request.method == 'POST':
        title = request.form['title']
        action = request.form['action']

        if action == "add":
            library.add_book(title)
        elif action == "borrow":
            library.borrow_book(title)

    return render_template('index.html', books=library.book, borrowed=library.borrowed)

app.run(debug=True)
        

