from bottle import route, run

@route('/hello')
def hello():
    return "Hello World!"

run(host='192.168.1.10', port=8080, debug=True)