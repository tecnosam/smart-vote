// (esversion: 6)

var socket = io();

socket.on('connect', function() {
    if (meeting_id > 0) {
        socket.emit( "join", { meeting_id: meeting_id } )
    }
    console.log( "Connected..." );
} );

socket.on( 'disconnect', function() {
    console.log( "Disconnected..." );
} );

socket.on( 'message', function(data) {
    console.log( data )
} )

socket.on("add-vote", function( vote ) {
    // console.log("duck")
    if ( vote.id != 0 ) {
        console.log(vote);
        let n_votes = $(`#option-${vote.oid}-votes`);

        n_votes.html( Number( n_votes.html() )+1 );

    }   
})

