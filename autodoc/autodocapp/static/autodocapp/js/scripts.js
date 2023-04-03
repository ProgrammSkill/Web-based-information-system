
var overlay = document.querySelector('#overlay-modal');

var old_value_mark;

$("#table tbody").on("click", ".BthEditMark", function(e){
    e.preventDefault();
    var $this = $(this);
    let name_mark = $this.parents(".record").find('td').eq(0).text();
    old_value_mark =  $this.parents(".record").find('td').eq(0);
    $("#formEditMark input[name='brand']").val(name_mark);
    $("#formEditMark").attr("action", $this.attr("href"));
    overlay.classList.add('active');
    $("#ModalEditMark").css('display','block');
    return false;
});

$(".close").on("click", function(e){
    $(".modal").css('display','none');
    overlay.classList.remove('active');
});



$("#formEditMark").on("submit", function(e){
    e.preventDefault();
    e.stopPropagation();
    var $this = $(this);
    var valid = true;
    $('#formEditMark input').each(function() {
        let $this = $(this);

        if(!$this.val()) {
            valid = false;
//            $this.parents('.validate').find('.mySpan').text($this.attr('name').replace(/[\_]+/g, ' ') + ' ошибка в запросе');
            $this.parents('.validate').find('.mySpan').text('Поле пустое');
        }
    });

    if(valid){
        let data = $this.serialize();
        $.ajax({
            url: $this.attr("action"),
            type: "POST",
            data: data,
            dataType: "json",
            success: function(resp){
                $("#ModalEditMark").css('display','none');
                overlay.classList.remove('active');
                let new_value_mark = $("#formEditMark input[name='brand']").val();
                old_value_mark.replaceWith('<td>'+new_value_mark+'</td>');
            },
            error: function(resp){
                alert("Что-то пошло не так при редактировании");
            }
        });
    }
    return false;
});

$(".js-create-mark").on("click", function(e){
    overlay.classList.add('active');
    $("#ModalCreateMark").css('display','block');
    return false;
});


/* Binding */
//$(".js-create-product").click(loadForm);
//$("#formCreateMark").on("submit", function(e){
////    e.preventDefault();
//    e.stopPropagation();
//    var $this = $(this);
//    var valid = true;
//
//    $('#formCreateMark input').each(function() {
//        let $this = $(this);
//
//        if(!$this.val()) {
//            valid = false;
//            $this.parents('.validate').find('.mySpan').text('Поле пустое');
//        }
//    });

//    if(valid){
//        let data = $this.serialize();
//        $.ajax({
//            url: $this.attr("action"),
//            type: "POST",
//            data: data,
//            dataType: "json",
//            success: function(resp){
//
//                $('#formCreateMark input').each(function() {
//
//                    $('#formCreateMark input').val('');
//
//                });
//
//                $("#ModalCreateMark").css('display','none');
//                overlay.classList.remove('active');
//            },
//            error: function(resp){
//                alert("Что-то пошло не так при добавлении марки");
//            }
//        });
//    }
//    return false;
//});


$(".btn_delete_record").on("click", function(e){
    e.preventDefault();
    var $this = $(this);
    if(confirm("Вы точно хотите удалить?")){
        $.ajax({
            url: $this.attr("href"),
            type: "GET",
            dataType: "json",
            success: function(resp){
                $this.parents('.record').fadeOut("slow", function(){
                    $this.parents('.record').remove();
                });
            },
            error: function(resp){
                alert("Возникла ошибка при удалении");
            }
        });
    }
    return false;
});



//======================================================================================================================
//Editing the model

var old_value_model;

$("#table tbody").on("click", ".BthEditModel", function(e){
    e.preventDefault();
    var $this = $(this);
    let name_model = $this.parents(".record").find('td').eq(0).text();
    old_value_model =  $this.parents(".record").find('td').eq(0);
    $("#formEditModel input[name='model']").val(name_model);
    $("#formEditModel").attr("action", $this.attr("href"));
    overlay.classList.add('active');
    $("#ModalEditModel").css('display','block');
    return false;
});

$(".js-create-model").on("click", function(e){
    overlay.classList.add('active');
    $("#ModalCreateModel").css('display','block');
    return false;
});


$(".close").on("click", function(e){
    $("#ModalEditModel").css('display','none');
    $("#ModalCreateModel").css('display','none');
    overlay.classList.remove('active');
});

$("#formEditModel").on("submit", function(e){
    e.preventDefault();
    e.stopPropagation();
    var $this = $(this);
    var valid = true;
    $('#formEditModel input').each(function() {
        let $this = $(this);

        if(!$this.val()) {
            valid = false;
//            $this.parents('.validate').find('.mySpan').text($this.attr('name').replace(/[\_]+/g, ' ') + ' ошибка в запросе');
            $this.parents('.validate').find('.mySpan').text('Поле пустое');
        }
    });

    if(valid){
        let data = $this.serialize();
        $.ajax({
            url: $this.attr("action"),
            type: "POST",
            data: data,
            dataType: "json",
            success: function(resp){
                $("#ModalEditModel").css('display','none');
                overlay.classList.remove('active');
                let new_value_model = $("#formEditModel input[name='model']").val();
                old_value_model.replaceWith('<td>'+new_value_model+'</td>');
            },
            error: function(resp){
                alert("Что-то пошло не так при редактировании");
            }
        });
    }
    return false;
});


//======================================================================================================================

$(".js-create-brand-model").on("click", function(e){
    overlay.classList.add('active');
    $("#ModalCreateBrandAndMark").css('display','block');
    return false;
});

var old_value_brand;
var old_value_model;
//var old_id_model;


//var old_value_brand;
$("#table tbody").on("click", ".BthEditBrandAndModel", function(e){
    e.preventDefault();
    var $this = $(this);
    let id_brand = $this.parents(".record").find('td').eq(0).attr('id');
    old_value_brand =  $this.parents(".record").find('td').eq(0);
//    alert(old_value_brand);
    let id_model = $this.parents(".record").find('td').eq(1).attr('id');
    old_value_model =  $this.parents(".record").find('td').eq(1);
    $("#formEditBrandAndModel select[name='id_brand']").val(id_brand);
    $("#formEditBrandAndModel select[name='id_model']").val(id_model);
    $("#formEditBrandAndModel").attr("action", $this.attr("href"));
    overlay.classList.add('active');
    $("#ModalEditBrandAndModel").css('display','block');
    return false;
});


$("#formEditBrandAndModel").on("submit", function(e){
    e.preventDefault();
    e.stopPropagation();
    var $this = $(this);
    let data = $this.serialize();
    $.ajax({
        url: $this.attr("action"),
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp){
            $("#ModalEditBrandAndModel").css('display','none');
            overlay.classList.remove('active');
            let new_value_id_brand = $("#formEditBrandAndModel select[name='id_brand']").val();
            let new_value_id_model = $("#formEditBrandAndModel select[name='id_model']").val();

            let new_text_brand = $("#formEditBrandAndModel select[name='id_brand'] option[value='"+new_value_id_brand+"']").text();

            let new_text_model = $("#formEditBrandAndModel select[name='id_model'] option[value='"+new_value_id_model+"']").text();

            old_value_brand.replaceWith('<td id='+new_value_id_brand+'>' + new_text_brand + '</td>');
            old_value_model.replaceWith('<td id='+new_value_id_model+'>' + new_text_model  + '</td>');
        },
        error: function(resp){
            alert("Что-то пошло не так при редактировании");
        }
    });

    return false;
});