

async function edit_prof() {

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
            $('#polls').prepend( cast_poll( poll ) );
            $( '#add-poll-tag' ).val("");
            $( '#add-poll-desc' ).val("");
        },
        error: function ( err ) {
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