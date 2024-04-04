//Do not share this token
//TODO input your own API token
const TOKEN = ''

// this is where we call the API to classify our unlabeled text based on the training data we pass in as a prompt
function classify(s_args, s_input) {

    // we start by extracting the training data from the specified range in s_args and packaging it into a prompt
    let inputs = [s_input];
    let examples = [];
    for (let i = 0; i< s_args.length; i++) {
      //this is assuming label is always the 2nd parameter
      examples.push({"text" : s_args[i][0] , "label" : s_args[i][1]})
    }
  
    const payload_for_classification = {
      examples,
      inputs,
      "model" : "embed-english-v2.0",
    };
  
    const options = {
      'headers' : { 'Authorization' : 'Bearer ' + TOKEN },
      'method' : 'post',
      'contentType': 'application/json',
      'payload' : JSON.stringify(payload_for_classification)
    };

    const response = UrlFetchApp.fetch('https://api.cohere.ai/v1/classify', options);
    const responseContent = response.getContentText();
    const responseContentText = JSON.parse(response.getContentText());
    const classificationContent = responseContentText.classifications[0];
    const ourPrediction = classificationContent.prediction;
    const confidence = (classificationContent.confidence * 100).toFixed(2) + "%";
    let displayString = "Prediction: " + ourPrediction.toUpperCase() + " review\n" + "Confidence Level: " + confidence + "\n";
    return displayString;
  
  }

// this is where we call the API to summarize the review
function summarize(cell_value) {

    let raw = JSON.stringify({
        "message": "Summarize this in about 10 words: " + cell_value,
        "temperature": 0.2,
        "model": "command-r",
    });
    let requestOptions = {
        'method': 'post',
        'muteHttpExceptions': true,
        'contentType': 'application/json',
        'headers': {
            'Authorization': 'Bearer ' + TOKEN
        },
        'payload': raw,
        redirect: 'follow'
    };
    
     let response = UrlFetchApp.fetch("https://api.cohere.ai/v1/chat", requestOptions)
     let responseContentTxt = JSON.parse(response.getContentText());
     let summarizedTxt = "SUMMARY: " + responseContentTxt.text + "\n";
     return summarizedTxt;

}