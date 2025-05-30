console.clear()
const readline = require('readline-sync')
const numero = readline.questionInt('Digite um numero: ')

if (numero == 1) {
    console.log('Domingo')
    console.log('Final de semana')
} else if (numero == 2) {
    console.log('Segunda')
    console.log('DIa Util')
} else if (numero == 3) {
    console.log('Terça')
    console.log('DIa Util')
} else if (numero == 4) {
    console.log('Quarta')
    console.log('DIa Util')
} else if (numero == 5) {
    console.log('Quinta')
    console.log('DIa Util')
} else if (numero == 6) {
    console.log('Sexta')
    console.log('DIa Util')
} else if (numero == 7) {
    console.log('Sabado')
    console.log('Final de semana')
} else {
    console.log('Dia invalido')
}
// 5 mim 25 segs
