$(document).ready(function () {
    $('#main_menu_a').click(function (event) {
         $('.main_menu_index_ul').toggleClass('active_a');
         $('#main_menu_a').toggleClass('active_menu');
         $('.main_menu_index').toggleClass('main_menu_index_active');
    });
});