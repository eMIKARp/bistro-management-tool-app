

// Unhide products from first category

$('button[class="product_item '+$(".group_item")[0].id+'"]').css("display","inherit")


function calculate_total_transaction_value(){
    var total_transaction_value = 0
    $(".transaction_item").each(function () {
    total_transaction_value = total_transaction_value + parseFloat($(this).find('p[id="total_value"]').text())
    })
    $('div[id="summary_amount"]').text(total_transaction_value)
}

// Display products from product group
// chosen by user

$(".group_item").click(
    function() {
        $(".product_item").css("display","none")
        $("."+$(this).attr("id")).css("display","inherit")
    });

// Add product chosen by user to transaction list
// and updates total transaction value

$(".product_item").click(
    function() {
        var chosen_product = $(this).data('product_ext_id')


        // If at least one unit of product is on transaction list
        // update number of units on transaction list

        if ($('div[id="' + chosen_product + '"]').length) {
            var initial_quantity = parseInt($('div[id="' + chosen_product + '"]').find('p[id="ilosc"]').text())
            var brutto_price = parseFloat($('div[id="' + chosen_product + '"]').find('p[id="cena_brutto"]').text())
            var new_quantity = initial_quantity + 1
            var total_value = new_quantity * brutto_price
            $('div[id="' + chosen_product + '"]').find('p[id="ilosc"]').text(new_quantity)
            $('div[id="' + chosen_product + '"]').find('p[id="total_value"]').text(total_value)

        // else add product to the transaction list

        } else {
            $(".transction_window_main").append("" +
                "<div id='" + $(this).data('product_ext_id') + "' class='transaction_item'>" +
                    "<div id='buttons'>" +
                        "<button id='remove_unit' style='color:white;height: 50%;background-color:DarkOliveGreen'><i class='fas fa-minus'></i></button>"+
                        "<button id='remove_product' style='color:white;height: 50%;background-color:DarkOliveGreen'><i class='fas fa-trash-alt'></i></button>" +
                    "</div>"+
                    "<p id='nazwa'>" + $(this).data('product_name') + "</p>" +
                    "<p id='ilosc'>1</p>" +
                    "<p id='cena_brutto'>" + $(this).data("product_brutto_price") + "</p>" +
                    "<p id='total_value'>" + $(this).data("product_brutto_price") + "</p>" +
                "</div>")
            var total_value = parseFloat($(this).data("product_brutto_price"))
        }

        // Update total transaction value

        calculate_total_transaction_value()
    }
)

// Removes product chosen by user from transaction list
// and updates total transaction value

$('.transction_window_main').on("click","#remove_product",function () {
    $(this).parent().parent().remove()
    calculate_total_transaction_value()
})

// Removes unit chosen by user from transaction list
// and updates total transaction value

$('.transction_window_main').on("click","#remove_unit",function () {
    var current_quantity = parseInt($(this).parent().parent().find('p[id="ilosc"]').text())
    if (current_quantity == 1){
         $(this).parent().parent().remove()
    } else {
    var brutto_price = parseInt($(this).parent().parent().find('p[id="cena_brutto"]').text())
    var new_quantity = current_quantity-1
    $(this).parent().parent().find('p[id="ilosc"]').text(new_quantity)
    $(this).parent().parent().find('p[id="total_value"]').text(new_quantity*brutto_price)

    }
    calculate_total_transaction_value()
})



// Hides or partially hides panel with ingredients and
// replaces it with form through witch we can add new ingredient


$(".user_menu_panel").on("click","ingredient_menu_b1",function(){

    $(".ingredient_window").css("display","none")
    $(".ingredient_form").css("display","flex")

    consloe.log("Udalo sie!")

})


// Send an AJAX request upon category change
// to retriew subcategory and aisle related to that category

