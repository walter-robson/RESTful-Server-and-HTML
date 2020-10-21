// respond to button click
console.log("Page load happened!")

send_button = document.getElementById("send-button");
send_button.onmouseup = makeRequest;

function makeRequest(){
    console.log("Entered get Form Info!")
    // get text from title, author and story

    var port = document.getElementById('input-port-number').value;
    
    var key = null;
    if (document.getElementById('checkbox-use-key').checked){
        key = document.getElementById('input-key').value;
    }
    var message_body = null;
    if (document.getElementById('checkbox-use-message').checked){
        // get key value
        message_body = document.getElementById('text-message-body').value;
    }
    
    var selindex = document.getElementById('select-server-address').selectedIndex;
    var url_base = document.getElementById('select-server-address').options[selindex].value;
    var action = "GET"; // default
    if (document.getElementById('radio-get').checked){
            action = "GET";
    } else if (document.getElementById('radio-put').checked) {
            action = "PUT";
    } else if (document.getElementById('radio-post').checked) {
            action = "POST";
    } else if (document.getElementById('radio-delete').checked) {
            action = "DELETE";
    }

    


};



