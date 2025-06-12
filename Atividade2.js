let numero = parseInt(prompt("Digite um número para a contagem regressiva:"));

function contagemRegressiva(n) {
  for (let i = n; i >= 1; i--) {
    setTimeout(() => {
      console.log(i);
    }, (n - i) * 1000);
  }
}

if (!isNaN(numero) && numero > 0) {
  contagemRegressiva(numero);
} else {
  alert("Por favor, digite um número válido maior que zero.");
}
