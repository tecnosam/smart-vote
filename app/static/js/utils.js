

async function edit_profile() {
    // edit profile

    let data = {};

    let btnVal = $('#epf .asyncTrigger').html();
    $('#epf .asyncTrigger').html(`<i style="color:black" class='fas fa-spinner fa-spin'></i>`);

    for ( let inp of $('#epf input') ) {
        if ( !inp.value.length ) {
            continue;
        }

        data[ inp.name ] = inp.value;

    }

    await $.ajax({
        url: `/users/${uid}`,
        type: "PUT",
        data: data,
        success: function(data) {
            alert("Profile has been updated")
        },

        error: function( err ) {
            console.log( err.responseText );
            alert( err.responseText );
        }

    });

    $('#epf .asyncTrigger').html( btnVal );

}

async function add_poll(  ) {
    let tag = $( '#add-poll-tag' ).val();
    let desc = $( '#add-poll-desc' ).val();

    await $.ajax({
        url: `/meetings/${meeting_id}/polls`,
        type: "POST",
        data: { tag: tag, desc: desc },
        success: function( poll ) {
            $('#polls').prepend( 
                `<div id="poll-${poll.id}" class="col-lg-6 mb-4">
                    ${cast_poll( poll )}
                </div>`
            );
            $( '#add-poll-tag' ).val("");
            $( '#add-poll-desc' ).val("");
        },
        error: function ( err ) {
            alert( err.responseText );
        }
    })
}

async function edit_poll( pid ) {

    let tag = $(`#edit-poll-${pid}-tag`).val();
    let desc = $(`#edit-poll-${pid}-desc`).val();

    let btnVal = $(`#edit-poll-${pid} .asyncTrigger`).html();

    $(`#edit-poll-${pid} .asyncTrigger`).html(`<i style="color:black" class='fas fa-spinner fa-spin'></i>`);


    await $.ajax({
        url: `/meetings/polls/${pid}`,
        type: "PUT",
        data: { tag: tag, desc: desc },

        success: function ( poll ) {

            alert( "Successfully editted poll" );

            $(`#poll-${pid}`).html( cast_poll( poll ) );

            // clean up modal residue
            $('body').removeClass( 'modal-open' );
            $('.modal-backdrop').remove();

        },

        error: function( err ) {
            alert( err.responseText );
        }

    });

    $( `#edit-poll-${pid} .asyncTrigger` ).html( btnVal );

}

async function delete_poll( pid ) { 
    if ( !confirm( "Are you sure you want to delete this poll?!" ) ) {
        return ;
    }

    $.ajax({
        url: `/meetings/polls/${pid}`,
        type: "DELETE",
        success: function( poll ) {
            alert(`Poll ${poll.tag} has been deleted successfully`);

            $(`#poll-${poll.id}`).remove();

            // clean up modal residue
            $('body').removeClass( 'modal-open' );
            $('.modal-backdrop').remove();
        },
        error: function( err ) {
            alert( err.responseText );
        }

    });
 }

async function add_option( pid ) {
    let tag = $(`#add-option-${pid}-tag`).val();
    let desc = $(`#add-option-${pid}-desc`).val();
    let btn = $(`#add-option-${pid} .asyncTrigger`);

    let btnVal = btn.html();

    btn.html( `<i style="color:black" class='fas fa-spinner fa-spin'></i>` );

    await $.ajax({
        url: `/polls/${pid}/options`,
        type: "POST",
        data: { tag: tag, desc: desc },
        success: function ( option ) {

            alert("successfully added option");
            $(`#poll-${pid}-options`).append( cast_option( option ) );

            $(`#add-option-${pid}`).modal("hide");

        },
        error: function ( err ) {
            alert( err.responseText )
        }
    })

    btn.html( btnVal );

}

async function delete_option( oid ) {

    if ( !confirm( "Are you sure you want to delete this option" ) ) {
        return ;
    }

    await $.ajax({
        url: `/polls/options/${ oid }`,
        type: "DELETE",
        success: function( option ) {
            alert( `successfully deleted option ${option.tag}` );

            $(`#option-${option.id}`).remove()
        },
        error: function( err ) {
            alert( err.responseText );
        }
    })

}

async function add_meeting(  ) {
    let tag = $( '#cm-tag' ).val();

    await $.ajax({
        url: `/users/${uid}/meetings?tag=${tag}`,
        type: "POST",
        success: function( data ) {
            // $('#meetings').prepend( cast_meeting( data ) )
            window.location.href = "";
        }
    })
}

async function change_meeting_tag( meeting_id, old_tag ) {

    new_tag = prompt( "Input a new tag for your meeting form", old_tag );

    if ( new_tag == null ) {
        return;
    }

    await $.ajax({
        url: `/meetings/${meeting_id}?tag=${new_tag}`,
        type: "PUT",
        success: function ( meeting ) {
            alert(`Tag changed to ${meeting.tag}`);
            $(`.meeting-${meeting.id}-tag`).html( meeting.tag )
        },
        error: function ( err ) {
            alert( err.responseText );
        }
    });
}

async function delete_meeting( meeting_id ) {
    if ( !confirm("Are you sure you want to delete this meeting form") ) {
        return;
    }

    await $.ajax({
        url: `/meetings/${meeting_id}`,
        type: "DELETE",
        success: function ( meeting ) {
            alert( `Meeting ${meeting.tag} has been deleted successfully` );

            $(`#meeting-${meeting_id}`).remove();

            // clean up modal residue
            $('body').removeClass( 'modal-open' );
            $('.modal-backdrop').remove();
        },
        error: function( err ) {
            alert( err.responseText );
        }
    })
}

async function meeting_import_members () {}

async function delete_member( mid ) {

    if ( ! confirm( "Are you sure you want to delete this member" ) ) {
        return;
    }

    await $.ajax( {
        url: `/meetings/members/${mid}`,
        type: "DELETE",
        success: function ( member ) {
            alert(`member ${member.name} deleted successfully`);
            $( `#member-${member.id}` ).remove();
        },
        error: function ( err ) {
            alert( err.responseText );
        }
    });
}