<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" type="text/css" href="/static/style.css">
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
 <title>Flask</title>
</head>
<body>
<h3>Chatbot</h3>
<div>
 <div id="chatbox">
  <p class="botText"><span>Hi! Im Chatbot</span></p>
 </div>
 <div id = "userInput">s
  <input id = "textInput" type="text" name = "msg" placeholder="Message">
  <input id="buttonInput" type="submit" value="send">
</div>
<script type="text/javascript">
 function getBotResponse(){
  var rawText = $("#textInput").val();
  var userHtml = '<p class="userText"><span>' + rawText + '</span></p>';
  $("#textInput").val("");
  $("#chatbox").append(userHtml);
  document.getElementById('userInput').scrollIntoView({block:'start',behaviour:'smooth'});
  $.get("/get",{msg:rawText}).done(function(data){
   var botHtml = '<p class="botText"><span>' + data + '</span></p>';
   $("#chatbox").append(botHtml);
   document.getElementById('userInput').scrollIntoView({block:'start',behaviour:'smooth'});
  });
 $("#textInput").keypress(function(e){
  if(e.which == 13) {
   getBotResponse();
  }
 });
 $("#buttonInput").click(function(){
  getBotResponse();
 })

</script>
</body>
</html>