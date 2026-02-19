function contarAteDez () {
    for (let i = 0; i <= 10; i++) {
        console.log(i)
    }
}

function reverterTexto (texto) {
    return texto.split("").reverse().join("")
}

function dobro (numero) {
    return numero * 2
}

function contarVogais (texto) {

    // match serve para criar um array "secundario" com determinados caracteres que 
    // com condições podem ser usados de devidas maneiras
    const vogais = texto.match(/[aeiouáéíóúãõàèìòùâêîôû]/gi) 

    if (vogais ) {
        return `${texto} tem essas vogais: ${vogais.join(", ")}`
    }else {
        return `${texto} não possui vogais`
    }
}

function contarPares () {

    const numeros = [1, 2, 3, 4]

    for (let i = numeros; numeros % 2 === 0; numeros + numeros) {
        return (console.log(numeros))
    }
}