document.getElementById("lang").addEventListener("change",(event)=>{
    const form = document.createElement('form');
    form.method = 'POST';
    const langInput = document.createElement('input');
    langInput.type = "hidden"
    langInput.name = 'lang';
    langInput.value = event.target.value;
    form.appendChild(langInput);
    document.getElementsByTagName("body")[0].appendChild(form);
    form.submit();
})