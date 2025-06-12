// vetor com 6 números, sendo 4 pares e 4 ímpares no total
const numeros = [2, 3, 4, 5, 6, 7];

// Contadores
let pares = 0;
let impares = 0;

// verificando quantos pares e impares existem
numeros.forEach(num => { 
    if (num % 2 === 0){ 
        pares++;
    } else { 
        impares++;
    }
  });