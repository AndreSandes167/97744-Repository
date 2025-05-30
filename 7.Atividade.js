console.clear()
const readline = require('readline-sync')
const numero = readline.questionInt('Digite um numero: ')

if (numero >= 0) {
    console.log('Positivo')
} else {
    console.log('Negativo')
}