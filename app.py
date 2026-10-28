from flask import Flask
from modules import home, cake, memories, letter, hug, gifts, finale, memory_detail, paris

app = Flask(__name__)
for module in (home, cake, memories, letter, hug, gifts, finale, memory_detail, paris):
    app.register_blueprint(module.bp)

@app.get('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(debug=True)
