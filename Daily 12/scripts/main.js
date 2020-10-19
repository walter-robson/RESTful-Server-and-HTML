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

function displayOrder(order_dict){
    console.log('entered displayOrder!');
    console.log(order_dict);
    // get fields from story and display in label.
    var order_top = document.getElementById('order-top-line');
    order_top.innerHTML = order_dict['name'] + ' (' + order_dict['email'] + ')';

    var order_body = document.getElementById('order-body');
    order_body.innerHTML = order_dict['item'] + ' with ' + order_dict['condiments'];

}
