jQuery(function() {
    // …
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    
    function registerUser(data){
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            url: "https://api.sharksgambit.tech/register/new_user/",
            type: "POST",
            headers: {'X-CSRFToken': csrftoken},
            mode: 'same-origin', // Do not send CSRF token to another domain.
            crossDomain: true,
            data: {
                user_name: data
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
