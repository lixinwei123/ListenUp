//const functions = require("firebase-functions");
const express = require('express');
var cors = require('cors');
const app = express();
var request = require('request');
var admin = require('firebase-admin');

clientid = '78c4dxl71hmu6t';
clientsecret = '4g2cS0SBRlDl7DHk';

app.use(cors());

admin.initializeApp({
  credential: admin.credential.cert({
    projectId: 'listenuptesting',
    clientEmail: 'firebase-adminsdk-nhcja@listenuptesting.iam.gserviceaccount.com',
    privateKey: "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDfK8tTuBR+pxvG\nCd03SU3XtTZx0pwFM76ScF00IjpQF95ztG/7iPvT9KDW1CUq9Xdqh7U9xIk1Z3X2\nwraSCDZnXbpkAiGjaRNPUVajWQRNVt1UV57Xklu5g9laD9K5rOATa/VQY7dh0RyT\n2eErOqhctavCs8R9xA3+pHhxwT/lespi6huGB8eo+DC9m1UkFBVTX5yhloXefELh\nHpAQZMOWqxmA6BmMdtrCqcQug/Q/2UkBMwnsHoVGKLWGTXpjGBeQW+0wZsxVe7XA\ntbNkYBFYq9ZrY+xhVnoKVYyTRQVWt0lqDpwwVcACqvng35GwGrFM6y9AwrWAHwOV\n4qiXZ2B5AgMBAAECggEACVBgwtnhZ8HIq8oN703sukPIBcBrnjShJP0ciV2jqmO8\nodPrgodz3yOMB5CWC9tvxESYAKpwVt1pCRyU6wuoXZsF+ZY0hNyQn5RToICevdg8\nvNWP/bY62XISbar7DqBo6laXR+d0KAMcBWL9U0ULnBxBkrWBo1q913KndjPsW0Lh\n3m70+9PsqAodz0FwPlqtslQTYZuazRsqIAxoKG73Lda3JDjm75OBxtjL9kfNjkUN\npsYQebyOsEEM4R+k4rIU/T+QzoA6+jt073IGnDx916PujDbJGy4hqeu1EImpg4GY\ngxAHkmh3wSQsbAvcgth1dEE6O/Ey7nNiwekTrzngCwKBgQD2le6BFZwcmoRjU1/H\noEAxvkN0gd0MrhKNwuQQY9RJ1XQG79YQV3foyOdrTG/Dp7gBhjOUDJKJYXtYx81L\ngiwclUsbO95GPaFVGGxhM7IwztqseQa7762ncFJ3sOa+fiDsbegdTPdvK9xZUq1q\nsr28/iHKoGtayiSi8Wq/zgNnrwKBgQDnsQOVD9qcoWdCU/r8xd3mI91lkWXapjzS\ngLgtsvrOMknnGOevR3SH5gTpY0NUoy4AAU2e6wJbwMLIgN2fPV3CivLNTOZbBusZ\nlJ6M5Z8Y4uECv2awwFnrojK5IzF8gehN+q4ecY1hFVX57zZrz10VD9eW5w8gNxBO\nZQ6i65gcVwKBgHd9pDvtSt8ZiXnQVyOXZkQ0nN+CZqnUWK1VecrvdVnqE/Wgly0I\nFdU6NdprCeXYCnTCoY/mn8Pu9yTIfZVPmSyos+KYmleTWfCwiyR3NqwsMQ9O/pJn\nzNDMv0m88bPxzuaDQ+2e9HBs4rRuOhbwUr2YsKtOHXe7aRGEx2P24vOFAoGAS7Yk\nnYlYvuZff+VBl2hxYstFhfNFfXXlWkSF6ykZnFgCnmodC8Il6mLYKAwv7HCGj6nd\nW5kgZCtRe4Pg6DB9ex08yqnefNB98xYF2bUPkGpTbTpurEOvHrkaKjW97hnld9X7\nICerM5ZtSgdJmWFh4YgTw1QuNTDJO1T6u3KRenECgYAeHzncvkCYWxtHybexxJvk\nYrYRsEHCrtPQHHDWHflQEKdj4+NnCdYX4cJ7Fsk3g515LG2M1P5huEeGg2BbCNGd\n2rdHjeF6+bOSzjiSfe43lfdNUiAR0CVtqI+UiOumj38W4BZ9/2qn24ZsAreuxqJq\nk7dfGi7TvE5qLwMsJ+I0Mg==\n-----END PRIVATE KEY-----\n",

  }),
  databaseURL: 'https://listenuptesting.firebaseio.com/'
});

app.get('/callback', (req, res) => {
	var code = req.query.code;
	var FCMToken = req.query.state;

	//res.send("got the code from the callback", code, state);

	//get the access token
	var accessTokenURL = 'https://www.linkedin.com/oauth/v2/accessToken';
	//var atokenRedirect=  'https://us-central1-listenuptesting.cloudfunctions.net/expressAPI/callback';  //can be changed
	var atokenRedirect = "http://5d65609c.ngrok.io/callback";

	var atokenString = 'grant_type=authorization_code&code='+code
	+'&redirect_uri='+atokenRedirect+'&client_id='+clientid+'&client_secret='+clientsecret;

	request({
		url: accessTokenURL,
		method: 'POST',
		headers: {
			"content-type": 'application/x-www-form-urlencoded'
		},
		body: atokenString
	}, (error, response, body) => {
		console.log("error first post",error);
		console.log("response first post",response);
		console.log("body first post",body);

		//if successful, the tokens will be in these variables
		if(response.statusCode === 200){
			var newBody = JSON.parse(body);
			var accessToken = newBody.access_token;
			var expires = newBody.expires_in;
			//res.sendFile('index.html', {root: __dirname });
			//res.send('success, we got the access token');
			var profileURL = "https://api.linkedin.com/v1/people/~?oauth2_access_token=" + accessToken + "&format=json";
			var emailURL = "https://api.linkedin.com/v1/people/~/email-address?oauth2_access_token=" + accessToken + "&format=json";

			request(profileURL, (arr, rez, bewd) => {
				var newBewd = JSON.parse(bewd);
				var gotID = newBewd.id;
				var gotFirstname = newBewd.firstName;
				var gotLastName = newBewd.lastName;

				console.log("newBewd", newBewd);
				request(emailURL, (err, res, bod) => {
					var gotB64ModEmail = Buffer.from(bod).toString('base64').replace(/=/g,'');
					console.log("email is", gotB64ModEmail);


					//firebase auth get custom credential
					admin.auth().createCustomToken(gotID + gotB64ModEmail).then(function(customToken){
					  console.log("got Custom Token!", customToken);

					  var message = {
					  	data: {
					  		customT: customToken,
					  		email: bod,
					  		firstname: gotFirstname,
					  		lastname: gotLastName,
					  		fbID: gotID + gotB64ModEmail
					  	},
					  	token: FCMToken
					  };

					  //send message to clientside with token
					  admin.messaging().send(message).then(response => {
					  	console.log("successfully sent");
					  }).catch(err => {
					  	console.log("something went wrong", err);
					  });

					  }).catch(function(error){
					  	console.log("error!", error);
					 //res.send('error!');
					  });


					
				});
			})
	
				

			
		}
	});

});

app.listen(3000, () => {
	console.log("running server on 3000");
})

//const expressAPI = functions.https.onRequest(app);

/*module.exports = {
	expressAPI
}*/


