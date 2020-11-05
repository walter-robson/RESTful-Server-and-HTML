// respond to button click
console.log("Page load happened!")

send_button = document.getElementById("submit-button");
send_button.onmouseup = makeRequest4;

function makeRequest4(){
    console.log("Entered Search!")
    // get text from title, author and story
    const url_base = 'http://student04.cse.nd.edu';
    const port = '51086';

    var search_term = document.getElementById('text-field-1').value;
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
    console.log('Beginning to make nw call');
    // set up url
    var xhr = new XMLHttpRequest(); // 1 - creating request object
    var url = null;

    if(search_term != null){
        url = url_base + ':' + port + '/dictionary/' + search_term;   
    } else {  
        url = url_base + ':' + port + '/dictionary/';
    }
    var action = "GET"
    xhr.open(action, url, true); // 2 - associates request attributes with xhr

    // set up onload
    xhr.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhr.responseText);
        // do something
        updateResponse(xhr.responseText);
    }
    console.log(url);
    // set up onerror
    xhr.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhr.statusText);
    }

    // actually make the network call
   /* if(message_body != null) {
        xhr.send(message_body)
    } else {*/
     xhr.send(null) // last step - this actually makes the request
  //  }
  
};

function updateResponse(response){
        
        var response_json = JSON.parse(response);

        var answer_label = document.getElementById('answer-label');
        if(response_json['output'] === 'error'){
        answer_label.innerHTML = "ERROR"
        } else {
        answer_label.innerHTML = response_json['name'] + " is located at " + response_json['address'] + " and can be reached at " + response_json['phone_number'] + '\n' + response_json['comments'];
        }
        updateComments(response_json['comments'])
};

function updateComments(response){
        
        var response_json = JSON.parse(response);

        var answer_label = document.getElementById('comment-label');
        if(response_json['output'] === 'error'){
        answer_label.innerHTML = "ERROR"
        } else {
        answer_label.innerHTML = response ;
        }

};

