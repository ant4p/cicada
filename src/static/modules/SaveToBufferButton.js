document.getElementById('copyButton').addEventListener("click", (event) => {
    // Останавливаем всплытие и переход по ссылке
    event.preventDefault();
    event.stopPropagation();

    // Получаем текст email из родительской ссылки
    const emailLink = event.currentTarget.closest('a.contacts__contact.is-mail');
    if (!emailLink) {
      alert("Не удалось найти email для копирования");
      return;
    }
    // Текст email - это текст внутри ссылки без кнопки
    // Можно взять innerText и убрать текст кнопки, либо взять email из href
    // Лучше взять из href, чтобы не зависеть от разметки
    const href = emailLink.getAttribute('href'); // mailto:email@example.com
    if (!href || !href.startsWith('mailto:')) {
      alert("Некорректный email");
      return;
    }
    const email = href.replace('mailto:', '');

    navigator.clipboard.writeText(email)
      .then(() => {
        alert("Email скопирован: " + email);
      })
      .catch(err => {
        alert("Ошибка при копировании текста: " + err);
      });
  });
