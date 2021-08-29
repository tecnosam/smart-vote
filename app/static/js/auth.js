async function login( email, pwd ) {
    email = email === null ? document.getElementById('login-email').value : email;
}

async function signup ( name = null, email = null, pwd = null ) {
    name = name===null ? $('#signup-name').val() : name;
    email = email===null ? $('#signup-email').val() : email;
    pwd = pwd===null ? $('#signup-pass').val() : pwd;
    // console.log( name, email, pwd )

    const btnVal = $('#main-form .asyncTrigger').val();

    $('#main-form .asyncTrigger').val("Loading...");

    await $.ajax({

        url: "/users",
        type: "POST",
        data: { name: name, email: email, pwd: pwd },
        success: function( data ) {

            if ( data !== null ) {
                window.location.href = "/";
            } else {
                alert( "Invalid Authentication details" )
            }

        },
        error: function ( err ) {
            console.log( err );

            alert( err.responseText );
            $('#main-form .asyncTrigger').val( btnVal );
        }

    });


}
