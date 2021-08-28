// (esversion: 6)

var socket = io();

socket.on('connect', function() {
    console.log( "Connected..." );
} );

socket.on( 'disconnect', function() {
    console.log( "Disconnected..." );
} );

socket.on("add-vote", function( vote ) {
    // console.log("duck")
    if ( vote.id != 0 ) {
        console.log(vote);
        let n_votes = $(`#option-${vote.oid}-votes`);

        n_votes.html( Number( n_votes.html() )++ );

    }   
})

