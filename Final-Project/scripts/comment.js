// respond to button click
console.log("Page load happened!")

send_button = document.getElementById('comment-button');
send_button.onmouseup = makeRequest;

function makeRequest(){
    console.log("Entered Comments!")
    // get text from title, author and story
    const url_base = 'http://student04.cse.nd.edu';
    const port = '51086';

    var name = document.getElementById('comment-name').value;
    var comment = document.getElementById('comment-text')
    console.log('Beginning to make nw call' + name);
    var message_body = "{'comment': '" + comment + "'}"
    // set up url
    var xhr = new XMLHttpRequest(); // 1 - creating request object
    var url = null;

    if(name != null){
        url = url_base + ':' + port + '/comments/' + name;   
    } else {  
        updateResponse("{'result': 'error'}");
    }
    var action = "PUT"
    xhr.open(action, url, true); // 2 - associates request attributes with xhr

    // set up onload
    xhr.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhr.responseText);
        // do something
        updateResponse1(xhr.responseText);
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
     xhr.send(message_body) // last step - this actually makes the request
  //  }
   makeCommentRequest(name);
};

function updateResponse1(response){
        
        var response_json = JSON.parse(response);

        var answer_label = document.getElementById('comment-label');
        if(response_json['output'] === 'error'){
        answer_label.innerHTML = "ERROR"
        } else {
        answer_label.innerHTML = response_json['result'] ;
        }

};
function makeCommentRequest(name){
    console.log("Entered Comments!")
    // get text from title, author and story
    const url_base = 'http://student04.cse.nd.edu';
    const port = '51086';

    console.log('Beginning to make nw call' + name);
    
    // set up url
    var xhr = new XMLHttpRequest(); // 1 - creating request object
    var url = null;

    if(name != null){
        url = url_base + ':' + port + '/comments/' + name;   
    } else {  
        updateResponse("{'result': 'error'}");
    }
    var action = "GET"
    xhr.open(action, url, true); // 2 - associates request attributes with xhr

    // set up onload
    xhr.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhr.responseText);
        // do something
        updateComments(xhr.responseText);
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
function updateComments(response){
        
        var response_json = JSON.parse(response);

        var answer_label = document.getElementById('comment-label');
        if(response_json['output'] === 'error'){
        answer_label.innerHTML = "ERROR"
        } else {
        answer_label.innerHTML = response_json['comments'] ;
        }

};
