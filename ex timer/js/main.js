const relogio = document.querySelector('.relogio')
const iniciar = document.querySelector('.iniciar')
const pausar = document.querySelector('.pausar')
const zerar = document.querySelector('.zerar')
let segundos = 0;
let timer;

function criahora (segundos) {
    const data = new Date(segundos * 1000)
    return data.toLocaleTimeString('pt-BR', {
        hour12: false,
        timeZone: 'UTC'
    })
}

function iniciarelogio () {
     timer = setInterval(function() {
        segundos++
        relogio.innerHTML = criahora(segundos)
    }, 1000)
}


iniciar.addEventListener('click', function(evento) {
    clearInterval(timer)
    iniciarelogio()
})

pausar.addEventListener('click', function(evento) {
    clearInterval(timer)
})

zerar.addEventListener('click', function(evento) {
    clearInterval(timer)
    relogio.innerHTML = '00:00:00'
    segundos = 0
})