$("#login-form").validate({
    rules:{
        userName: {
            required:true,
            text:true,
        },
        password: {
            required:true,
            minlength:4
        }
    },

    submitHandler: function(form){
        form.submit();
    }
});