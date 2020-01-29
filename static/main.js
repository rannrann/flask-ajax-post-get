
$(function (){
    var $orders = $('#orders');
    var $name = $('#name');
    var $drink = $('#drink');

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

    $('#add-order').on('click', function(){
       var order = {
           'name':$name.val(),
           'drink':$drink.val(),
       };

       $.ajax({
           type:'POST',
           url:'/receive_json_from_web',
           data:JSON.stringify(order),
           success:function (newOrder) {
                $("#orders").append('<li>name: '+ newOrder.name+', drink: '+ newOrder.drink +' </li>');
           }
       });
    });
});