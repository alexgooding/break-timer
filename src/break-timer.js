function toastControl(time, toastToTriggerId, toastToDismissId=null) {
    if (toastToDismissId != null) {
        var toastToDismiss = document.getElementById(toastToDismissId);
        toastToDismiss.classList.remove("show"); 
    }
    var toastToTrigger = document.getElementById(toastToTriggerId);
    var timeInMinutes = time * 1000 * 60;
    setTimeout(function(){ toastToTrigger.classList.add("show"); }, timeInMinutes);
}
