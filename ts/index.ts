const input_a = <HTMLInputElement>document.getElementById("a_valor");
const input_b = <HTMLInputElement>document.getElementById("b_valor");
const input_n = <HTMLInputElement>document.getElementById("n_valor");
const input_fx = <HTMLInputElement>document.getElementById("fx_valor");
const resultado = <HTMLInputElement>document.getElementById("resultado");

function Obtener_datos(){
  var a_valor: number = parseInt(input_a.value)
  var b_valor: number = parseInt(input_b.value)
  var n_valor: number = parseInt(input_n.value)
  var fx_valor: string = input_fx.value

  var datos = {
    valor_a: a_valor,
    valor_b: b_valor,
    valor_n: n_valor,
    valor_fx: fx_valor
  }

  fetch('/proceso',{
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(datos)
  })
    .then(response => response.json())
    .then(datos => {
      Presentar_respuesta(datos.result);
    })
    .catch(error => console.error('Error', error))

}

function Presentar_respuesta(respuesta){
  resultado.innerText = respuesta;
}
