// setup ajax for save jobs

$(".save_form").submit(function (e) {
    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);
    var url = form.attr('action');

    $.ajax({
        type: "POST",
        url: url,
        data: form.serialize(),
        success: function (data) {
            if (data.is_saved) {
                form.find('.save-heart').addClass('fa-bookmark').removeClass('fa-bookmark-o').css('color', '#0984e3');
            }
        }
    });

});

$(".un_save_form").submit(function (e) {
    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);
    var url = form.attr('action');

    $.ajax({
        type: "POST",
        url: url,
        data: form.serialize(),
        success: function (data) {
            if (data.is_unsaved) {
                form.parent().parent().remove();
            }
        }
    });

});


//  apply for the job ajax 
$(".apply_form").submit(function (e) {
    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);
    var url = form.attr('action');

    $.ajax({
        type: "POST",
        url: url,
        data: form.serialize(),
        success: function (data) {
            if (data.is_apply) {
                form.find('.btn-info').addClass('btn-success').removeClass('btn-info').val("Thank You");
            }
        }
    });

});



// adding html editor 
/* $('textarea').addClass('ckeditor ')
CKEDITOR.replace('ckeditor'); */