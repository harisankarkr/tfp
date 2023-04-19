// user profile sub nav toggle 
// ------------------------------------------------------------

$(document).ready(function(){

    // manage account
    $('.man-ac').show();
    $("#user-btn1").click(function(){
      $('.rel-box').hide();
      $('.his-tabel').hide();  
      $(".man-ac").show(500);
    });

    // your orders
    $('.rel-box').hide();
    $("#user-btn2").click(function(){
      $('.man-ac').hide();
      $('.his-tabel').hide();  
      $(".rel-box").show(500);
    });

    // purchase history
    $('.his-tabel').hide();
    $("#user-btn3").click(function(){
      $('.man-ac').hide();
      $('.rel-box').hide();
      $(".his-tabel").show(500);
    });

    // edit address
    $('#edit-ad').hide();
    $("#ed-ad-btn").click(function(){
        $('#edit-ad').show(500);
    })

    // save address
    $("#save-ad").click(function(){
        $('#edit-ad').hide(500);
    })

});

// ==============================================================================
// product delete congfo box

function confirmDelete(form) {
    var result = confirm("Are you sure you want to delete this product?");
    if (result) {
      // User clicked "OK" in the confirmation dialog, submit the form
      form.submit();
    }
    // Otherwise, do nothing (i.e. the form submission is cancelled)
  }
  

// ==============================================================================
// prd card image change

function changeImage(product_id, img) {
  // Get the source of the clicked image
  console.log(img); 
  var newSrc = img.src;
  
  // Get the main image element and update its source
  var mainImage = document.getElementById("mainImage" + product_id);
  console.log(mainImage); // add this line to check if mainImage is null
  mainImage.src = newSrc;
}

// ==================================================================================================================
// category 2 drop down

    function populateCategory2() {
        var category1Select = document.getElementById("category1");
        var category2Select = document.getElementById("category2");
        var selectedCategory1 = category1Select.options[category1Select.selectedIndex].value;
    
        // Clear the existing options
        category2Select.innerHTML = "";
    
        if (selectedCategory1 === "Men's Topwear") {
            var category2Options = ["T-shirts", "Casual shirts", "Formal shirts", "Jackets", "Sweatshirts & Hoodies", "Blazers & Coats"];
        } else if (selectedCategory1 === "Men's Bottomwear") {
            var category2Options = ["Jeans", "Casual Trousers", "Formal Trousers", "Shorts & 3/4ths", "Track pants & Joggers"];
        } else if (selectedCategory1 === "Women's Fusion Wear") {
            var category2Options = ["Gowns", "Pants & Shorts", "Jackets & Shrugs", "Tops", "Shirts & T-shirts", "Jeans"];
        } else if (selectedCategory1 === "Women's Ethnic Wear") {
            var category2Options = ["Kurthas", "Salwars & Churidars", "Skirts & Ghagras", "Sarees", "Dress materials", "Dupattas"];
        } else {
            var category2Options = [""];
        }
    
        // Add the new options
        for (var i = 0; i < category2Options.length; i++) {
            var option = document.createElement("option");
            option.text = category2Options[i];
            category2Select.add(option);
        }
    }


    // ================================================================================================
