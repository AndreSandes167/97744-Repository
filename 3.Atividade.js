console.clear()
const readline = require('readline-sync')
const A = readline.questionInt('Digite um numero: ')
const B = readline.questionInt('Digite um numero: ')
const C = readline.questionInt('Digite um numero: ')

if (A + B < C) {
    console.log('A soma de A + B e menor que C')
} else {
    console.log('A soma de A + B e maior que C')
}
