// Checking if add ingredient window should be visible
// if true call showAddIngredientForm function

if (show_add_ingredient_window == true){
    showAddIngredientForm();
}


// Hide form window and show error window
// for better error visibility


$('.form_fields_line').on('click','#add_ingredient_show_errors',function () {

    $('#form_fields_area').toggleClass("form_fields_area_errors_hidden form_fields_area_errors_visible")
    $('#form_error_line').toggleClass("form_error_line_hidden form_error_line_visible")


    if ($('#add_ingredient_show_errors').prop('value') == 'Pokaż błędy!'){
        $('#add_ingredient_show_errors').prop('value','Ukryj błędy!')
    } else {
        $('#add_ingredient_show_errors').prop('value','Pokaż błędy!')
    }

})


// Hides or partially hides panel with ingredients and
// replaces it with form through witch we can add new ingredient

function showAddIngredientForm(){

    if($("#ingredient_form_2").css('display')=='none'){
        $("#ingredient_form_1").toggleClass("user_form_hidden ingredient_form_visible");
        $("#ingredient_window").toggleClass("users_window_form_hidden ingredient_window_form_visible");

        var ids = ["buttons","category","subcategory","aisle","name","unit","gramature","netto","vat","brutto","amount"]

        ids.forEach(function (id) {
            $("[id^=ing_"+id+"_]").toggleClass("ing_"+id+"_form_hidden ing_"+id+"_form_visible")
            $("#head_"+id).toggleClass("ing_"+id+"_form_hidden ing_"+id+"_form_visible")
        })

    }
}

function showAddShoppingForm(){
    if($("#ingredient_form_1").css('display')=='none'){
       $("#ingredient_form_2").toggleClass("user_form_hidden ingredient_form_visible");
       $("#ingredient_window").toggleClass("users_window_form_hidden ingredient_window_form_visible");

       var ids = ["buttons","category", "subcategory", "aisle", "name", "unit", "gramature", "netto", "vat", "brutto", "amount"]

       ids.forEach(function (id) {
           $("[id^=ing_" + id + "_]").toggleClass("ing_" + id + "_form_hidden ing_" + id + "_form_visible")
           $("#head_" + id).toggleClass("ing_" + id + "_form_hidden ing_" + id + "_form_visible")
       })
    }
}

$(".user_menu_panel").on("click","#ingredient_menu_b1",showAddIngredientForm)
$(".user_menu_panel").on("click","#ingredient_menu_b2",showAddShoppingForm)

// Send an AJAX request upon category change
// to retriew subcategory and aisle related to that category

$("#id_subcategory").change(function ()

{
    var selected_subcategory = $(this).find("option:selected").text()
    var ajax_request = $.ajax(
        'ajax/change_ing_subcategory',
        {
            data:{'selected_subcategory':selected_subcategory},
            dataType:'json',
            success:function (data,status) {

                $('#ingredient_aisle option').remove()

                data['corresponding_aisle'].forEach(function(item,index){
                    $('#ingredient_aisle select').append('<option value="'+index+'">'+item.name+'</option>')
                })
            },
            error:function(data,status,error_desc){
                console.log(status+": "+error_desc)
            }
        }
        )

})


// Send an AJAX request upon category change
// to retriew subcategory and aisle related to that category

$("#id_category").change(function ()

{
    var selected_category = $(this).find("option:selected").text()
    var ajax_request = $.ajax(
        'ajax/change_ing_category',
        {
            data:{'selected_category':selected_category},
            dataType:'json',
            success:function (data,status) {

                $('#ingredient_subcategory option').remove()
                $('#ingredient_aisle option').remove()

                data['corresponding_subcategories'].forEach(function(item,index){
                    $('#ingredient_subcategory select').append('<option value="'+index+'">'+item.name+'</option>')
                })

                data['corresponding_aisle'].forEach(function(item,index){
                    $('#ingredient_aisle select').append('<option value="'+index+'">'+item.name+'</option>')
                })
            },
            error:function(data,status,error_desc){
                console.log(status+": "+error_desc)
            }
        }
        )

})


// Remove ingredient when user clicks on button
// Sends AJAX request to delete ingredient from database

$("[id^=remove_ingredient]").click(function(){
    var ingredient_ext_id = $(this).data('ingredient_ext_id')
    var ajax_request = $.ajax(
        'ajax/delete_ingredient',
        {
            data:{'ingredient_ext_id':ingredient_ext_id},
            dataType:'json',
            success:function (data,status) {
             $('#ingredient_'+ingredient_ext_id).remove()
                console.log(data['status'])
            },
            error:function (data,status,error_desc){
                console.log(status+": "+error_desc)
            }
        }
    )

})

// Edit ingredient when user clicks on button
// ????
