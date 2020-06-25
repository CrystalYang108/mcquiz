function check(){

	var question1 = document.quiz.question1.value;
	var question2 = document.quiz.question2.value;
	var question3 = document.quiz.question3.value;
	var correct = 0;


	if (question1 == "fruits.index" || question1 == "north america") {
		correct++;
}
	if (question2 == "b2") {
		correct++;
}	
	if (question3 == "c3") {
		correct++;
	}
	
	var pictures = ["img/happy.gif", "img/sigh.gif", "img/sad1.gif"];
	var messages = ["Great job!", "That's okay, I guess.", "You need to study more..."];
	var score;

	if (correct == 0) {
		score = 2;
	}

	if (correct > 0 && correct < 3) {
		score = 1;
	}

	if (correct == 3) {
		score = 0;
	}

	document.getElementById("after_submit").style.visibility = "visible";

	document.getElementById("message").innerHTML = messages[score];
	document.getElementById("number_correct").innerHTML = "You got " + correct + " correct.";
	document.getElementById("picture").src = pictures[score];
	}
	
