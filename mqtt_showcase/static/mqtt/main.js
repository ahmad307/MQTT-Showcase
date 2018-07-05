
// Prevent page from reloading upon submission of connection form
    $('#connection_form').on('submit', function (event) {
        event.preventDefault();

        // Send POST request if the user wants to connect
        if ($('#connect_btn').text() === 'Connect'){
            var frm = $('#connection_form');
            post_connect(frm);
        } else {
            post_disconnect();
            $('#connect_btn').text('Connect');
            $('#connection_result').text('');
        }
    });

    $('#publish_form').on('submit', function (event) {
        event.preventDefault();

        if ($('#message').val().length !== 0 && $('#topic').val().length !== 0){
            var frm = $('#publish_form');
            post_connect(frm);
            get_messages();
        } else {
            window.alert('Enter valid Topic and Message.')
        }

    });

    $('#subscribe_form').on('submit', function (event) {
        event.preventDefault();
        var frm = $('#subscribe_form');
        post_connect(frm);
        window.alert('Topic Subscribed');
    })

    // Send POST request to the server with given form's data
    //  to begin/publish MQTT connection/topic
    function post_connect(frm) {
        $.ajax({
            url: '/ajaxconnect/',
            type:'POST',
            data:frm.serialize(),

            success: function (json) {
                // Prompt the user if he's trying to publish without connection
                if (json['message'] === 'Not Connected'){
                    window.alert('Please Connect First');
                // Change connect button value if connection was established
                } else if(document.activeElement.getAttribute('value') === 'connect') {
                    console.log('Ajax Connection success');
                    var pressed = document.getElementById('connect_btn');
                    $('#connect_btn').text('Disconnect');
                    $('#connection_result').text('Connected');
                }
            },
            error: function (xhr,errmsg,err) {
                console.log('Ajax Connection Fail');
            }
        });
    }

    // Send POST request to the server to end MQTT connection
    function post_disconnect() {
        $.ajax({
            url: '/ajaxdisconnect/',
            type: 'POST',
            data: {csrfmiddlewaretoken:'{{ csrf_token }}'},

            success: function () {
                console.log('Ajax Disconnection Success');
            },
            error: function () {
                console.log('Ajax Disconnection Fail');
            }
        });
    }

    function get_messages() {
        $.get("/get/", function (data, status) {
            var size = data['messages'].length;
            var item = data['messages'][size - 1];
            $('#messages_list').prepend("<li>" + item + "</li>");
            /*for (var i=0;i<data['messages'].length;i++){
                var item = data['messages'][i];
                $('#messages_list').prepend("<li>" + item + "</li>");
            }*/
        });
    }