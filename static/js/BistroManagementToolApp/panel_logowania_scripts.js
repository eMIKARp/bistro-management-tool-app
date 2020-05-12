// Wciśnięcie przycisku z userem lub wybranie
// opcji z userem na mniejszym ekranie spowoduje
// przypisanie wybranego usera do pola username formularza

  $("#clear").click(function() {
        document.body.requestFullscreen();
        console.log("check");
    })



$(".users-list").change(function () {
    $('#username_field').val(($(this).val()))
})

$(".users-container").on('click',"[id^=u_]",function () {
    $("[class^='user-tile']").css('background-color','yellowgreen')
    $(this).css('background-color','orange')
    $(this).children().css('background-color','orange')
    $('#username_field').val($(this).data("username"))
})

$(".keyboard-container").on('click',"[id^=d]",function () {
    $('#password_field').val($('#password_field').val().concat($(this).text()))
})

$(".keyboard-container").on('click',"[id^=backspace]",function () {
    $('#password_field').val($('#password_field').val().substring(0,$('#password_field').val().length-1))
})

$(".keyboard-container").on('click',"[id^=clear]",function () {
    $('#password_field').val(null)
})

$(".keyboard-container").on('click',"[id^=ok]",function () {
    $('#login_form').submit()
})