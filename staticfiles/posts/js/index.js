function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");

// NewsLetter

const form2 = document.getElementById('formNewsletter')
const csr = document.getElementsByName("csrfmiddlewaretoken")[0].value;

form2.addEventListener('submit', (event) => {
  event.preventDefault()
  const email = document.getElementById('email').value

  $.ajax({
    type: "POST",
    url: 'newsletter/subscribers',
    data: {
      email: email,
      csrfmiddlewaretoken: csrftoken
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
    // $('.input-serach').attr('autofocus','on');

  });
});