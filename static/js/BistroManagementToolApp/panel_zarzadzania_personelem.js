// Checking if add ingredient window should be visible
// if true call showAddIngredientForm function

if (show_add_user_window == true){
    showAddUserForm();
}


// Hide form window and show error window
// for better error visibility


$('.form_fields_line').on('click','#add_user_show_errors',function () {

    $('#form_fields_area').toggleClass("form_fields_area_errors_hidden form_fields_area_errors_visible")
    $('#form_error_line').toggleClass("form_error_line_hidden form_error_line_visible")


    if ($('#add_user_show_errors').prop('value') == 'Pokaż błędy!'){
        $('#add_user_show_errors').prop('value','Ukryj błędy!')
    } else {
        $('#add_user_show_errors').prop('value','Pokaż błędy!')
    }

})


// Hides or partially hides panel with ingredients and
// replaces it with form through witch we can add new ingredient

function showAddUserForm(){

    if($("#user_form_2").css('display')=='none' && $("#user_form_3").css('display')=='none'){
        $("#user_form_1").toggleClass("user_form_hidden users_form_visible");
        $("#users_window").toggleClass("users_window_form_hidden users_window_form_visible");

        var ids = ["buttons","image","username","fullname","email","status","lastlogin","datecreated"]

        ids.forEach(function (id) {
            $("[id^=usr_"+id+"_]").toggleClass("usr_"+id+"_form_hidden usr_"+id+"_form_visible")
            $("#head_"+id).toggleClass("usr_"+id+"_form_hidden usr_"+id+"_form_visible")
        })

    }
}

function showManageEmployeeScheaduleForm(){
    if($("#user_form_1").css('display')=='none' && $("#user_form_3").css('display')=='none'){
       $("#user_form_2").toggleClass("user_form_hidden users_form_visible");
       $("#users_window").toggleClass("users_window_form_hidden users_window_form_visible");

       var ids = ["buttons","image","username","fullname","email","status","lastlogin","datecreated"]

       ids.forEach(function (id) {
           $("[id^=usr_" + id + "_]").toggleClass("usr_" + id + "_form_hidden usr_" + id + "_form_visible")
           $("#head_" + id).toggleClass("usr_" + id + "_form_hidden usr_" + id + "_form_visible")
       })
    }
}

function showEditUserForm() {
    if ($("#user_form_1").css('display') == 'none' && $("#user_form_2").css('display') == 'none') {
        $("#user_form_3").toggleClass("user_form_hidden users_form_visible");
        $("#users_window").toggleClass("users_window_form_hidden users_window_form_visible");

        var ids = ["buttons", "image", "username", "fullname", "email", "status", "lastlogin", "datecreated"]

        ids.forEach(function (id) {
            $("[id^=usr_" + id + "_]").toggleClass("usr_" + id + "_form_hidden usr_" + id + "_form_visible")
            $("#head_" + id).toggleClass("usr_" + id + "_form_hidden usr_" + id + "_form_visible")
        })
    }
}

$(".user_menu_panel").on("click","#user_menu_b1",showAddUserForm)
$(".user_menu_panel").on("click","#user_menu_b3",showManageEmployeeScheaduleForm)

// Remove selected user when user clicks on button
// Sends AJAX request to delete user from database

$("[id^=remove_user]").click(function(){
    var user_id = $(this).data('user_id')
    var ajax_request = $.ajax(
        'ajax/delete_user',
        {
            data:{'user_id':user_id},
            dataType:'json',
            success:function (data,status) {
             $('#usr_'+user_id).remove()
                console.log(data['status'])
            },
            error:function (data,status,error_desc){
                console.log(status+": "+error_desc)
            }
        }
    )

})

// Edit selected user when user clicks on button
// Sends AJAX request to retrieve selecded user from db

$("[id^=edit_user]").click(function(){
    var user_id = $(this).data('user_id')
    var ajax_request = $.ajax(
        'ajax/edit_user',
        {
            data:{'user_id':user_id},
            dataType:'json',
            success:function (data,status) {
                showEditUserForm()
            },
            error:function (data,status,error_desc){
                console.log('error')
            }
        }
    )

})