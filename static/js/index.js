$(document).ready(function () {
    $('.datepicker').datepicker();
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown();
    $('select').formSelect();
    $('.modal').modal({
        onOpenStart: function (modal, trigger) {
            $('#delete-link').attr("href", trigger.dataset.recipeDeleteUrl);
        }
    });

    $("#add-ingredient").on("click", function (e) {
        // Prevent Default stops the form being submitted after this button is clicked 
        e.preventDefault();

        var newIngredient = $(".ingredient-list-item:first").clone();
        newIngredient.insertBefore(this);
        newIngredient.find("input").val("");
        $("<a>").insertAfter(newIngredient.find("input")).attr("class", "remove-btn").text("Remove Line");
    });

    $("#add-step").on("click", function (e) {
        // Prevent Default stops the form being submitted after this button is clicked 
        e.preventDefault();

        var newStep = $(".step-list-item:first").clone();
        newStep.insertBefore(this);
        newStep.find("input").val("");
        $("<a>").insertAfter(newStep.find("input")).attr("class", "remove-btn").text("Remove Line");
    });

    // Remove button for forms 

    $(document).on("click", ".remove-btn", function (e) {
        e.preventDefault();
        this.closest("div").remove();
    });
});