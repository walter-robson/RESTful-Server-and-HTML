// respond to button click
console.log("Page load happened!")

var submitButton = document.getElementById('submit-button')
submitButton.onmouseup = getFormInfo;

function getFormInfo(){
    console.log("Entered get Form Info!")
    // get text from title, author and story
    var email_text = document.getElementById('title-text').value;
    var password_text = document.getElementById('author-text').value;
    var order_name = document.getElementById('text-story').value;
    console.log('title:' + title_text + ' author: ' + author_text + ' story ' + story_text);

    // get food type
    var food_type = "";
    if (document.getElementById('checkbox-horror-value').checked){
        console.log('detected hotdog!');
        genres_string = "Hotdog";
    }

    if (document.getElementById('checkbox-comedy-value').checked) {
        console.log('detected hamburger!');
        genres_string = "Hamburger";
    }

    if (document.getElementById('checkbox-drama-value').checked) {
        console.log('detected bratwurst!');
        genres_string = "Bratwurst";
    }

    // get condiments
    var condiments = "";
    if (document.getElementById('checkbox-horror-value').checked){
        console.log('detected Mustard!');
        genres_string += "Mustard,";
    }

    if (document.getElementById('checkbox-comedy-value').checked) {
        console.log('detected ketchup!');
        genres_string = "Ketchup,";
    }

    if (document.getElementById('checkbox-drama-value').checked) {
        console.log('detected Fry Sauce!');
        genres_string = "Fry Sauce";
    }
    // make genre combined string
    console.log('genres: ' + genres_string);

    // make dictionary
    story_dict = {};
    story_dict['title'] = title_text;
    story_dict['author'] = author_text;
    story_dict['story'] = story_text;
    story_dict['genres'] = genres_string;
    console.log(story_dict);

    displayStory(story_dict);

}

function displayStory(story_dict){
    console.log('entered displayStory!');
    console.log(story_dict);
    // get fields from story and display in label.
    var story_top = document.getElementById('story-top-line');
    story_top.innerHTML = story_dict['title'] + ' by ' + story_dict['author'];

    var story_body = document.getElementById('story-body');
    story_body.innerHTML = story_dict['story'];

}
