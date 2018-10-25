var imagem= document.querySelector('img');
imagem.onclick=function(){
    var local=imagem.getAttribute('src');

    if(local==='imagens/doodle.gif'){
        imagem.setAttribute('src','imagens/final.gif');

    }else{
        imagem.setAttribute('src','imagens/doodle.gif');
    }
}