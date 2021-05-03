var number = Math.round( Math.random() * 100 + 1 );
var guess = "";
while (guess != number) {
  guess = prompt("Guess a number between 1 and 100: ");
  if ( guess > number )
      alert("Too high.");
  else if (guess < number)
    alert("Too low.");
  else
    alert("Correct, you win!");
}
var userName = prompt("What is your name?")
for (var i = 1; i < 100; i++) {
  document.write(userName + " wins! ")
}
