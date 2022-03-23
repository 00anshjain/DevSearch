{/* <script type="text/javascript"> */}
  // Get Search Form and page links
  let searchForm = document.getElementById('searchForm')
  let pageLinks = document.getElementsByClassName('page-link')
  // There are multiple element for this class name

  // If we dont have search form we dont want this to work
  // ENSURE SEARCH FORM EXISTS
  if(searchForm){
    for(let i=0; pageLinks.length > i; i++ ){
      // We will iterate on each page
      // We will add eventlistener to each event
      // Evertime button is clicked, we gonna fire of this event
        pageLinks[i].addEventListener('click', function (e) {
          e.preventDefault()
          // It will stop default action from occuring
          // console.log('Button Clicked') //Print statement

          // GET THE DATA ATTRIBUTE
          let page = this.dataset.page
          // this is the button we clicked on
          // console.log('PAGE:', page)

          // ADD HIDDEN SEARCH INPUT TO FORM
          searchForm.innerHTML += `<input value=${page} name="page" hidden/>`

          // SUBMIT FORM
          searchForm.submit()

        })
    }
  }
// </script>