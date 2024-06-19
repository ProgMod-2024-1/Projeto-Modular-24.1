function sendData() {
    const url = 'add_filial';  // Flask route URL
    const name = document.getElementById('nomeFilialNova').value;
    const address = document.getElementById('enderecoFilialNova').value;
    const cep = document.getElementById('cepFilialNova').value;
    const nAlunos = document.getElementById('numeroDeAlunosFilialNova').value;
    const myButton = document.getElementById('createModal');
    myButton.disabled = true;
    const data = {
        name: name,
        address: address,
        cep: cep,
        nAlunos: nAlunos
    };

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Response from Flask:', data.message);
        myButton.disabled = false;
    })
    .catch(error => {
        console.error('Error sending data:', error);
        myButton.disabled = false;
    })
    .finally(()=>{
        location.reload()
    });    
}
