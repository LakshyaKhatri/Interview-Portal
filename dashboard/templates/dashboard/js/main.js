// fetches all applications and adds them to the datatable
function populateApplications() {
  let applicationDataURL = 'api/v1/applications/?sort=';

  if (ascending)
    applicationDataURL += currentSortingCol;
  else
    applicationDataURL += '-' + currentSortingCol;

  $.get(applicationDataURL, function(applicationList, status){
    const tableBody = document.getElementById('applications-table-body');
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
}

let currentSortingCol = 'applied_on';
let ascending = true;
populateApplications()    // Populate applications for the first time

function sort_applications(colHeadSpan){
  let downArrow = $(colHeadSpan).next();
  let upArrow = downArrow.next();

  if (colHeadSpan.id === currentSortingCol) {
    // If user clicked on same column again
    ascending = !ascending;
  } else {
    // If user clicked on another column
    // first remove arrows from that column header
    let prevArrow = $('#' + currentSortingCol).next();
    prevArrow.css('display', 'none');
    prevArrow.next().css('display', 'none');

    // update current sorting column
    currentSortingCol = colHeadSpan.id;
    ascending = true;
  }

  if (ascending) {
    upArrow.css('display', 'none');
    downArrow.css('display', 'inline');
  } else {
    upArrow.css('display', 'inline');
    downArrow.css('display', 'none');
  }

  populateApplications();
}
