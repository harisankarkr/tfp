// designer login validation
// -------------------------------------------------------------------------------------

const desigID = document.getElementById('DesigEmail')
const desigPswd = document.getElementById('DesigPswd')
const form = document.getElementById('DesigLogForm')
const errorElement = document.getElementById('errMsg')

form.addEventListener('submit', e => {
    let messages = []
    if (desigID.value === '' || desigID.value == null){
        messages.push("inncorrect Designer ID")
        console.log('hihi')
    }

    if (messages.length > 0) {
        e.preventDefault()
        errorElement.innerText = messages.join(',')
    }
})
// -------------------------------------------------------------------------------------