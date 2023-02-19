jQuery(function() {
    // …
    
    
    function registerUser(data){

        $.ajax({
            url: "https://api.sharksgambit.tech/register/new_user/",
            type: "POST",
            crossDomain: true,
            data: {
                username: data,
                CSRF: getCSRFTokenValue()
            },
            dataType: "json",
            success: function (response) {
                var resp = JSON.parse(response)
                alert(resp.status);
            },
            error: function (xhr, status) {
                alert("error");
            }
        });
            
        $.post("https://api.sharksgambit.tech/register/new_user/",
        {
            username: data[0]
        },
        function(data, status){
            alert("Data: " + data + "\nStatus: " + status);
        });
    }
    
    
    $('#register').on('submit',function(event){
        event.preventDefault();
        console.log('haha!',$(this).serializeArray())
        registerUser($(this).serializeArray()[0])
    });
  });
