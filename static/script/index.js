var input_a = document.getElementById("a_valor");
var input_b = document.getElementById("b_valor");
var input_n = document.getElementById("n_valor");
var input_fx = document.getElementById("fx_valor");
var resultado = document.getElementById("resultado");
function Obtener_datos() {
    var a_valor = parseInt(input_a.value);
    var b_valor = parseInt(input_b.value);
    var n_valor = parseInt(input_n.value);
    var fx_valor = input_fx.value;
    var datos = {
        valor_a: a_valor,
        valor_b: b_valor,
        valor_n: n_valor,
        valor_fx: fx_valor
    };
    fetch('/proceso', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(datos)
    })
        .then(function (response) { return response.json(); })
        .then(function (datos) {
        Presentar_respuesta(datos.result);
    })
        .catch(function (error) { return console.error('Error', error); });
}
function Presentar_respuesta(respuesta) {
    resultado.innerText = respuesta;
}
