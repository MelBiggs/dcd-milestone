$(document).ready(function(){
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown();
    $('select').formSelect();



    $("#add-ingredient").on("click", function (e) {
        // Prevent Default stops the form being submitted after this button is clicked 
        e.preventDefault();  
        
        var newIngredient = $(".ingredient-list-item:first").clone();      
        newIngredient.insertBefore(this)
        newIngredient.find("input").val("");
        $("<a>").insertAfter(newIngredient.find("input")).attr("class","remove-btn").text("remove");
    });

    $("#add-step").on("click", function (e) {
        // Prevent Default stops the form being submitted after this button is clicked 
        e.preventDefault();  
        
        var newStep = $(".step-list-item:first").clone();      
        newStep.insertBefore(this)
        newStep.find("input").val("");
        $("<a>").insertAfter(newStep.find("input")).attr("class","remove-btn").text("remove");
    });

    // Remove button for forms 

    $(document).on("click", ".remove-btn", function (e) {
        e.preventDefault();  
        this.closest("div").remove();
    });

});