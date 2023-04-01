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

