(function () {
    "use strict";
    let inputField = document.getElementById('input');
    let ulField = document.getElementById('suggestions');
    inputField.addEventListener('input', changeAutoComplete);
    ulField.addEventListener('click', selectItem);
  
    function changeAutoComplete({ target }) {
      let data = target.value;
      ulField.innerHTML = ``;
      if (data.length) {
        let autoCompleteValues = autoComplete(data);
        autoCompleteValues.forEach(value => { addItem(value); });
      }
    }
  
    function autoComplete(inputValue) {
      let destination = ["Italy", "Spain", "Portugal", "Brazil"];
      return destination.filter(
        (value) => value.toLowerCase().includes(inputValue.toLowerCase())
      );
    }
  
    function addItem(value) {
      ulField.innerHTML = ulField.innerHTML + `<li>${value}</li>`;
    }
  
    function selectItem({ target }) {
      if (target.tagName === 'LI') {
        inputField.value = target.textContent;
        ulField.innerHTML = ``;
      }
    }
  })();