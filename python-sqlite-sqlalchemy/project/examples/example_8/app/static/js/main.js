// jQuery handler for the page

let ns = {};

ns.model = (function() {
    return {

    };
}());

ns.view = (function() {
    let $add_category = $("#add-category-form"),
        $category_form = $("#add-category-form form"),
        $add_product = $("#add-product-form"),
        $product_form = $("#add-product-form form");

    return {
        init: function() {
            $add_category.hide();
            $add_product.hide();
        },
        show_form: function($selector) {
            $selector.show();
        },
        hide_form: function($selector) {
            $selector.hide();
        },
        update_new_category_form(category_name) {
            $("#add-category-form span").text(category_name);
        },
        update_new_product_form(category_name) {
            $("#add-product-form span").text(category_name);
        }
    };
}());

ns.controller = (function(m, v) {
    let model = m,
        view = v;

    // initialize the dislay
    view.init();

    // add handlers
    $("button.add-category").on("click", function(e) {
        let $this = $(this),
            $target = $(e.target),
            category_name,
            category_id,
            category_level;

        // set the form values from the selected category
        category_name = $target.text();
        category_id = $target.data("descendant-category-id");
        category_level = $target.data("descendant-level");

        view.show_form($("#add-category-form"));
        view.show_form($("#add-product-form"))
        view.update_new_category_form(category_name);
        view.update_new_product_form(category_name);

        // because both are shown, both have to be populated
        $("#add-category-form input.category-id").val(category_id),
        $("#add-category-form input.category-level").val(category_level);

        $("#add-product-form input.category-id").val(category_id),
        $("#add-product-form input.category-level").val(category_level);
    });

    $("button.add-product").on("click", function(e) {
        let $this = $(this),
            $target = $(e.target),
            category_name,
            category_id,
            category_level;

        // set the form values from the selected leaf category
        category_name = $target.text();
        category_id = $target.data("descendant-category-id");
        category_level = $target.data("descendant-level");

        view.hide_form($("#add-category-form"));
        view.show_form($("#add-product-form"));
        view.update_new_product_form(category_name);

        $("#add-product-form input.category-id").val(category_id),
        $("#add-product-form input.category-level").val(category_level);
    });

    $("button#new-category-submit").on("click", function(e) {
        e.preventDefault();
        $("#add-category-form form").submit();
    });

    $("button#new-product-submit").on("click", function(e) {
        e.preventDefault();
        $("#add-product-form form").submit();
    });

}(ns.model, ns.view));