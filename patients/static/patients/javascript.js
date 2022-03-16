function created() {
    document.getElementById('home').classList = "list-group-item list-group-item-dark";
    document.getElementById('appointments').classList = "list-group-item list-group-item-light";
    document.getElementById('diagnosis').classList = "list-group-item list-group-item-light";
    document.getElementById('prescriptions').classList = "list-group-item list-group-item-light";
    document.getElementById('reports').classList = "list-group-item list-group-item-light";
    document.getElementById('insurance').classList = "list-group-item list-group-item-light";
    document.getElementById('transactions').classList = "list-group-item list-group-item-light";
    document.getElementById('profile').classList = "list-group-item list-group-item-light";

    document.getElementById('home-view').style.display = 'block';

}

function switchPage(page) {
    var home = document.getElementById('home');
    var appointments = document.getElementById('appointments');
    var diagnosis = document.getElementById('diagnosis');
    var prescriptions = document.getElementById('prescriptions');
    var reports = document.getElementById('reports');
    var insurance = document.getElementById('insurance');
    var transactions = document.getElementById('transactions');
    var profile = document.getElementById('profile');

    var homeView = document.getElementById("home-view")
    var appointmentsView = document.getElementById("appointments-view")
    var diagnosisView = document.getElementById("diagnosis-view")
    var prescriptionsView = document.getElementById("prescriptions-view")
    var reportsView = document.getElementById("reports-view")
    var insuranceView = document.getElementById("insurance-view")
    var transactionsView = document.getElementById("transactions-view")
    var profileView = document.getElementById("profile-view")


    if (page === 'home') {
        home.classList = "list-group-item list-group-item-dark";
        appointments.classList = "list-group-item list-group-item-light";
        diagnosis.classList = "list-group-item list-group-item-light";
        prescriptions.classList = "list-group-item list-group-item-light";
        reports.classList = "list-group-item list-group-item-light";
        insurance.classList = "list-group-item list-group-item-light";
        transactions.classList = "list-group-item list-group-item-light";
        profile.classList = "list-group-item list-group-item-light";

        homeView.style.display = 'block';
        appointmentsView.style.display = 'none';
        diagnosisView.style.display = 'none';
        prescriptionsView.style.display = 'none';
        reportsView.style.display = 'none';
        insuranceView.style.display = 'none';
        transactionsView.style.display = 'none';
        profileView.style.display = 'none';

    } else if (page === 'appointments') {
        home.classList = "list-group-item list-group-item-light";
        appointments.classList = "list-group-item list-group-item-dark";
        diagnosis.classList = "list-group-item list-group-item-light";
        prescriptions.classList = "list-group-item list-group-item-light";
        reports.classList = "list-group-item list-group-item-light";
        insurance.classList = "list-group-item list-group-item-light";
        transactions.classList = "list-group-item list-group-item-light";
        profile.classList = "list-group-item list-group-item-light";

        homeView.style.display = 'none';
        appointmentsView.style.display = 'block';
        diagnosisView.style.display = 'none';
        prescriptionsView.style.display = 'none';
        reportsView.style.display = 'none';
        insuranceView.style.display = 'none';
        transactionsView.style.display = 'none';
        profileView.style.display = 'none';

    } else if (page === 'diagnosis') {
        home.classList = "list-group-item list-group-item-light";
        appointments.classList = "list-group-item list-group-item-light";
        diagnosis.classList = "list-group-item list-group-item-dark";
        prescriptions.classList = "list-group-item list-group-item-light";
        reports.classList = "list-group-item list-group-item-light";
        insurance.classList = "list-group-item list-group-item-light";
        transactions.classList = "list-group-item list-group-item-light";
        profile.classList = "list-group-item list-group-item-light";

        homeView.style.display = 'none';
        appointmentsView.style.display = 'none';
        diagnosisView.style.display = 'block';
        prescriptionsView.style.display = 'none';
        reportsView.style.display = 'none';
        insuranceView.style.display = 'none';
        transactionsView.style.display = 'none';
        profileView.style.display = 'none';

    } else if (page === 'prescriptions') {
        home.classList = "list-group-item list-group-item-light";
        appointments.classList = "list-group-item list-group-item-light";
        diagnosis.classList = "list-group-item list-group-item-light";
        prescriptions.classList = "list-group-item list-group-item-dark";
        reports.classList = "list-group-item list-group-item-light";
        insurance.classList = "list-group-item list-group-item-light";
        transactions.classList = "list-group-item list-group-item-light";
        profile.classList = "list-group-item list-group-item-light";

        homeView.style.display = 'none';
        appointmentsView.style.display = 'none';
        diagnosisView.style.display = 'none';
        prescriptionsView.style.display = 'block';
        reportsView.style.display = 'none';
        insuranceView.style.display = 'none';
        transactionsView.style.display = 'none';
        profileView.style.display = 'none';

    } else if (page === 'reports') {
        home.classList = "list-group-item list-group-item-light";
        appointments.classList = "list-group-item list-group-item-light";
        diagnosis.classList = "list-group-item list-group-item-light";
        prescriptions.classList = "list-group-item list-group-item-light";
        reports.classList = "list-group-item list-group-item-dark";
        insurance.classList = "list-group-item list-group-item-light";
        transactions.classList = "list-group-item list-group-item-light";
        profile.classList = "list-group-item list-group-item-light";

        homeView.style.display = 'none';
        appointmentsView.style.display = 'none';
        diagnosisView.style.display = 'none';
        prescriptionsView.style.display = 'none';
        reportsView.style.display = 'block';
        insuranceView.style.display = 'none';
        transactionsView.style.display = 'none';
        profileView.style.display = 'none';

    } else if (page === 'insurance') {
        home.classList = "list-group-item list-group-item-light";
        appointments.classList = "list-group-item list-group-item-light";
        diagnosis.classList = "list-group-item list-group-item-light";
        prescriptions.classList = "list-group-item list-group-item-light";
        reports.classList = "list-group-item list-group-item-light";
        insurance.classList = "list-group-item list-group-item-dark";
        transactions.classList = "list-group-item list-group-item-light";
        profile.classList = "list-group-item list-group-item-light";

        homeView.style.display = 'none';
        appointmentsView.style.display = 'none';
        diagnosisView.style.display = 'none';
        prescriptionsView.style.display = 'none';
        reportsView.style.display = 'none';
        insuranceView.style.display = 'block';
        transactionsView.style.display = 'none';
        profileView.style.display = 'none';

    } else if (page === 'transactions') {
        home.classList = "list-group-item list-group-item-light";
        appointments.classList = "list-group-item list-group-item-light";
        diagnosis.classList = "list-group-item list-group-item-light";
        prescriptions.classList = "list-group-item list-group-item-light";
        reports.classList = "list-group-item list-group-item-light";
        insurance.classList = "list-group-item list-group-item-light";
        transactions.classList = "list-group-item list-group-item-dark";
        profile.classList = "list-group-item list-group-item-light";

        homeView.style.display = 'none';
        appointmentsView.style.display = 'none';
        diagnosisView.style.display = 'none';
        prescriptionsView.style.display = 'none';
        reportsView.style.display = 'none';
        insuranceView.style.display = 'none';
        transactionsView.style.display = 'block';
        profileView.style.display = 'none';

    } else if (page === 'profile') {
        home.classList = "list-group-item list-group-item-light";
        appointments.classList = "list-group-item list-group-item-light";
        diagnosis.classList = "list-group-item list-group-item-light";
        prescriptions.classList = "list-group-item list-group-item-light";
        reports.classList = "list-group-item list-group-item-light";
        insurance.classList = "list-group-item list-group-item-light";
        transactions.classList = "list-group-item list-group-item-light";
        profile.classList = "list-group-item list-group-item-dark";

        homeView.style.display = 'none';
        appointmentsView.style.display = 'none';
        diagnosisView.style.display = 'none';
        prescriptionsView.style.display = 'none';
        reportsView.style.display = 'none';
        insuranceView.style.display = 'none';
        transactionsView.style.display = 'none';
        profileView.style.display = 'block';

    }
}