
$(function() {
    $("#rut").rut().on('rutValido', function(e, rut, dv) {
        alert("El rut " + rut + "-" + dv + " es correcto");
    }, { minimumLength: 7} );
})
