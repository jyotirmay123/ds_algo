$(document).ready(function() {
    async function pushToDB(pos, log='Navigator Position') {
        $.getJSON('https://ipapi.co/json/', function (geodata) {

            const timeElapsed = Date.now();
            const today = new Date(timeElapsed);
            geodata.time = today.toUTCString();
            geodata.time_timezone = 'UTC';
            geodata.page='PMP';
            geodata.pos = pos;
            geodata.log = log;
            geodata.comment = '';
            console.log(geodata);

            actualPush(geodata)
        });
    }

    async function actualPush(geodata) {
        $.post( "https://jyotirmays-api.herokuapp.com/v1/insertJson", geodata, function( data ) {
            console.log(data);
        });
    }

    if (navigator.geolocation) {
        navigator.geolocation.watchPosition(
            pushToDB,
            (error) => {
                if (error.code === error.PERMISSION_DENIED) {
                    // console.log("you denied me :-(");
                    pushToDB(null, 'Denied Me');
                } else {
                    pushToDB(null, 'Some Other Error!');
                }
            });
    } else {
        pushToDB(null, 'No Navigator');
    }
});
