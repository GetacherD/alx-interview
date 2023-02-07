#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
req('https://swapi-api.alx-tools.com/api/films/' + String(id),
  function (err, resp, body) {
    if (!err) {
      const bdy = JSON.parse(body);
      const chars = bdy.characters;
      if (chars) {
        for (const chr of chars) {
          req(chr, function (err, resp, body) {
            if (!err) {
              console.log(JSON.parse(body).name);
            }
          });
        }
      }
    }
  }
);
