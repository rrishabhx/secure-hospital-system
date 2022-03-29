function newInsuranceBlock() {
    var object = document.getElementById('new-insurance-block');
    object.classList.toggle('d-none');
}

function newAppointment(){
    var object = document.getElementById('new-appointment-block');
    object.classList.toggle('d-none');
}
function popitup(url) {
    newwindow=window.open(url,'{{title}}','height=200,width=150');
    if (window.focus) {newwindow.focus()}
    return false;
}
