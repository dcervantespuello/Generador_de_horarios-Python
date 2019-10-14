$(document).ready(function () {

            (function ($) {

                $('#nombre').keyup(function () {

                    var rex = new RegExp($(this).val(), 'i');
                    $('.cursos tr').hide();
                    $('.cursos tr').filter(function () {
                        return rex.test($(this).text());
                    }).show();

                })

            }(jQuery));

        });
