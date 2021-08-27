/* 등록 팝업 */
function showPopup(hasFilter) {
	const popup = document.querySelector('#popup');
  
  if (hasFilter) {
  	popup.classList.add('has-filter');
  } else {
  	popup.classList.remove('has-filter');
  }
  
  popup.classList.remove('hide');
}

function closePopupCheck() {
	const popupCheck = document.querySelector('#popupCheck');
  popupCheck.classList.add('hide');
}

