console.log("Page load happened!")

send_button = document.getElementById("submit-button");
send_button.onmouseup = makeRequest;

function makeRequest(){
    console.log("Entered Search!")
    // get text from title, author and story
    const url_base = 'http://student04.cse.nd.edu';
    const port = '51086';

    var search_term = document.getElementById('text-field-1').value;
    console.log('Beginning to make nw call' + name);
    // set up url
    var xhr = new XMLHttpRequest(); // 1 - creating request object
    var url = null;

    url = url_base + ':' + port + '/reset/';
   
    var action = "PUT"
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
     xhr.send(null) // last step - this actually makes the request

};

function updateResponse(response){
        
        var response_json = JSON.parse(response);

        var answer_label = document.getElementById('answer-label');
        if(response_json['output'] === 'error'){
        answer_label.innerHTML = "ERROR"
        } else {
        answer_label.innerHTML = response_json['result'] ;
        }
};
