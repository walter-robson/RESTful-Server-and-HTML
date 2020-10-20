// respond to button click
console.log("Page load happened!")

var submitButton = document.getElementById('submit-button')
submitButton.onmouseup = getFormInfo;

function getFormInfo(){
    console.log("Entered get Form Info!")
    // get text from title, author and story
    var email_text = document.getElementById('input-email').value;
    var password_text = document.getElementById("input-password").value;
    var order_name = document.getElementById('input-name').value;
    console.log('Name:' + order_name + ' Email: ' + email_text + ' Password ' + password_text);

    // get food type
    var food_type = "";
    if (document.getElementById('radio1').checked){
        console.log('detected hotdog!');
        food_type = "Hotdog";
    }

    if (document.getElementById('radio2').checked) {
        console.log('detected hamburger!');
        food_type = "Hamburger";
    }

    if (document.getElementById('radio3').checked) {
        console.log('detected bratwurst!');
        food_type = "Bratwurst";
    }

    console.log('Food type: ' + food_type);

    // get condiments
    var condiments = "";
    if (document.getElementById('checkbox-1').checked){
        console.log('detected Mustard!');
        condiments += " Mustard,";
    }

    if (document.getElementById('checkbox-2').checked) {
        console.log('detected ketchup!');
        condiments += " Ketchup,";
    }

    if (document.getElementById('checkbox-3').checked) {
        console.log('detected Fry Sauce!');
        condiments += " Fry Sauce,";
    }
    if (document.getElementById('checkbox-4').checked) {
        console.log('detected Relish!');
        condiments += " Relish";
    }
    // make genre combined string
    console.log('condiments: ' + condiments);

    // make dictionary
    order_dict = {};
    order_dict['name'] = order_name;
    order_dict['email'] = email_text;
    order_dict['item'] = food_type;
    order_dict['password'] = password_text;
    order_dict['condiments'] = condiments;
    console.log(order_dict);

    displayOrder(order_dict);

};

function makeNetworkCallToGenderApi(name){
    console.log('entered make nw call' + name);
    // set up url
    var xhr = new XMLHttpRequest(); // 1 - creating request object
    var url = "https://api.genderize.io/?name=" + name;
    xhr.open("GET", url, true); // 2 - associates request attributes with xhr

    // set up onload
    xhr.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhr.responseText);
        // do something
        updateGenderWithResponse(name, xhr.responseText);
    }

    // set up onerror
    xhr.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhr.statusText);
    }

    // actually make the network call
    xhr.send(null) // last step - this actually makes the request

} // end of make nw call

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
        updateNationalityWithResponse(name, xhr.responseText);
    }

    // set up onerror
    xhr.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhr.statusText);
    }

    // actually make the network call
    xhr.send(null) // last step - this actually makes the request

} // end of make nw call

function updateNationalityWithResponse(nationality, response_text){
    // update a label
    var label2 = document.getElementById("response-line2");
    label2.innerHTML = response_text;

    // dynamically adding label
    label_item = document.createElement("label"); // "label" is a classname
    label_item.setAttribute("id", "dynamic-label" ); // setAttribute(property_name, value) so here id is property name of button object

    var item_text = document.createTextNode(response_text); // creating new text
    label_item.appendChild(item_text); // adding something to button with appendChild()

    // option 1: directly add to document
    // adding label to document
    //document.body.appendChild(label_item);

    // option 2:
    // adding label as sibling to paragraphs
    var response_div = document.getElementById("response-div");
    response_div.appendChild(label_item);

} // end of updateTriviaWithResponse

function displayOrder(order_dict){
    console.log('entered displayOrder!');
    console.log(order_dict);
    // get fields from story and display in label.
    var order_top = document.getElementById('order-top-line');
    order_top.innerHTML = order_dict['name'] + ' (' + order_dict['email'] + ') (Password: ' + order_dict['password'] + ')';

    var order_body = document.getElementById('order-body');
    order_body.innerHTML = order_dict['item'] + ' with ' + order_dict['condiments'];

}
