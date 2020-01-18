$(document).ready(function(){
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown();
    $('select').formSelect();



    $("#add-ingredient").on("click", function (e) {
        // Prevent Default stops the form being submitted after this button is clicked 
        e.preventDefault();  
        
        var newthing = $(".ingredient-list-item:first").clone();      
        newthing.insertBefore(this)
        newthing.find("input").val("");
        $("<a>").insertAfter(newthing.find("input")).attr("class","remove-btn").text("remove");
    });

    $(document).on("click", ".remove-btn", function (e) {
        e.preventDefault();  
        this.closest("div").remove();
    });

    $("#add-step").on("click", function (e) {
        // Prevent Default stops the form being submitted after this button is clicked 
        e.preventDefault();  
        
        var newthing = $(".step-list-item:first").clone();      
        newthing.insertBefore(this)
        newthing.find("input").val("");
        $("<a>").insertAfter(newthing.find("input")).attr("class","remove-btn").text("remove");
    });
});