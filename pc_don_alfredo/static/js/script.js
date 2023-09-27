$(document).ready(function () {
    $("#miCarrusel").carousel();
});

$(document).ready(function () {
    $("#orderForm").submit(function (e) {
        e.preventDefault();

        $.ajax({
            type: "POST",
            url: "{% url 'process_order' %}",
            data: $(this).serialize(),
            success: function (data) {
                alert("Pedido enviado correctamente");
                $('#orderModal').modal('hide');
            },
            error: function () {
                alert("Error al enviar el pedido");
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('#cake-order-form');
    form.addEventListener('submit', function (event) {
        event.preventDefault();

        if (form.checkValidity()) {

            form.submit();

            window.alert('Pedido realizado con éxito. ¡Gracias por tu pedido!');
        }
    });
});

var today = new Date();

var minDate = new Date(today);
minDate.setDate(today.getDate() + 2);

var minDateFormatted = minDate.toISOString().split('T')[0];

document.getElementById('pickup_date').setAttribute('min', minDateFormatted);