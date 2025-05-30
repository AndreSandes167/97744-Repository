console.clear()
const readline = require('readline-sync')
const A = readline.questionInt('Digite um numero: ')
const B = readline.questionInt('Digite um numero: ')
if (A == B) {
    resultado = (A + B)
} else {
    resultado = (A * B)
}

C = resultado

console.log(C)