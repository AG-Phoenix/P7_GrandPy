const form = document.querySelector("form")
const div = document.querySelector("#responseBlock")
const input = document.querySelector("#mainInput")


form.addEventListener("submit", askPapy)

function askPapy(event){
  event.preventDefault()
  console.log(("askPapy"))
	fetch("./static/tmp/data.json").then(r => r.json()).then(
    r => {
      div.innerHTML += `<p class="question">${input.value}</p>`
      form.reset()
      div.innerHTML += `<p class="repsonse">🤖 ${r.response}</p>`
      input.focus()
    })
}
