function toastControl(time, toastToTriggerId, toastToDismissId=null) {
    if (toastToDismissId != null) {
        var toastToDismiss = document.getElementById(toastToDismissId);
        toastToDismiss.classList.remove("show"); 
    }
    var toastToTrigger = document.getElementById(toastToTriggerId);
    countdownTimer(time);
    setTimeout(function(){ toastToTrigger.classList.add("show"); }, time);
}

function countdownTimer(milliseconds) {
    var timerElement = document.getElementById("timer");
    var timeLeft = milliseconds;
    timerElement.innerHTML = formatMillisecondsToTime(timeLeft);
    var interval = setInterval(function() {
        timeLeft -= 1000;
        timerElement.childNodes[0].textContent = formatMillisecondsToTime(timeLeft);
        if (timeLeft <= 0) {
            clearInterval(interval);
            var audioAlert = document.getElementById("back-to-work-alert");
            audioAlert.play();
        }  
    }, 1000);
}

function formatMillisecondsToTime(milliseconds) {
    var totalSeconds = milliseconds / 1000;
    var seconds = totalSeconds % 60;
    var minutes = (totalSeconds - seconds) / 60;
    var hours = (minutes - (minutes % 60)) / 60;

    return formatTimeComponent(hours) + ":" + formatTimeComponent(minutes) + ":" + formatTimeComponent(seconds)
}

function formatTimeComponent(value) {
    return ("0" + value).slice(-2);
}


function updateMuteButtonValue() {
    $.ajax({
        url: "/mute",
        type: "POST",
        headers: {
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        success: (data) => {
          console.log(data);
        },
        error: (error) => {
          console.log(error);
        }
      });
}