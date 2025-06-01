document.getElementById('copyButton').addEventListener("click", () => {
const textToCopy = document.querySelector('.contacts__contact.text.text--big.is-mail').innerText;
navigator.clipboard.writeText(textToCopy)
.then(() => {
alert("Почта скопирована");
})
.catch(err => {
alert("Ошибка при копировании текста: " + err);
});
});
