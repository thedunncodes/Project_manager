const board_page_bar = document.querySelector('.page_focus3')
const page = "/boards";

(() => {
    if (window.location.pathname === page) {
        board_page_bar.classList.toggle('pm_focus_toggle')
    }
})();


let tf_layout = ''
let new_task = ''
let task_icon = ''


// function getClasses(event) {
//     const clickedElement = event.target.closest('.add_task_icon'); // Get the element the event occurred on
//     task_icon = event.target.closest('.add_task_icon');
//     tf_layout = window.getComputedStyle(clickedElement.querySelector('.task_form_layout'))
//     console.log(clickedElement.classList)
//     new_task = clickedElement.querySelector('.task_form_layout'); 

//     if (tf_layout.display === 'block') {
//         // window.onclick = (event) => {
//         //     if (!event.target.closest('.task_form')) {
//         //         console.log('yes')
//         //         // new_task.classList.toggle('task_form_layout_toggle')
//         //     }
//         // }
//     } else {
//         console.log('nein')
//         console.log(tf_layout.display)
//         new_task.classList.toggle('task_form_layout_toggle')
//     }
//   }

//   window.onclick = (event) => {
//     tf_layout = window.getComputedStyle(task_icon.querySelector('.task_form_layout'))
//     console.log(tf_layout.display)
//         if (!event.target.closest('.task_form')) {
//             if (tf_layout.display === 'block') {
//                 console.log('Du bist')
//                 new_task.classList.toggle('task_form_layout_toggle')
//             }
//         }
//     }


// if (tf_layout.display === 'block') {
//     // window.onclick = (event) => {
//     //   console.log(new_task)
//     //   if (tf_layout.display === 'block') {
//     //       console.log("nein")
//     //       if (!event.target.closest('.task_form')) {
//     //           if (tf_layout.display === 'block') {
//     //               new_task.classList.toggle('task_form_layout_toggle')
//     //           }
//     //       }
//     //   }
//     // }
//     console.log('yes')
// }










window.onclick = (event) => {
    // console.log(!event.target.closest('.task_form'))
    // console.log(!event.target.matches('.add_task_icon1'))
    if (event.target.matches('.add_task_icon1')) {
        task_icon = event.target.closest('.add_task_icon');
        tf_layout = window.getComputedStyle(task_icon.querySelector('.task_form_layout'))
        // console.log(task_icon.classList)
        new_task = task_icon.querySelector('.task_form_layout');
        // console.log(new_task)
        if (tf_layout.display === 'block') {
            new_task.classList.toggle('task_form_layout_toggle')
        } else {
            new_task.classList.toggle('task_form_layout_toggle')
        }
    } else if (!event.target.closest('.task_form')) {
            const new_task = task_icon.querySelector('.task_form_layout');
            // console.log(!event.target.closest('.task_form'))
            if (tf_layout.display === 'block') {
                new_task.classList.toggle('task_form_layout_toggle')
            }
    }
}