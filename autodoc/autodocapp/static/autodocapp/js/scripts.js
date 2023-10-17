
var overlay = document.querySelector('#overlay-modal');

var old_value_mark;

$(".js-create").on("click", function(e){
    overlay.classList.add('active');
    $(".modal-create").css('display','block');
    return false;
});

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

$("#formEditModel").on("submit", function(e){
    e.preventDefault();
    e.stopPropagation();
    var $this = $(this);
    var valid = true;
    $('#formEditModel input').each(function() {
        let $this = $(this);

        if(!$this.val()) {
            valid = false;
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

var old_value_brand;
var old_value_model;

//var old_value_brand;
$("#table tbody").on("click", ".BthEditBrandAndModel", function(e){
    e.preventDefault();
    var $this = $(this);
    let id_brand = $this.parents(".record").find('td').eq(0).attr('id');
    old_value_brand =  $this.parents(".record").find('td').eq(0);
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


var old_value_city;
$("#table tbody").on("click", ".BthEditCity", function(e){
    e.preventDefault();
    var $this = $(this);
    let name_city = $this.parents(".record").find('td').eq(0).text();
    old_value_city =  $this.parents(".record").find('td').eq(0);
    $("#formEditCity input[name='city']").val(name_city);
    $("#formEditCity").attr("action", $this.attr("href"));
    overlay.classList.add('active');
    $("#ModalEditCity").css('display','block');
    return false;
});

$("#formEditCity").on("submit", function(e){
    e.preventDefault();
    e.stopPropagation();
    var $this = $(this);
    var valid = true;
    $('#formEditCity input').each(function() {
        let $this = $(this);

        if(!$this.val()) {
            valid = false;
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
                $("#ModalEditCity").css('display','none');
                overlay.classList.remove('active');
                let new_value_city = $("#formEditCity input[name='city']").val();
                old_value_city.replaceWith('<td>'+new_value_city+'</td>');
            },
            error: function(resp){
                alert("Что-то пошло не так при редактировании");
            }
        });
    }
    return false;
});

//======================================================================================================================
var old_value_street;
$("#table tbody").on("click", ".BthEditStreet", function(e){
    e.preventDefault();
    var $this = $(this);
    let name_street = $this.parents(".record").find('td').eq(0).text();
    old_value_street =  $this.parents(".record").find('td').eq(0);
    $("#formEditStreet input[name='street']").val(name_street);
    $("#formEditStreet").attr("action", $this.attr("href"));
    overlay.classList.add('active');
    $("#ModalEditStreet").css('display','block');
    return false;
});

$("#formEditStreet").on("submit", function(e){
    e.preventDefault();
    e.stopPropagation();
    var $this = $(this);
    var valid = true;
    $('#formEditStreet input').each(function() {
        let $this = $(this);

        if(!$this.val()) {
            valid = false;
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
                $("#ModalEditStreet").css('display','none');
                overlay.classList.remove('active');
                let new_value_street = $("#formEditStreet input[name='street']").val();
                old_value_street.replaceWith('<td>'+new_value_street+'</td>');
            },
            error: function(resp){
                alert("Что-то пошло не так при редактировании");
            }
        });
    }
    return false;
});

//==========================================================================================================================

var old_value_manufacturer;
$("#table tbody").on("click", ".BthEditManufacturer", function(e){
    e.preventDefault();
    var $this = $(this);
    let name_manufacturer = $this.parents(".record").find('td').eq(0).text();
    old_value_manufacturer =  $this.parents(".record").find('td').eq(0);
    $("#formEditManufacturer input[name='manufacturer']").val(name_manufacturer);
    $("#formEditManufacturer").attr("action", $this.attr("href"));
    overlay.classList.add('active');
    $("#ModalEditManufacturer").css('display','block');
    return false;
});

$("#formEditManufacturer").on("submit", function(e){
    e.preventDefault();
    e.stopPropagation();
    var $this = $(this);
    var valid = true;
    $('#formEditManufacturer input').each(function() {
        let $this = $(this);

        if(!$this.val()) {
            valid = false;
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
                $("#ModalEditManufacturer").css('display','none');
                overlay.classList.remove('active');
                let new_value_manufacturer = $("#formEditManufacturer input[name='manufacturer']").val();
                old_value_manufacturer.replaceWith('<td>'+new_value_manufacturer+'</td>');
            },
            error: function(resp){
                alert("Что-то пошло не так при редактировании");
            }
        });
    }
    return false;
});


//================================================================================================================================================================

var old_value_street;
var old_value_city;
var old_value_house;
var old_value_telephone;

$("#table tbody").on("click", ".BthEditShop", function(e){
    e.preventDefault();
    var $this = $(this);

    let id_city = $this.parents(".record").find('td').eq(0).attr('id');
    old_value_city = $this.parents(".record").find('td').eq(0);

    let id_street = $this.parents(".record").find('td').eq(1).attr('id');
    old_value_street = $this.parents(".record").find('td').eq(1);

    let house = $this.parents(".record").find('td').eq(2).text();
    old_value_house =  $this.parents(".record").find('td').eq(2);

    let telephone = $this.parents(".record").find('td').eq(3).text();
    old_value_telephone =  $this.parents(".record").find('td').eq(3);

    $("#formEditShop select[name='id_city']").val(id_city);
    $("#formEditShop select[name='id_street']").val(id_street);
    $("#formEditShop input[name='house']").val(house);
    $("#formEditShop input[name='telephone']").val(telephone);

    $("#formEditShop").attr("action", $this.attr("href"));
    overlay.classList.add('active');
    $("#ModalEditShop").css('display','block');
    return false;
});

$("#formEditShop").on("submit", function(e){
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
            $("#ModalEditShop").css('display','none');
            overlay.classList.remove('active');

            let new_value_id_city = $("#formEditShop select[name='id_city']").val();
            let new_value_id_street = $("#formEditShop select[name='id_street']").val();
            let new_value_house = $("#formEditShop input[name='house']").val();
            let new_value_telephone = $("#formEditShop input[name='telephone']").val();


            let new_text_city = $("#formEditShop select[name='id_city'] option[value='" + new_value_id_city+"']").text();

            let new_text_street = $("#formEditShop select[name='id_street'] option[value='" + new_value_id_street+"']").text();


            old_value_city.replaceWith('<td id='+new_value_id_city+'>' + new_text_city + '</td>');
            old_value_street.replaceWith('<td id='+new_value_id_street+'>' + new_text_street  + '</td>');
            old_value_house.replaceWith('<td>'+new_value_house+'</td>');
            old_value_telephone.replaceWith('<td>'+new_value_telephone+'</td>');



        },
        error: function(resp){
            alert("Что-то пошло не так при редактировании");
        }
    });

    return false;
});