$( document ).ready(function() {
    $('.slides').slick({
        slidesTofadeIn: 1, // numeros de imagens na tela
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

    // tip filter
    $('.btn').addClass('active');

    // funcao que checa se o botao all deve estar ativo
    function check_all_btn(){
        if($('#hotels').hasClass('active') &&
            $('#places').hasClass('active') &&
            $('#sbc').hasClass('active') &&
            $('#sao_paulo').hasClass('active'))
            $('#all').addClass('active');
        else
            $('#all').removeClass('active');
    };

    function filter_options(){
        $('.sao_paulo').fadeOut();
        $('.sbc').fadeOut();
        if($('#sao_paulo').hasClass('active') && $('#sbc').hasClass('active')){
            // alert('both');
            if($('#hotels').hasClass('active')){
                // alert('hotels');
                $('.hotels').fadeIn();
            }
            if($('#places').hasClass('active')){
                // alert('places');
                $('.places').fadeIn();
            }
        }
        else if($('#sao_paulo').hasClass('active')){
            // alert('sp');
            if($('#hotels').hasClass('active')){
                $('.hotels.sao_paulo').fadeIn();
            }
            if($('#places').hasClass('active')){
                $('.places.sao_paulo').fadeIn();
            }
        }            
        else if($('#sbc').hasClass('active')){
            // alert('sbc');
            if($('#hotels').hasClass('active')){
                $('.hotels.sbc').fadeIn();
            }
            if($('#places').hasClass('active')){
                $('.places.sbc').fadeIn();
            }
        }
    }

    function setDropDownName(){
        if($('#sao_paulo').hasClass('active') && $('#sbc').hasClass('active')){
            $('#dropdownMenuButton').text('São Paulo & SBC');
        }else if($('#sao_paulo').hasClass('active')){
            $('#dropdownMenuButton').text('São Paulo');
        }else if($('#sbc').hasClass('active')){
            $('#dropdownMenuButton').text('São Bernardo');
        }else{
            $('#dropdownMenuButton').text('Escolha uma Cidade:');
        }
        filter_options();
    };
    
    $('#all').click(function(){
        if($(this).hasClass('active')){
            $('.btn').removeClass('active');
            // $('.hotels,.places,.sbc,.sao_paulo').fadeOut();
        }else{
            $('.btn').addClass('active');
            // $('.hotels,.places,.sbc,.sao_paulo').fadeIn();
        }
        filter_options();
    });

    $('#hotels').click(function(){
        if($(this).hasClass('active')){
            $(this).removeClass('active');
            // $('.hotels').fadeOut();
        }else{
            $(this).addClass('active');
            // if($('#sao_paulo').hasClass('active') && $('#sbc').hasClass('active'))
            //     $('.hotels').fadeIn();
            // else if($('#sao_paulo').hasClass('active'))
            //     $('.hotels.sao_paulo').fadeIn();
            // else if($('#sbc').hasClass('active'))
            //     $('.hotels.sbc').fadeIn();
        }
        check_all_btn();
        filter_options();
    });

    $('#places').click(function(){
        // console.log($(this));
        // console.log($(this).hasClass('active'));
        if($(this).hasClass('active')){
            // console.log('ativo');
            $(this).removeClass('active');
            // $('.places').fadeOut();
        }else{
            // console.log('nao ativo');
            $(this).addClass('active');
            // if($('#sao_paulo').hasClass('active') && $('#sbc').hasClass('active'))
            //     $('.places').fadeIn();
            // else if($('#sao_paulo').hasClass('active'))
            //     $('.places.sao_paulo').fadeIn();
            // else if($('#sbc').hasClass('active'))
            //     $('.places.sbc').fadeIn();
        }
        check_all_btn();
        filter_options();
    });

    $('#sbc').click(function(){
        if($(this).hasClass('active')){
            $(this).removeClass('active');
            // $('.sbc').fadeOut();
        }else{
            $(this).addClass('active');
            // $('.sbc').fadeIn();
        }
        check_all_btn();
        setDropDownName();
    });

    $('#sao_paulo').click(function(){
        if($(this).hasClass('active')){
            $(this).removeClass('active');
            // $('.sao_paulo').fadeOut();
        }else{
            $(this).addClass('active');
            // $('.sao_paulo').fadeIn();
        }
        check_all_btn();
        setDropDownName();        
    });

    function initDropDownName(){
        $('#sao_paulo').addClass('active');
        $('#sbc').addClass('active');
        setDropDownName();
        filter_options();
    }

    initDropDownName();
});