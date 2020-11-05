// respond to button click
console.log("Page load happened!")

send_button = document.getElementById("new-submit-button");
send_button.onmouseup = makeRequest1;

function makeRequest1(){
    console.log("Entered Add!")
    // get text from title, author and story
    const url_base = 'http://student04.cse.nd.edu';
    const port = '51086';

    var name = document.getElementById('new-name').value;
    var address = document.getElementById('new-address').value;
    var phone = document.getElementById('new-phone').value;
    var borough = document.getElementById('new-borough').value;
    var comments = document.getElementById('new-comments').value;
    /*
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
*/
    console.log('Beginning to make nw call' + name);
    // set up url
    var xhr = new XMLHttpRequest(); // 1 - creating request object
    var url = null;

    
    url = url_base + ':' + port + '/dictionary/';
    
    var action = "POST";
    xhr.open(action, url, true); // 2 - associates request attributes with xhr

    // set up onload
    xhr.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhr.responseText);
        // do something
        updateResponse3(xhr.responseText);
    }
    console.log(url);
    // set up onerror
    xhr.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhr.statusText);
    }

    var message_body = "{\"name\": \"" + name + "\", \"borough\": \"" + borough + "\", \"address\": \"" + address + "\", \"phone_number\": \"" + phone + "\", \"comments\": \"" + comments + "\"}";
    console.log(message_body);
    xhr.send(message_body) // #TODO: fix message body to actually post the correct stuff
    

   
};

function updateResponse3(response){
        console.log(response);
        var response_json = JSON.parse(response);
        
        var answer_label = document.getElementById('answer-label');
        if(response_json['output'] === 'error'){
        answer_label.innerHTML = "ERROR"
        } else {
        answer_label.innerHTML = response_json['result'] ;
        }
};
