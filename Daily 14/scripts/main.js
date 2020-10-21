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

    console.log('Beginning to make nw call' + name);
    // set up url
    var xhr = new XMLHttpRequest(); // 1 - creating request object
    var url = null;
    if(key != null){
        url = url_base + ':' + port + '/' + key + '/' + message_body;
    } else {
        var url = url_base + ':' + port + '/' + message_body;
    }
    
    xhr.open(action, url, true); // 2 - associates request attributes with xhr

    // set up onload
    xhr.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhr.responseText);
        // do something
        updateResponse(xhr.responseText);
    }

    // set up onerror
    xhr.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhr.statusText);
    }

    // actually make the network call
    xhr.send(null) // last step - this actually makes the request



};

function updateResponse(response){
        var response_label = document.getElementById('response-label');
        response_label.innerHTML = response;

        var response_json = JSON.parse(response);

        var answer_label = document.getElementById('answer-label');
        answer_label.innerHTML = response_json['title'] + " belongs to the genres " + response_json['genres'];
};



