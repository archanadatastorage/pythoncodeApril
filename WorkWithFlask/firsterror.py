from flask import Flask,render_template,abort

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/')
def index():
    return render_template('index1.html')

'''@app.route('/messages/<int:idx>')
def message(idx):
    messages = ['Message Zero', 'Message One', 'Message Two']
    try:
        return render_template('message.html', message=messages[idx])
    except IndexError:
        abort(404)'''
@app.route('/messages/<int:idx>')
def message(idx):
    app.logger.info('Building the messages list...')
    messages = ['Message Zero', 'Message One', 'Message Two']
    try:
        app.logger.debug('Get message with index: {}'.format(idx))
        return render_template('message.html', message=messages[idx])
    except IndexError:
        app.logger.error('Index {} is causing an IndexError'.format(idx))
        abort(404)