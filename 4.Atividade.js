console.clear()
const readline = require('readline-sync')
const numero = readline.questionInt('Digite um numero: ')

if (numero % 2 === 0) {
    console.log('par')
} else {
    console.log('impar')
}