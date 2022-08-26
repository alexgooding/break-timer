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
        url: "/mute/",
        type: "POST",
        headers: {
          "X-Requested-With": "XMLHttpRequest"
        },
        success: (data) => {
          console.log(data);
        },
        error: (error) => {
          console.log(error);
        }
      });
}

function getMuteButtonValue() {
    $.ajax({
        url: "/mute/",
        type: "GET",
        headers: {
          "X-Requested-With": "XMLHttpRequest"
        },
        success: (data) => {
          console.log(data);
          // TODO return data asychronously
          return data;
        },
        error: (error) => {
          console.log(error);
        }
      });
}

function muteElem(elem) {
    elem.muted = true;
    elem.pause();
}

function mutePage() {
    document.querySelectorAll("audio").forEach(elem => muteElem(elem));
}

function pageMuteControl() {
    // update mute button value
    updateMuteButtonValue();

    // mute page is mute enabled
    response = getMuteButtonValue();
    mute = Boolean(response);
    console.log(response);
    console.log(mute);
    if (mute) {
        mutePage();
        console.log("Page muted");
    }
    else {
        // TODO unmute page
    }
} 
