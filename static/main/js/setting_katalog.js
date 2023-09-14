$(document).ready(function () {

    $('.header-burger').click(function (event) {
        $('.header-burger,.header-menu_1,.header-menu_2').toggleClass('active');
    });

    $('.popup-link').click(function (event) {
        let tg = window.Telegram.WebApp;
        document.getElementById("first_name_user").value = tg.initDataUnsafe.user.first_name;
        document.getElementById("last_name_user").value = tg.initDataUnsafe.user.last_name;
    });


    $('.Plus_Kol').on('TouchEvent click', function (event) {
        var $input = $(this).parent().find('input');
        $input.val(parseInt($input.val()) + 1);
        $input.change();
        return false;
    });

    $('.Minus_Kol').on('TouchEvent click', function (event) {
        var $input = $(this).parent().find('input');
        var count = parseInt($input.val()) - 1;
        count = count < 1 ? 1 : count;
        $input.val(count);
        $input.change();
        return false;
    });


    $('.submit__orders').click(function (event) {

        if ($('.product_name_cart').text() !== '') {

        } else {
            alert("Карзина пуста 🤷🏼‍♀️")
            event.preventDefault();
        }
    });

    $('#back_id').click(function (event) {
        window.history.go(-1)
    });

    $('.basket').click(function (event) {
        if ($('#id_quantity').val() === '') {
            alert("Вы не указали количество 😞");
            event.preventDefault()
        } else {

        }
    })


});


$(function () {
    //2. Получить элемент, к которому необходимо добавить маску
    $("#telefon").mask("+7(999)999-99-99");
    $("#id_quantity").mask("9");
});

const popupLinks = document.querySelectorAll('.popup-link');
const body = document.querySelector('body');
const lockPadding = document.querySelectorAll('.lock_padding');
const html = document.documentElement;
const scrollPosition = window.pageYOffset;
const padContent = document.getElementById("content_product_click");

let unlock = true;

const timeout = 800;

if (popupLinks.length > 0) {
    for (let index = 0; index < popupLinks.length; index++) {
        const popupLink = popupLinks[index];
        popupLink.addEventListener("click", function (e) {
            const popupName = popupLink.getAttribute('href').replace('#', '');
            const curentPopup = document.getElementById(popupName);
            popupOpen(curentPopup);
            e.preventDefault();
        });
    }
}

const popupCloseIcon = document.querySelectorAll('.close_pupop');
if (popupCloseIcon.length > 0) {
    for (let index = 0; index < popupCloseIcon.length; index++) {
        const el = popupCloseIcon[index];
        el.addEventListener('click', function (e) {
            popupClose(el.closest('.popup'));
            e.preventDefault();
        });
    }
}


function popupOpen(curentPopup) {
    if (curentPopup && unlock) {
        const popupActive = document.querySelector('.popup.open');
        if (popupActive) {
            popupClose(popupActive, false);
        } else {
            bodyLock();
        }
        curentPopup.classList.add('open');
        curentPopup.addEventListener('click', function (e) {
            if (!e.target.closest('.popup_content')) {
                popupClose(e.target.closest('.popup'));
            }
        });

    }
}

function popupClose(popupActive, doUnlock = true) {
    if (unlock) {
        popupActive.classList.remove('open');
        if (doUnlock) {
            bodyUnLock();
        }
    }
}


function bodyLock() {
    body.classList.add('lock');
    html.style.top = -scrollPosition + "px";
    html.classList.add("open_activ");
    document.querySelector('.popup_content').focus();

}


function bodyUnLock() {
    body.classList.remove('lock');
    html.classList.remove("open_activ");
    window.scrollTo(0, scrollPosition);
    html.style.top = "";
    this.starter.focus();
}

