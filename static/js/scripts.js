console.log('I am here')

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');

let correctAnswers = document.querySelectorAll('.correct-answer')
let markClosedAll = document.querySelectorAll('.mark-closed')

// console.log(correctAnswer.parentElement)


for (const correctAnswer of correctAnswers) {
  let answerPk = correctAnswer.parentElement.dataset.answerPk
  let URL = `/questions/${answerPk}/answer/mark_correct`  

  correctAnswer.addEventListener('click', e => {
    fetch(URL, {
      headers:{
        'Accept': 'application/json/json',
        'X-Requested-With': 'XMLHttpRequest',
      },
    })
    .then(response => {
      return response.json()
    })
    .then(data => {
      console.log(data)
      // debugger
      correctAnswer.nextElementSibling.classList.toggle('fa-smile')
      correctAnswer.classList.toggle('fa-square')
      correctAnswer.classList.toggle('fa-check-square')
    })
  })
}

for (const markClosed of markClosedAll) {
  let questionPk = markClosed.parentElement.dataset.questionPk
  let URL = `/questions/${questionPk}/mark_closed`  

  markClosed.addEventListener('click', e => {
    fetch(URL, {
      headers:{
        'Accept': 'application/json/json',
        'X-Requested-With': 'XMLHttpRequest',
      },
    })
    .then(response => {
      return response.json()
    })
    .then(data => {
      console.log(data)
      // debugger
      // markClosed.previousSibling.classList.toggle('disable')
      markClosed.classList.toggle('disable')
    })
  })
}