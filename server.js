const express = require('express')
const app = express()
const path = require('path');
const router = express.Router();

app.set('view engine', 'html')

app.use('/', router);

router.get('/',function(req,res){
  res.sendFile(path.join(__dirname+'/index2.html'));
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})