let vetor = [10, -5, 7, -2, 3];

// contador de negativos e soma de positivos
let negativos = 0;
let somaPositivos = 0;

// Loop para verificar cada número
for (let i = 0; i < vetor.length; i++) { 
    if (vetor[i] < 0){ 
      negativos++;
    } else { 
        somaPositivos += vetor[i];
    }
  }

  // Exibição dos resultados
  console.log("Quantidade de números negativos:", negativos);
  console.log("soma dos números positivos:", somaPositivos);
