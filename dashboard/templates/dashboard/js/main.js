// fetches all applications and adds them to the datatable
$.get("api/v1/applications", function(applicationList, status){
  const tableBody = document.getElementById("applications-table-body");
  tableBody.innerHTML = '';

  $.each(applicationList, function(index, application){
    const application_row = tableBody.insertRow(-1);
    application_row.insertCell(-1).innerHTML = application.name;
    application_row.insertCell(-1).innerHTML = '<span class="col-email-txt">' + application.email + '</span>';
    application_row.insertCell(-1).innerHTML = '<span class="col-type-txt">' + application.type + '</span>';
    application_row.insertCell(-1).innerHTML = '<span class="col-technology-txt">' + application.technology + '</span>';
    application_row.insertCell(-1).innerHTML = '<span class="col-status-txt">' + application.status + '</span>';
    application_row.insertCell(-1).innerHTML = application.moved_by;
    application_row.insertCell(-1).innerHTML = application.updated_on;
    application_row.insertCell(-1).innerHTML = application.applied_on;
  });
});
