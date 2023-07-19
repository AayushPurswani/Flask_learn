from flask import Flask, render_template
app =Flask(__name__)

posts =[
{
    'Author' : 'George R. R. Martin',
    'Book' : 'A song of Fire and Ice',
    'Content' : 'Its a good book',
    'Age' : 'Almost dead'
},
{
    'Author' : 'Tolkein',
    'Book' : 'Lord of the Rings',
    'Content' : 'Its a great book',
    'Age' : 'Dead'
},


]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def hi():
    return render_template("about.html", posts = posts, title = 'Authors')

if __name__ == '__main__':
    app.run(debug=True)
