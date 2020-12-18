/*====smooth ===*/
const showMenu = (toggledId, navId) =>{
		const toggle = document.getElementById(toggleId),
		nav = document.getElementById(navId)

		if(toggle && nav){
				toggle.addEventListener('click', ()=>{
						nav.classList.toggle('show-menu')
				})
		}
}
showMenu('nav-toggle','nav-menu')

/*====Font weight ===*/
const navLink = document.querySelectorAll('.nav__link')

function linkAction(){
		const navMenu = document.getElementById('nav-menu')

		navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListenet('click', linkAction))
