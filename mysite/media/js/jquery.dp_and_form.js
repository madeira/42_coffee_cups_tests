$(function() {
	$('#id_date').datepick({dateFormat: 'yyyy-mm-dd'});
});
function showDate(date) {
	alert('The date chosen is ' + date);
}
$(document).ready(function(){
    var options = {
        dataType: 'json',
            beforeSubmit: function(){
                $.blockUI({message: "loading data"});
            },
            success: function(response){
                setTimeout($.unblockUI, 4000);
                
                if (response.status=="valid")
                {
                    $('#form').html(response.text);
                    $('#message_valid').show()                    
                    $('#message_valid').hide(4000);                    
                }
                else
                {
                    $('#form').html(response.text);
                    $('#message_invalid').show()                    
                    $('#message_invalid').hide(4000);
                }
                $('#id_date').datepick({dateFormat: 'yyyy-mm-dd'});
            }
    };
    $("#myForm").ajaxForm(options);
});
