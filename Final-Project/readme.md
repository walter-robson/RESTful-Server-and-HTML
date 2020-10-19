Command         Resource        Input Example(body of request)  Output Example(response received from server)            Behavior

PUT        /comments/:key
    e.g. /comments/FacilityName     {"value":"Review"}        {"result": "success"}                   Adds that key-value pair to the dictionary

POST       /dictionary/        {"key" : "Facility Name",        {"result": "success"}                           Adds a key-value pair from the message
                                                                                                                           body to the dictionary

GET        /dictionary/:key                                     {"result": "success", "key": "Facility Name",        displays the entry for that key
                                                                "value": "Address, phone number, reviews"}

GET        /dictionary/                                         {"result": "success", "entries":                         displays the entire contents of 
                                                                [{"key": "Facility Name",                                       the dictionary
                                                                "value": "address, phone number, reviews"},
                                                                 {"key": "Facility Name", 
                                                                 "value": "address, phone number, reviews"}]}

DELETE     /dictionary/:key                                     {"result": "success"}                             Deletes that key-value pair from the 
                e.g.                                                                                               dictionary. You can check deletion 
         /dictionary/FacilityName                                                                                                with a GET

.
DELETE       /dictionary/                                        {"result": "success"}                        Deletes all the contents of the dictionary.

