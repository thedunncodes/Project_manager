let pm_button = document.querySelector('.col1-header')
let project_form = document.querySelector('.pm-col1-form')
let pm = window.getComputedStyle(document.querySelector('.pm-col1-form'))

window.onclick = (event) => {
    // "closest" is the one trick pony to all my troubles sinceeee 😭 😭 
    // Now the window can ignore the div you dont want it to matche
    // "closest" will help check if the clicked element or any of its ancestors do not match the specified class
    
    if (event.target.closest('.col1-header')) {
        project_form.classList.toggle("show");
    } else if (!event.target.closest('.pm-col1-form')) {
        if (pm.display === 'block') {
            project_form.classList.toggle("show");
        }
    }
}
