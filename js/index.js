const polka = require('polka');

function handler(req, res) {
    res.end('Hello world!');
}

polka()
    .get('/', handler)
    .listen(8080, err => {
        if (err) throw err;
        console.log(`> Running on 127.0.0.1:8080`);
    });
