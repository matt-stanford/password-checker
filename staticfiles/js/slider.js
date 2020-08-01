let pwLength = document.getElementById('pwLength');
let pwLengthValue = document.getElementById('pwLengthValue')
let copyIcon = document.getElementById('copy-icon')


pwLength.addEventListener('input', () => {
    pwLengthValue.innerHTML = pwLength.value;
});

copyIcon.addEventListener('click', () => {
    let copyText = document.getElementById('password-span');
    let textArea = document.createElement('textarea');
    textArea.value = copyText.textContent;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand('copy');
    textArea.remove();
});