document.getElementById('startButton').addEventListener('click', function() {
    fetch('/start-api', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        alert('API iniciada!');
    })
    .catch(error => {
        console.error('Erro ao iniciar a API:', error);
        alert('|Falha na API.');
    });
});