
function validarFormulario() {
    var resp = validarRut();
    if (resp == false) {
        return false;
    }
    resp = validarFecha();
    if (resp == false) {
        return false;
    }
    resp = validaNombre();
    if (resp == false) {
        return false;
    }
    resp = validaApellido();
    if (resp == false) {
        return false;
    }
    return true;

}

function validaNombre() {
    var nombre = document.getElementById('txtNombre').value;
    var largo = nombre.trim().length;
    if (largo == 0) {
        //alert('el nombre esta vacio');
        Swal.fire({
            icon: 'error',
            title: 'nombre',
            text: 'el nombre esta vacio'
          });
        return false;
    }
    if (largo < 3) {
        //alert('el nombre tiene un largo menor a 3 caracteres');
        Swal.fire({
            icon: 'error',
            title: 'nombre',
            text: 'el nombre tiene un largo menor a 3 caracteres'
          });
        return false;
    }
    return true;
}

function validaApellido() {
    var apellido = document.getElementById('txtApellido').value;
    var largo = apellido.trim().length;
    if (largo == 0) {
        //alert('el apellido esta vacio');
        Swal.fire({
            icon: 'error',
            title: 'apellido',
            text: 'el apellido esta vacio'
          });
        return false;
    }
    if (largo < 3) {
        //alert('el apellido tiene un largo menor a 3 caracteres');
        Swal.fire({
            icon: 'error',
            title: 'apellido',
            text: 'el apellido tiene un largo menor a 3 caracteres'
          });
        return false;
    }
    return true;
}

function validarRut() {
    var rut = document.getElementById('txtRut').value;
    //alert(rut);
    var num = 3;
    var suma = 0;
    for (let index = 0; index < 8; index++) {
        var caracter = rut.slice(index, index + 1);
        //alert(caracter + ' x ' + num);
        suma = suma + (caracter * num);
        num = num - 1;
        if (num == 1) {
            num = 7;
        }
    }
    //alert('Suma:'+suma);
    var resto = suma % 11;
    var dv = 11 - resto;
    if (dv > 9) {
        if (dv == 10) {
            dv = 'K';
        } else {
            dv = 0;
        }
    }
    //alert('DV:'+dv);
    var dv_usuario = rut.slice(-1).toUpperCase();
    if (dv != dv_usuario) {
        //alert('rut incorrecto');
        //Swal.fire('el rut es incorrecto');
        Swal.fire({
            icon: 'error',
            title: 'digito verificador rut',
            text: 'el digito de su rut es incorrecto'
          });
        return false;
    }
    return true;
}

function validarFecha() {
    var fechaUsuario = document.getElementById('txtFechaNaci').value;
    var fechaSistema = new Date();
    console.log('Fecha Usuario:' + fechaUsuario);
    console.log('Fecha Sistema:' + fechaSistema);
    ////////////////////////////////////////// 2021-04-01
    var ano = fechaUsuario.slice(0, 4);
    var mes = fechaUsuario.slice(5, 7);
    var dia = fechaUsuario.slice(8, 10);
    console.log('A:' + ano + ' M:' + mes + ' D:' + dia);
    var fechaNuevaUsuario = new Date(ano, (mes - 1), dia);
    console.log('Nueva Fecha:' + fechaNuevaUsuario);
    //////////////////////////////////////////////////
    if (fechaNuevaUsuario > fechaSistema) {
        //alert('fecha de nacimiento mayor a la fecha actual');
        Swal.fire({
            icon: 'error',
            title: 'fecha de nacimiento',
            text: 'fecha de nacimiento mayor a la fecha actual'
          });
        return false;
    }
    ///////////////////////////////////////////////////
    var elDia = 24 * 60 * 60 * 1000;// cuantos milisegundos son 1 dia
    var dias = Math.trunc((fechaSistema.getTime() - fechaNuevaUsuario.getTime()) / elDia);
    console.log('Dias:' + dias);
    var anos = Math.trunc(dias / 365);
    if (anos < 18) {
        //alert('usted es menor de edad, solo tiene ' + anos + ' anos de edad');
        Swal.fire({
            icon: 'error',
            title: 'fecha de nacimiento',
            text: 'usted es menor de edad, solo tiene ' + anos + ' anos de edad'
          });
        return false;
    }
    return true;
}


$(document).ready(function() {
    $('#contact_form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            first_name: {
                validators: {
                        stringLength: {
                        min: 2,
                    },
                        notEmpty: {
                        message: 'Please enter your First Name'
                    }
                }
            },
             last_name: {
                validators: {
                     stringLength: {
                        min: 2,
                    },
                    notEmpty: {
                        message: 'Please enter your Last Name'
                    }
                }
            },
			 user_name: {
                validators: {
                     stringLength: {
                        min: 8,
                    },
                    notEmpty: {
                        message: 'Please enter your Username'
                    }
                }
            },
			 user_password: {
                validators: {
                     stringLength: {
                        min: 8,
                    },
                    notEmpty: {
                        message: 'Please enter your Password'
                    }
                }
            },
			confirm_password: {
                validators: {
                     stringLength: {
                        min: 8,
                    },
                    notEmpty: {
                        message: 'Please confirm your Password'
                    }
                }
            },
            email: {
                validators: {
                    notEmpty: {
                        message: 'Please enter your Email Address'
                    },
                    emailAddress: {
                        message: 'Please enter a valid Email Address'
                    }
                }
            },
            contact_no: {
                validators: {
                  stringLength: {
                        min: 12, 
                        max: 12,
                    notEmpty: {
                        message: 'Please enter your Contact No.'
                     }
                }
            },
			 department: {
                validators: {
                    notEmpty: {
                        message: 'Please select your Department/Office'
                    }
                }
            },
                }
            }
        })
        .on('success.form.bv', function(e) {
            $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
                $('#contact_form').data('bootstrapValidator').resetForm();

            // Prevent form submission
            e.preventDefault();

            // Get the form instance
            var $form = $(e.target);

            // Get the BootstrapValidator instance
            var bv = $form.data('bootstrapValidator');

            // Use Ajax to submit form data
            $.post($form.attr('action'), $form.serialize(), function(result) {
                console.log(result);
            }, 'json');
        });
});




