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
