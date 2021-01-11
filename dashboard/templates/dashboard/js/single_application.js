let current_status = $('#status-select').val();

$('#status-select').on('change', function() {
  current_status = this.value;
});

const updateButton = $('.update-btn');

updateButton.on('click', function() {
  $('.spinner').show();
  updateButton.prop('disabled',true);

  $.post(
      '../api/v1/update-status/' + $('#current-application').text() + '/',
      $('#update-status-form').serialize()).done(function(response){
        const updateTextSpan = updateButton.children('span');

        setTimeout(function (){
          updateTextSpan.text('Updated');
          $('.status-tag').text($('#status-select option:selected').text());
          $('.spinner').hide();
          setTimeout(function (){
            updateTextSpan.text('Update');
            updateButton.prop('disabled',false);
          }, 1000);
        }, 1000);
      }
    );
});
