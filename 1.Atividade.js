const readline = require('readline-sync')
const idade = readline.questionInt('Digite sua idade: ')

if (idade >= 65) {
    console.log('Nao e obrigado a votar. ')
} else if (idade >= 18) {
    console.log('Voto obrigatorio. ')
} else if (idade >= 16) {
    console.log('Voto Opicional. ')
} else if (idade < 16) {
    console.log('Nao pode Votar. ')
} else {
    console.log('Nada encontrado.')
}