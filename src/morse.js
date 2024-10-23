const fs = require('fs');
const csv = require('csv-parser');

// Definimos las estructuras de Datos
class Morse {
    constructor(clave, morse, palabra_clave, code) {
        this.clave = clave;
        this.morse = morse;
        this.palabra_clave = palabra_clave;
        this.code = code;
    }
}

function leerFichero(fichero){
    let morse = [];
    fs.createReadStream(fichero)
    .pipe(csv())
    .on('data', (fila) => {
        morse.push(new Morse(fila.clave, fila.morse, fila.palabra_clave, fila.code));
    })
    .on('end', () => {
        console.log('CSV file successfully processed');
    });
    return morse;
}

(async () => { 
    try {
        const lista = await leerFichero('./data/abecedario.csv')
        console.log(lista);
    } catch (error){
        console.error('Error', error)
    }
});