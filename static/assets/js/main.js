const btnDelete = document.querySelectorAll('.delete');

if(btnDelete){
    const buttons = Array.from(btnDelete);

    buttons.forEach(function(btn){
        btn.addEventListener('click', (evt)=>{
            if(! confirm('Esta seguro de querer eliminar?')){
                evt.preventDefault();
            }
        });
    })
}
