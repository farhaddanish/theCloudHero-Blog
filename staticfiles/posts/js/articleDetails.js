// newsletter 2
formNewsletter2 = document.querySelector("#formNewsletter2");
formNewsletter2.addEventListener("submit", (event) => {
    event.preventDefault();
    const csr2 = formNewsletter1.firstElementChild.value;
    const email = document.getElementById("email2").value;
    console.log(email)
    $.ajax({
        type: "POST",
        url: "/newsletter/subscribers",
        data: {
            email: email,
            csrfmiddlewaretoken: csr2,
        },

        success: function (response) {
            if (response.userExist) {
                Swal.fire({
                    icon: "error",
                    title: "Oops...",
                    text: "It seems that you have already subscribed!",
                    footer: "🙂",
                });
            }

            if (response.subscribed) {
                Swal.fire(
                    "Subscribe Succesfull!",
                    "Now you will recieve some cool newsletters!",
                    "success"
                );
            }
        },
    });
});

// serach

$(document).ready(function () {
    $("#search").click(function (e) {
        e.preventDefault();
        $(".menu-item").toggleClass("hide-item");
        $(".search-form").toggleClass("active-serach-form");
        $(".serach-dropdown").toggleClass("hide-dropdown");
    });
});




 // newsletter

formNewsletter1 = document.querySelector("#formNewsletter1");
formNewsletter1.addEventListener("submit", (event) => {
    event.preventDefault();
    const csr1 = formNewsletter1.firstElementChild.value;
    const email = document.getElementById("email1").value;
    $.ajax({
        type: "POST",
        url: "/newsletter/subscribers",
        data: {
            email: email,
            csrfmiddlewaretoken: csr1,
        },

        success: function (response) {
            if (response.userExist) {
                Swal.fire({
                    icon: "error",
                    title: "Oops...",
                    text: "It seems that you have already subscribed!",
                    footer: "🙂",
                });
            }

            if (response.subscribed) {
                Swal.fire(
                    "Subscribe Succesfull!",
                    "Now you will recieve some cool newsletters!",
                    "success"
                );
            }
        },
    });
});

const form = document.getElementById("form-ajax");
const csr = document.getElementsByName("csrfmiddlewaretoken")[0].value;
const errorBlock = document.querySelector(".errorBlock");
form.addEventListener("submit", (event) => {
    errorBlock.classList.remove("errorlist");
    event.preventDefault();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const url = "/loginWithAjax";

    $.ajax({
        type: "POST",
        url: url,
        data: {
            email: email,
            password: password,
            csrfmiddlewaretoken: csr,
        },

        success: function (response) {
            if (response.login) {
                const memberDiv = document.getElementById("member-login-id");

                memberDiv.innerHTML = `
                <h3 class="member-login-heading">Thanks for joining with us :</h3>
                        <p class="register-paragragh"> TheCloudHeros will send you some cool idea's , articles
                                     and newsLetters to your email. to be in touch with your purposes  </p>
                                     <i class="fas fa-smile-beam icon-login  "></i>`;
                Swal.fire(
                    "Subscribe Succesfull!",
                    "Thanks for your joining to TheCloudHeros",
                    "success"
                );
            } else {
                errorBlock.classList.add("errorlist");
            }
        },
    });
});