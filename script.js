function gerarTabuada() { 
const numeroInput = document.getElementById('numeroInput')
let numero= parseInt(numeroInput.value)


//constltadoDiv =documentgetElementById('resultadoTabuada')
resultadoDiv = ''


resultadoDiv.innerHTML += <h2>Tabuada do $(numero)</h2>
10
for (let i=1; <= 10; i++) { 
    let rersultado = numero * i
    resultadoDiv.innerHTML += <p>${numero} x ${i} = ${resultado}</p>
 }

 