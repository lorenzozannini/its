function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function myparseInt(n) {
    for (let i = 0; i < n.length; i++) {
        if (isNaN(n.charAt(i)) == true) {
            console.log("Errore al carattere " + (i + 1) + " tentativi rimasti 2")
            const n = prompt("Retry enter number ->");
            for (let i = 0; i < n.length; i++) {
                if (isNaN(n.charAt(i)) == true) {
                    console.log("Errore al carattere " + (i + 1) + " tentativi rimasti 1")
                    const n = prompt("Retry enter number ->");
                    for (let i = 0; i < n.length; i++) {
                        if (isNaN(n.charAt(i)) == true) {
                            console.log("Errore al carattere " + (i + 1) + " tentativi esauriti")
                            process.exit(0);
                        }
                    }
                    return parseInt(n)
                }
            }
            return parseInt(n)
        }
    }
    return parseInt(n)
}

const prompt = require("prompt-sync")();

/*
var str = prompt("Enter a string ->");
console.log("Hai inserito "+str);
str = capitalizeFirstLetter(str);
console.log("Prima lettera maiuscola "+str);
*/

const n1 = myparseInt(prompt("Enter first number ->"));
const n2 = myparseInt(prompt("Enter second number ->"));
console.log("La somma dei numeri inseriti è " + (n1 + n2));