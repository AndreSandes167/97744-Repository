// Instalar; npm install readline-sync

const readline = require('readline-sync')

const idade = readline.questionInt('Digite sua idade: ')

if (idade < 18) {
    console.log('Menor idade: ')
}  else {
    console.log('MAior idade: ')
}