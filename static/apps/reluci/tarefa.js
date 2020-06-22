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
          $("#accordion-tarefas").html(data.html_tarefa_list);
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

  // Create observacao-tarefa
  $(".js-create-observacao-tarefa").click(loadForm);
  $("#modal-ponto-controle").on("submit", ".js-observacao-tarefa-create-form", saveForm);

  // Update observacao-tarefa
  $(".js-update-observacao-tarefa").click(loadForm);
  $("#modal-ponto-controle").on("submit", ".js-observacao-tarefa-update-form", saveForm);

  // Delete observacao-tarefa
  $("#observacao-tarefa-table").on("click", ".js-delete-observacao-tarefa", loadForm);
  $("#modal-ponto-controle").on("submit", ".js-observacao-tarefa-delete-form", saveForm);

});



   
     