// ===== Toaster =====
function showToast(type, message) {
  const container = document.getElementById('toast-container');

  const toast = document.createElement('div');
  toast.classList.add('toast', type);

  // Ícones inline (Lucide style)
  const icon = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  icon.setAttribute('fill', 'none');
  icon.setAttribute('stroke', 'currentColor');
  icon.setAttribute('stroke-width', '2');
  icon.setAttribute('viewBox', '0 0 24 24');

  const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
  if (type === 'success') {
    path.setAttribute('d', 'M5 13l4 4L19 7'); // check
  } else {
    path.setAttribute('d', 'M6 18L18 6M6 6l12 12'); // X
  }
  icon.appendChild(path);

  const text = document.createElement('span');
  text.textContent = message;

  toast.appendChild(icon);
  toast.appendChild(text);
  container.appendChild(toast);

  // Mostrar
  setTimeout(() => toast.classList.add('show'), 100);

  // Remover após 4s
  setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => toast.remove(), 400);
  }, 4000);
}

// ===== Tabs =====
const tabTexto = document.getElementById('tab-texto');
const tabArquivo = document.getElementById('tab-arquivo');
const paneTexto = document.getElementById('pane-texto');
const paneArquivo = document.getElementById('pane-arquivo');

function activateTab(which) {
  if (which === 'texto') {
    tabTexto.classList.add('active');
    tabArquivo.classList.remove('active');
    paneTexto.classList.add('active');
    paneArquivo.classList.remove('active');
  } else {
    tabArquivo.classList.add('active');
    tabTexto.classList.remove('active');
    paneArquivo.classList.add('active');
    paneTexto.classList.remove('active');
  }
}
tabTexto.addEventListener('click', () => activateTab('texto'));
tabArquivo.addEventListener('click', () => activateTab('arquivo'));

// ===== Dropzone =====
const dropzone = document.getElementById('dropzone');
const fileInput = document.getElementById('fileInput');
const fileName = document.getElementById('fileName');
const clearFileBtn = document.getElementById('clearFileBtn');

dropzone.addEventListener('click', () => fileInput.click());
dropzone.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') fileInput.click();
});

['dragenter', 'dragover'].forEach((evt) => {
  dropzone.addEventListener(evt, (e) => {
    e.preventDefault();
    e.stopPropagation();
    dropzone.style.borderColor = '#94a3b8';
  });
});
['dragleave', 'drop'].forEach((evt) => {
  dropzone.addEventListener(evt, (e) => {
    e.preventDefault();
    e.stopPropagation();
    dropzone.style.borderColor = '#cbd5e1';
  });
});

dropzone.addEventListener('drop', (e) => {
  const f = e.dataTransfer.files?.[0];
  if (f) {
    fileInput.files = e.dataTransfer.files;
    fileName.textContent = f.name;
  }
});
fileInput.addEventListener('change', () => {
  const f = fileInput.files?.[0];
  fileName.textContent = f ? f.name : '';
  clearFileBtn.classList.toggle('hidden', !f);
});
clearFileBtn.addEventListener('click', () => {
  fileInput.value = ''; // limpa o input
  fileName.textContent = '';
  clearFileBtn.classList.add('hidden');
});

// ===== Processar =====
const btn = document.getElementById('btnProcess');
const resultCard = document.getElementById('result');
const categoryBadge = document.getElementById('categoryBadge');
const responseText = document.getElementById('responseText');

btn.addEventListener('click', async () => {
  try {
    const text = document.getElementById('emailText').value?.trim();
    const file = fileInput.files?.[0];

    if (!text && !file) {
      showToast('error', 'Informe um texto ou selecione um arquivo .txt/.pdf.');
      return;
    }

    const form = new FormData();
    if (file) form.append('file', file);
    if (text) form.append('email', text);

    btn.classList.add('loading');
    btn.setAttribute('disabled', 'true');

    const res = await fetch('/emails/classify', {
      method: 'POST',
      body: form,
    });

    if (!res.ok) throw new Error('Falha ao processar o e-mail');
    const data = await res.json();

    resultCard.classList.remove('hidden');
    categoryBadge.textContent = data.category || 'Sem categoria';
    categoryBadge.classList.remove('produtivo', 'improdutivo');
    if (data.category?.toLowerCase() === 'produtivo')
      categoryBadge.classList.add('produtivo');
    if (data.category?.toLowerCase() === 'improdutivo')
      categoryBadge.classList.add('improdutivo');

    responseText.textContent = data.response || '(sem resposta sugerida)';

    showToast('success', 'E-mail processado com sucesso!');
  } catch (err) {
    showToast('error', err.message || 'Erro inesperado');
  } finally {
    btn.classList.remove('loading');
    btn.removeAttribute('disabled');
  }
});
