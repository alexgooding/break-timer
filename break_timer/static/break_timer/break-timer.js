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
        async: false,
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
    var result = null;
    $.ajax({
        url: "/mute/",
        type: "GET",
        async: false,
        headers: {
          "X-Requested-With": "XMLHttpRequest"
        },
        success: (data) => {
          result = data;
        },
        error: (error) => {
          console.log(error);
        }
      });
    return result;
}

function muteElem(elem) {
    elem.muted = true;
    elem.pause();
}

function unmuteElem(elem) {
  elem.muted = false;
}

function mutePage() {
    document.querySelectorAll("audio").forEach(elem => muteElem(elem));
}

function unmutePage() {
  document.querySelectorAll("audio").forEach(elem => unmuteElem(elem));
}

function configureAudioElements() {
  // mute page if mute enabled
  response = getMuteButtonValue();
  var muteCheckbox = document.getElementById('mute-button-checkbox');
  if (response === 'True') {
      muteCheckbox.checked = true;
      mutePage();
      console.log("Page muted");
  }
  else {
      muteCheckbox.checked = false;
      unmutePage();
      console.log("Page unmuted");
  }
}

function onClickMuteControl() {
    // update mute button value
    updateMuteButtonValue();

    configureAudioElements();    
} 
