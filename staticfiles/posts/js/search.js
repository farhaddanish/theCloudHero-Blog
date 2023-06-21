$(document).ready(function () {

    $('#search').click(function (e) {
        e.preventDefault();
        $('.menu-item').toggleClass('hide-item');
        $('.search-form').toggleClass('active-serach-form');
        $('.serach-dropdown').toggleClass('hide-dropdown');
        

    });
});