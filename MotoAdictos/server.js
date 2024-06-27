const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const mysql = require('mysql2');
const path = require('path');

const app = express();
const port = 3000;

app.use(cors());
app.use(bodyParser.json());

// Servir archivos estáticos desde la carpeta "templates"
app.use(express.static(path.join(__dirname, 'templates')));

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'cac2024',
    database: 'moto_adictos'
});

db.connect(err => {
    if (err) throw err;
    console.log('Connected to database');
});

app.get('/api/comments', (req, res) => {
    db.query('SELECT * FROM comments', (err, results) => {
        if (err) throw err;
        res.send(results);
    });
});

app.post('/api/comments', (req, res) => {
    const { moto, name, text } = req.body;
    db.query('INSERT INTO comments (moto, name, text) VALUES (?, ?, ?)', [moto, name, text], (err, result) => {
        if (err) throw err;
        res.send(result);
    });
});

app.put('/api/comments/:id', (req, res) => {
    const { id } = req.params;
    const { moto, name, text } = req.body;
    db.query('UPDATE comments SET moto = ?, name = ?, text = ? WHERE id = ?', [moto, name, text, id], (err, result) => {
        if (err) throw err;
        res.send(result);
    });
});

app.delete('/api/comments/:id', (req, res) => {
    const { id } = req.params;
    db.query('DELETE FROM comments WHERE id = ?', [id], (err, result) => {
        if (err) throw err;
        res.send(result);
    });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
