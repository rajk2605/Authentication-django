function check()
{
	let marks = document.getElementById("id_marks");
	let msg = document.getElementById("msg");

if(marks.value=="")
{
	alert("marks are empty");
	msg.innerHTML="";
	marks.focus();
	return false;
}
let marks = parseInt(marks.value);

if(marks < 0) || (marks > 100)
{
	alert("Marks Should be between 0 to 100");	
	msg.innerHTML="";
	marks.focus();
	return false;
}
return true;
}