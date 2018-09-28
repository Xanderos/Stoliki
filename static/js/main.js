var today, datepicker;
today = new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate());
$('#datepicker').datepicker({
          maxDate: function() {
              var date = new Date();
              date.setDate(date.getDate()+15);
              return new Date(date.getFullYear(), date.getMonth(), date.getDate());
          },
          minDate: today,
          format: 'dd/mm/yyyy'

});
