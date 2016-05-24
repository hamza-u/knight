

function change_text () {
	var item = document.getElementById ("header2")
	if (item.innerHTML.match('Hamza'))
		item.innerHTML = 'Hello World !!!!!!!!!'
	else
		item.innerHTML = 'Hello Hamza'
}

function show_text () {
	var inp = document.forms["f1"]["i1"].value
	var out = document.getElementById ("output")

	out.innerHTML = inp
	window.alert(document.forms["f1"]["i1"].value);

}
