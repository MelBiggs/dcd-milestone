$(document).ready(function(){
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown();
    $('select').formSelect();



    $("#add-ingredient").on("click", function (e) {
        // Prevent Default stops the form being submitted after this button is clicked 
        e.preventDefault();  

        $('select').formSelect('destroy');
        $(".ingredient-list-item:last").clone().find("input:text").val("").end().prependTo(this);
        $('select').formSelect();
        
    });

    $('.remove-ingredient').on("click", function (e) {
        e.preventDefault();
        console.log('clddicjd');
    });
});