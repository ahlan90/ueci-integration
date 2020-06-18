$(function () {

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-ponto-controle .modal-content").html("");
        $("#modal-ponto-controle").modal("show");
      },
      success: function (data) {
        $("#modal-ponto-controle .modal-content").html(data.html_form);
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
          console.log(data);
          $("#analise-ponto-controle-table tbody").html(data.html_analise_ponto_controle_list);
          $("#modal-ponto-controle").modal("hide");
        }
        else {
          $("#modal-ponto-controle .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create ponto-controle
  $(".js-create-analise-ponto-controle").click(loadForm);
  $("#modal-ponto-controle").on("submit", ".js-ponto-controle-create-form", saveForm);

  // Update ponto-controle
  $(".js-update-analise-ponto-controle").click(loadForm);
  $("#modal-ponto-controle").on("submit", ".js-ponto-controle-update-form", saveForm);

  // Delete ponto-controle
  $("#ponto-controle-table").on("click", ".js-delete-ponto-controle", loadForm);
  $("#modal-ponto-controle").on("submit", ".js-ponto-controle-delete-form", saveForm);

});



   
     