$(document).ready(function () {

    
    $("#menu").click(function (event) {
        let dashboard = document.getElementById("dashboard");
        let main = document.getElementById("content_container")
        
        if (dashboard.style.display == "none") {
            dashboard.style.display = "block";
            main.className = "col-md-9 ml-sm-auto col-lg-10 px-md-4";
            localStorage.setItem("is_dashboard", 1);
        } else {
            main.className = "";
            dashboard.style.display = "none"
            localStorage.setItem("is_dashboard", 0);
        }
    })
    
    if (localStorage.getItem("is_dashboard") == 0) {
        $("#menu").click();
    }
    // making menu icon invisible in mobile devices
    if (window.innerWidth < 768) {
        document.getElementById("menu").style.display = "none"
    }

    // checking if there is change in the screeen size
    $(window).resize(function () {
        if (window.innerWidth < 768) {
            document.getElementById("menu").style.display = "none"
        }
        else
        {
            document.getElementById("menu").style.display = "inline"
        }
    });
})