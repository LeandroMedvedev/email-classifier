document
  .getElementById('emailForm')
  .addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = new FormData();
    const file = document.getElementById('file').files[0];
    const text = document.getElementById('text').value;

    if (file) {
      formData.append('file', file);
    } else if (text.trim() !== '') {
      formData.append('text', text);
    } else {
      alert('Por favor, insira um texto ou faça upload de um arquivo.');
      return;
    }

    const response = await fetch('/emails/classify', {
      method: 'POST',
      body: formData,
    });

    const data = await response.json();

    document.getElementById('category').innerText = data.category;
    document.getElementById('response').innerText = data.response;

    document.getElementById('result').classList.remove('hidden');
  });
