$(document).ready( function() {
    $(".sign-in").on("click", function() {
        $(".modal-body").load("/accounts/login");
        //start
        $(document).on('submit','form',function(e){
        e.preventDefault();
        $.ajax({
            type:'POST',
            url:'/accounts/login/',
            data:
            {
                username:$("#id_username").val(),
                password:$("#id_password").val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(resultData){
                  if(String(resultData).includes('Profile')){
                    window.location.replace("/profile");
                  }else{
                  $(".modal-body").html(resultData)
                    }
                  }

            })
        });
        //end
    });
    $(".sign-up").on("click", function() {
        $(".modal-body").load("/accounts/signup");
        //start
        $(document).on('submit','form',function(e){
        e.preventDefault();
        $.ajax({
            type:'POST',
            url:'/accounts/signup/',
            data:
            {
                username:$("#id_username").val(),
                password1:$("#id_password1").val(),
                password2:$("#id_password2").val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(resultData){
                if(String(resultData).includes('Profile')){
                    window.location.replace("/profile");
                  }else{
                  $(".modal-body").html(resultData)
                    }
                    }
            })
        });
        //end
    });
});
if(window.location.pathname==='/accounts/login/' || window.location.pathname==='/accounts/signup/'){
    window.location.replace("/");
}