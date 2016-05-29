#!/usr/bin/env node

'use strict';

var electron = require('electron');
var app = electron.app;
const {BrowserWindow} = require('electron');
var mainWindow = null;

app.on('ready', function() {
    mainWindow = new BrowserWindow({
        height: 600,
        width: 800
    });

    mainWindow.loadURL('http://127.0.0.1:5000/');

    //mainWindow.loadURL('file://' + __dirname + '/app/index.html');
});