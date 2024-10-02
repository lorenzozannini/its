const express = require('express');
const cors = require('cors')
const app = express();

app.use(cors());

var iPortaTcp = 4201;
var sIpAddress = "127.0.0.1"

app.listen(iPortaTcp,sIpAddress, () => console.log('API is running on http://' + sIpAddress + ':' + iPortaTcp));
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));

//PRIMA ROUTE
app.get('', (req, res) => {
    console.log("Mi hai chiesto la pagina iniziale");
    res.sendFile("index.html", { root: './htdocs' });
    });

//SECONDA ROUTE
app.get('/registrati.html', (req, res) => {
    console.log("Mi hai chiesto la pagina di registrazione");
    res.sendFile("/registrati.html", { root: './htdocs' });
    });

//TERZA ROUTE
app.get('/accedi.html', (req, res) => {
    console.log("Mi hai chiesto la pagina di accesso");
    res.sendFile("/accedi.html", { root: './htdocs' });
    });

//FORM ROUTE
app.get('/gestisciDatiForm', (req, res) => {
    console.log("Mi hai chiesto la pagina della form");
    res.send("<html><body>Ciao "+ req.query.vNome +"</body></html>");
    });