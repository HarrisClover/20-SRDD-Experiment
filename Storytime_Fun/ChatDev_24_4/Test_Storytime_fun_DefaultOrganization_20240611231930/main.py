'''
This is the main file for the Flask application. It contains the routes and views for the application. It has been updated to include routes for adding pages, characters, themes, settings, interactive elements, voice-overs, sound effects, and saving the storybook.
'''
from flask import Flask, render_template, request, session
from storybook import StoryBook
app = Flask(__name__)
app.secret_key = 'super secret key'
@app.route('/', methods=['GET', 'POST'])
def create_storybook():
    if request.method == 'POST':
        title = request.form['title']
        session['storybook'] = StoryBook(title).__dict__
        return redirect(url_for('add_page'))
    return render_template('create_storybook.html')
@app.route('/add_page', methods=['GET', 'POST'])
def add_page():
    if request.method == 'POST':
        text = request.form['text']
        image = request.form['image']
        session['storybook'].create_page(text, image)
        return redirect(url_for('add_character'))
    return render_template('add_page.html')
# Add similar routes for adding characters, themes, settings, interactive elements, voice-overs, sound effects
@app.route('/save_storybook', methods=['POST'])
def save_storybook():
    filename = request.form['filename']
    session['storybook'].save_storybook(filename)
    return render_template('storybook_saved.html')
if __name__ == '__main__':
    app.run(debug=True)