#!/usr/bin/node
const req = require('request');
const id = process.argv[2];

const filmAsync = function (id) {
  return new Promise(
    function (resolve, reject) {
      req('https://swapi-api.alx-tools.com/api/films/' + id,
        function (err, resp, body) {
          if (!err) {
            resolve(JSON.parse(body));
          }
        });
    }
  );
};
const charAsync = function (url) {
  return new Promise(
    function (resolve, reject) {
      req(url,
        function (err, resp, body) {
          if (!err) {
            resolve(JSON.parse(body));
          }
        });
    }
  );
};
async function getAllCharacters (id) {
  try {
    const movie = await filmAsync(id);
    const characters = await movie.characters;
    for (const character of characters) {
      const char = await charAsync(character);
      console.log(char.name);
    }
  } catch {

  }
}
getAllCharacters(id);
