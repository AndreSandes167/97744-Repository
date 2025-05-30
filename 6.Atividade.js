console.clear()
function obterNumerosEntre15e20() {
    const numeros = []; 
    for (let i = 15; i <= 20; i++) {
      numeros.push(i); 
    }
    return numeros; 
  }
  const numerosDoIntervalo = obterNumerosEntre15e20();
  console.log("Array de números entre 15 e 20:", numerosDoIntervalo);
