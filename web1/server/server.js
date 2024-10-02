/*npm install --save-dev express cors*/
/*Per evitare di riavviare: npm i nodemon 
							npx nodemon --exec node server.js*/

                            const express = require('express');
                            const cors = require('cors')
                            const app = express();
                            
                            app.use(cors());
                            
                            var iPortaTcp = 4201;
                            var sIpAddress = "127.0.0.1"
                            
                            app.listen(iPortaTcp,sIpAddress, () => console.log('API is running on http://' + sIpAddress + ':' + iPortaTcp));
                            
app.use('/paperino', (req, res) => {
console.log("Mi hai chiesto di salutarti");
res.send("<html>Buonanotte al secchio</html>");
});


app.use('/topolino', (req, res) => {
console.log("Mi hai chiesto di salutarti");
res.send("<html>Buona serata a tutti</html>");
});
