// respond to button click
console.log("Page load happened!")

var submitButton = document.getElementById('submit-button')
submitButton.onmouseup = getFormInfo;

function getFormInfo(){
    console.log("Entered get Form Info!")
    // get text from title, author and story

    var name = document.getElementById('input-name').value;
    console.log('Name:' + name);

    makeNetworkCallToNationalityApi(name);

};


function makeNetworkCallToNationalityApi(name){
    console.log('entered make nw call' + name);
    // set up url
    var xhr = new XMLHttpRequest(); // 1 - creating request object
    var url = "https://api.nationalize.io/?name=" + name;
    xhr.open("GET", url, true); // 2 - associates request attributes with xhr

    // set up onload
    xhr.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhr.responseText);
        // do something
        updateNameWithResponse(name, xhr.responseText);
    }

    // set up onerror
    xhr.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhr.statusText);
    }

    // actually make the network call
    xhr.send(null) // last step - this actually makes the request

} // end of make nw call

function updateNameWithResponse(name, response_text){
    var response_json = JSON.parse(response_text);
    // update a label
    var label1 = document.getElementById("response-line1");

    if(response_json['name'] == null){
        label1.innerHTML = 'Apologies, we could not find your nationality.'
    } else{
        label1.innerHTML =  name + ', your country code is ' + response_json['country'][0]['country_id'];
        var nationality = response_json['country'][0]['country_id'];
        makeNetworkCallToNationalityAPI2(nationality, name);
    }
} // end of updateAgeWithResponse

function makeNetworkCallToNationalityAPI2(nationality, name){
    console.log('entered make nw call' + nationality);
    // set up url
    var xhr = new XMLHttpRequest(); // 1 - creating request object
    var url = "https://restcountries.eu/rest/v2/alpha/" + nationality;
    xhr.open("GET", url, true); // 2 - associates request attributes with xhr

    // set up onload
    xhr.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhr.responseText);
        // do something
        updateNameWithResponse2(name, xhr.responseText);
    }

    // set up onerror
    xhr.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhr.statusText);
    }

    // actually make the network call
    xhr.send(null) // last step - this actually makes the request

} // end of make nw call

function updateNameWithResponse2(name, response_text){
    var response_json = JSON.parse(response_text);
    // update a label
    var label2 = document.getElementById("response-line2");

    if(response_json['name'] == null){
        label2.innerHTML = 'Apologies, we could not find your nationality.'
    } else{
        label2.innerHTML =  name + ', that means you are from ' + response_json['name'];
    }
} // end of updateAgeWithResponse