
$(function (){


    $.ajax({
        type:'GET',
        url:'/send_json_to_web',
        success: function(orders){
            $.each(orders, function (i,order){
                $("#orders").append('<li>name: '+ order.name+', drink: '+ order.drink +' </li>');
            });
        },
        error:function () {
            alert('error loading orders');
        }
    });

});