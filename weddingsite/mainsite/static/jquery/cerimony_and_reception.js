$( document ).ready(function() {
    $('.slides').slick({
        slidesToShow: 1, // numeros de imagens na tela
        slidesToScroll: 1, //numeros de imagens a ser mostrado por vez
        autoplay: true, // animacao do slider ativado
        autoplaySpeed: 4000, // tempo entre transições

        dots: false, // mostra os pontinhos
        infinite: true, // volta para a primeira imagem
        speed: 500, // velocidade do fade
        fade: true, // se tem fade
        cssEase: 'linear', // estilo do fade?
        arrows: false, //remove as setas de navegação
        
        draggable: false, // bloqueia a acessibilidade do slider
        mobileFirst: true, // responsivo para mobile, testar
        pauseOnFocus: false, // define se pausa quando estiver com o componente focado
        pauseOnHover: false, // define se pausa quando estiver com o mouse em cima
        touchMove: false // bloqueia a acessibilidade do slider
    });

    //back button
    var btn = $('#button');
    btn.click(function(){
        $("html, body").animate({scrollTop: 0}, 1000);
    });

    //google maps
    function initMap() {
        // The location of Centro Universitario FEI
        // -23.726328, -46.581292
        
        var marker_place = {lat: -23.724526, lng: -46.579869};
        var place = {lat: -23.723220, lng: -46.572965};
        // ,19,-z
        // The map, centered at Centro Universitario FEI
        var map = new google.maps.Map(
            document.getElementById('map'), {zoom: 15, center: place});
        // The marker, positioned at Centro Universitario FEI
        var marker = new google.maps.Marker({position: marker_place, map: map});
    }
    initMap();
      
});