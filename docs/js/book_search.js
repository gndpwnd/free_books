let search_index_file = 'js/search_index.json';
const dropdown = document.getElementById('search-results');

function getSearchIndexFile() {
  return fetch(search_index_file)
    .then(response => response.json())
    .then(data => {
      return search_index_file;
    })
    .catch(error => {
      console.log(error);
      search_index_file = '../js/search_index.json'; // change the file path
      return search_index_file;
    });
}

function searchBooks() {
  const userInput = document.getElementById('search-bar').value;
  if (userInput.trim() === '') { // return early if input is empty or only whitespace
    dropdown.innerHTML = '';
    dropdown.style.display = 'none'; // hide the dropdown
    return;
  }
  getSearchIndexFile().then(file => {
    fetch(file)
      .then(response => response.json())
      .then(data => {
        let matchingBooks = [];

        // Loop through each category in the data
        Object.keys(data).forEach(category => {
          // Loop through each book in the category
          data[category].forEach(book => {
            // Check if the book title contains the user input
            if (book[0].toLowerCase().includes(userInput.toLowerCase())) {
              // Add the matching book title, link, and category to the matchingBooks array
              matchingBooks.push({
                title: book[0],
                link: book[1],
                category: category
              });
            }
          });
        });

        // Debugging: print the matching books to the console
        //console.log(matchingBooks);

        // Populate the dropdown menu with all the matching books
        dropdown.innerHTML = '';
        // if there are no matches, return
        if (matchingBooks.length === 0) {
          dropdown.style.display = 'none';
        } else {
          for (const element of matchingBooks) {
            const book = element;
            const link = document.createElement('a');
            link.href = book.link;
            link.innerHTML = `<span class="title">${book.title}</span><span class="category">${book.category}</span>`;
            dropdown.appendChild(link);
          }
          dropdown.style.display = 'block';
        }
        
          dropdown.style.display = 'block'; // show the dropdown
      })
      .catch(error => console.log(error));
  });
}
