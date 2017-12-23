$("[data-toggle=popover]").each(function() {

$(this).popover({
  html: true,
  content: function() {
    var id = $(this).attr('id')
    return $('#popover-content-' + id).html();
  }
})
.on('shown.bs.popover', function(){
    $(".onoffswitch-label").off("click","**").click( function(){
        if( ! ($(this).parent().hasClass("switch-disabled")) )
          {
            var sw = $(this).parent().find("input"); 
            var sv = sw.val(); 
            if( sv=="on" ) sw.val("off");
            else sw.val("on");
            $(this).parent().toggleClass("switchON switchOFF");
          }
        });
   });
});

$('body').on('click', function (e) {
    $('.offFocus').each(function () {
        if (!$(this).is(e.target) && $(this).has(e.target).length === 0 && $('.popover').has(e.target).length === 0) {
            $(this).popover('hide');
        }
    });
});

$(".onoffswitch-label").click( function(){
        var sw = $(this).parent().find("input"); 
        var sv = sw.val(); 
        if( sv=="on" ) sw.val("off");
        else sw.val("on");
        $(this).parent().toggleClass("switchON switchOFF");
    });

function showMsg( message , duration = 5000 ){
        $(".alertBox")
            .html( message )
            .animate( {'right':'15px'} )
            .delay( duration )
            .animate( {'right':'-100%'} );
    }
