$(document).ready(function(){
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown();
    $('select').formSelect();



    $("#add-ingredient").on("click", function (e) {
        // Prevent Default stops the form being submitted after this button is clicked 
        e.preventDefault();  
        
        var newthing = $(".ingredient-list-item:last").clone();      
        newthing.insertBefore(this)
        newthing.find("input").val("");
    });

    $(document).on("click", ".remove-ingredients-btn", function (e) {
        e.preventDefault();  
        // If statement stops first field from being removed
        if($(document).find(".remove-ingredients-btn").length > 1){
            this.closest("div").remove();
        }
    });
});