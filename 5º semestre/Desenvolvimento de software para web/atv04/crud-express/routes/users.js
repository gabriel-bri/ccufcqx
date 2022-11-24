var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.json(
    {
      users: [
        {name: 'Timmy'},
        {name: 'Billy'}
      ]
    });
});

module.exports = router;
