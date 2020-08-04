document.querySelector('#back-button').addEventListener("click", function () {
    console.log('Inside the red sea');
    [].forEach.call(document.getElementsByClassName('step-2'), function(element) {
        element.classList.remove('active');
    });
    [].forEach.call(document.getElementsByClassName('step-1'), function(element) {
        element.classList.add('active');
    });
});

document.querySelector('.btn-continue').addEventListener("click", function () {
    console.log('Inside the blue sea');
    [].forEach.call(document.getElementsByClassName('step-1'), function(element) {
        element.classList.remove('active');
    });
    [].forEach.call(document.getElementsByClassName('step-2'), function(element) {
        element.classList.add('active');
    });
});
