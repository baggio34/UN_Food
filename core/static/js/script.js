document.addEventListener("DOMContentLoaded", function(){
	const signUpButton = document.getElementById('criar');
	const criar = document.getElementById('cadastrar');
	const signInButton = document.getElementById('signIn');
	const container = document.getElementById('container');

	signUpButton.addEventListener('click', () => {
		container.classList.add("right-panel-active");
	});

	signInButton.addEventListener('click', () => {
		container.classList.remove("right-panel-active");
	});

	criar.addEventListener('click', () => {
		container.classList.remove("right-panel-active");
	})

})