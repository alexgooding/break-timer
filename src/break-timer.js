function triggerAlert(time) {
    var toast = document.getElementById("toast");
    var timeInMinutes = time * 1000 * 60;
    setTimeout(function(){ toast.classList.add("show"); }, timeInMinutes);
}

function dismissAlert(time) {
    var toast = document.getElementById("toast");
    toast.classList.remove("show"); 
    triggerAlert(time);
}
