from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'cac2024'
app.config['MYSQL_DB'] = 'moto_adictos'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/motos')
def motos():
    return render_template('motos.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/acerca_de')
def acerca_de():
    return render_template('acerca_de.html')

@app.route('/api/comments', methods=['GET'])
def get_comments():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM comments')
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

@app.route('/api/comments', methods=['POST'])
def add_comment():
    data = request.get_json()
    moto = data['moto']
    name = data['name']
    text = data['text']
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO comments (moto, name, text) VALUES (%s, %s, %s)', (moto, name, text))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Comment added successfully'}), 201

@app.route('/api/comments/<int:id>', methods=['PUT'])
def update_comment(id):
    data = request.get_json()
    moto = data['moto']
    name = data['name']
    text = data['text']
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE comments SET moto = %s, name = %s, text = %s WHERE id = %s', (moto, name, text, id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Comment updated successfully'})

@app.route('/api/comments/<int:id>', methods=['DELETE'])
def delete_comment(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM comments WHERE id = %s', [id])
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Comment deleted successfully'})

if __name__ == '__main__':
    app.run(port=3000, debug=True)
