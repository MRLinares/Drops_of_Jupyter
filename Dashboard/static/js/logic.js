function saveDataToPickle() {

    // Create an empty list
    
    var data = [];
  
    // Retrieve the data from the input fields

    data.push(document.querySelector('#prediabetes').value);
    data.push(document.querySelector('#weightlbs').value);
    data.push(document.querySelector('#height').value);
    data.push(document.querySelector('#age').value);
    data.push(document.querySelector('#gender').value);
    data.push(document.querySelector('#education').value);
    data.push(document.querySelector('#race').value);
    data.push(document.querySelector('#hhincome').value);
    data.push(document.querySelector('#hhsize').value);

    return data;
  }

function handleClick() {
    let submitButton = document.querySelector("#submit-button");
    submitButton.addEventListener('click', function(event) {

        // Collect form data and store it in a list

        event.preventDefault();
        var data = saveDataToPickle();

        // Define the object with predetermined keys

        var dataObj = {
            Prediabetes: data[0],
            Weight_Lbs: data[1],
            height: data[2],
            Age: data[3],
            Gender: data[4],
            Education: data[5],
            Race: data[6],
            HHincome: data[7],
            HHcount: data[8]
        };

        // Log the object to the console

        console.log(dataObj);
    });
};

handleClick();
