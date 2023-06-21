formNewsletter2 = document.querySelector('#formNewsletter2')
formNewsletter2.addEventListener('submit', (event) => {
    event.preventDefault()
    const csr2 = formNewsletter1.firstElementChild.value

    const email = document.getElementById('email2').value

    $.ajax({
        type: "POST",
        url: '/newsletter/subscribers',
        data: {
            email: email,
            csrfmiddlewaretoken: csr2
        },

        success: function (response) {
            if (response.userExist) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'It seems that you have already subscribed!',
                    footer: '🙂'
                })
            }

            if (response.subscribed) {
                Swal.fire(
                    'Subscribe Succesfull!',
                    'Now you will recieve some cool newsletters!',
                    'success'
                )
            }
        }
    });
})






// newsletter

formNewsletter1 = document.querySelector('#formNewsletter1')
formNewsletter1.addEventListener('submit', (event) => {
    event.preventDefault()
    const csr1 = formNewsletter1.firstElementChild.value
    const email = document.getElementById('email1').value
    $.ajax({
        type: "POST",
        url: '/newsletter/subscribers',
        data: {
            email: email,
            csrfmiddlewaretoken: csr1
        },

        success: function (response) {
            if (response.userExist) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'It seems that you have already subscribed!',
                    footer: '🙂'
                })
            }

            if (response.subscribed) {
                Swal.fire(
                    'Subscribe Succesfull!',
                    'Now you will recieve some cool newsletters!',
                    'success'
                )
            }
        }
    });
})





$(document).ready(function () {
    $('#search').click(function (e) {

        e.preventDefault();
        $('.menu-item').toggleClass('hide-item');
        $('.search-form').toggleClass('active-serach-form');
        $('.serach-dropdown').toggleClass('hide-dropdown');

    });
});