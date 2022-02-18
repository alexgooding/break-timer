function toastControl(time, toastToTriggerId, toastToDismissId=null) {
    if (toastToDismissId != null) {
        var toastToDismiss = document.getElementById(toastToDismissId);
        toastToDismiss.classList.remove("show"); 
    }
    var toastToTrigger = document.getElementById(toastToTriggerId);
    var timeInMilliseconds = minutesToMilliseconds(time);
    setTimeout(function(){ toastToTrigger.classList.add("show"); }, timeInMilliseconds);
}

function minutesToMilliseconds(minutes) {
    return minutes * 1000 * 60;
}

function calculateSnoozeLength(minutes) {
    //return Math.round(minutes / 5);
    return minutes / 5;
}

function updateSnoozeButtons() {
    var breakLength = window.location.search.slice(1).split("&")[1].split("=")[1];
    var workLength = window.location.search.slice(1).split("&")[0].split("=")[1];
    var breakSnoozeLength = calculateSnoozeLength(breakLength);
    var workSnoozeLength = calculateSnoozeLength(workLength);

    document.getElementById('work-snooze-button').innerHTML = `Snooze for ${workSnoozeLength} minutes`
    document.getElementById('break-snooze-button').innerHTML = `Snooze for ${breakSnoozeLength} minutes`
}
