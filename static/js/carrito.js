

var eliminatItemBtn = document.getElementsByClassName('borrar-item')
document.querySelector('#vaciar-carrito').addEventListener('click', function(){

    var accion = this.dataset.accion


    vaciarCarrito(accion)



})









for(var i = 0 ; i < eliminatItemBtn.length; i++ ){
    eliminatItemBtn[i].addEventListener('click',function(){
        var productoId = this.dataset.producto
        var accion = this.dataset.accion
        // console.log('productoId:', productoId, 'accion:', accion)

        // console.log('USER:', user)
        if (user == 'AnonymousUser'){
            console.log('El usuario no está autenticadao')
        } else {
            // console.log('El usuario está autenticado..')
            borrarProductoCarrito(productoId, accion)
        }
    })

}


function borrarProductoCarrito(productoId,accion){
    // console.log('El usuario esta lgueado enviando data...')

    var url = '/borrarItemCarrito/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken ,
        },
        body:JSON.stringify({'productoId': productoId ,'accion': accion})
    })
    //respuesta
    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        console.log('data:', data)
        location.reload()
    })


}



function vaciarCarrito(accion){

    
    var url = '/vaciarCarrito/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken ,
        },
        body:JSON.stringify({'accion': accion})
    })
    //respuesta
    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        console.log('data:', data)
        location.reload()
    })




}


