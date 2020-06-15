
$(function () {

//    $(document).on('click', '.btnModal', function(){
//        $('#modal').modal('show');
//        CKEDITOR.replace('ckeditorwidget');
//    });

  /* Functions */

  var loadForm = function () {
    console.log('');
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-checklist .modal-content").html("");
        $("#modal-checklist").modal("show");
      },
      success: function (data) {
        $("#modal-checklist .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#modal-checklist").modal("hide");
        }
        else {
          $("#modal-checklist .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create ponto-controle
  $(".js-create-analise-ponto-controle").click(loadForm);
  $("#modal-checklist").on("submit", ".js-ponto-controle-create-form", saveForm);

  // Update ponto-controle
  $(".js-update-analise-ponto-controle").click(loadForm);
  $("#modal-checklist").on("submit", ".js-ponto-controle-update-form", saveForm);

  // Delete ponto-controle
  $("#ponto-controle-table").on("click", ".js-delete-ponto-controle", loadForm);
  $("#modal-checklist").on("submit", ".js-ponto-controle-delete-form", saveForm);

});



   
     