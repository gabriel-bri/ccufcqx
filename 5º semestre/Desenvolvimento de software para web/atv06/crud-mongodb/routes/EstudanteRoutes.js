var express = require('express');
var router = express.Router();
var EstudanteServices = require('../services/EstudanteServices');

router.get('/list', function(req, res, next) {
    EstudanteServices.list(req,res);
});

router.post('/register', function(req, res, next){
    EstudanteServices.register(req,res);
});

router.put('/update/:id', function(req, res, next){
    EstudanteServices.update(req,res);
});

router.delete('/delete/:id', function(req, res, next){
    EstudanteServices.delete(req,res);
});

router.get('/retrieve/:id', function(req, res, next){
    EstudanteServices.retrieve(req,res);
});

router.get('/retrieve/login/:login', function(req, res, next){
    EstudanteServices.retrieveByLogin(req,res);
});

module.exports = router;