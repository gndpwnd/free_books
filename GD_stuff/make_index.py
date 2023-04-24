make_index_html_to_use = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-0KZX48SLMJ"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-0KZX48SLMJ');
  </script>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta 
        name="description"
        content="Author: gndpnwd
        Free PDF books. 
        Valuable content for free. 
        No ads, no paywalls, no bullshit.">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/button.css">

    <title>Freshavacado</title>
</head>
<body class="everything">

    <a href="https://books.dev00ps.com">
        <img class="title" src="assets/free_books.webp" alt="Free Books" stye="width:563px;height:251px;">
    </a>

  <h2 class="subtitle">Valuable content for free. <i>No ads, no paywalls, no bullshit.</i></h2>
    
  <h3 class="subtitle">
    <button class="menu_button"><span onclick="window.location='./books.html'">Books</span></button>
    <button class="menu_button"><span onclick="window.location='./audiobooks.html'">Audiobooks</span></button>
    <button class="menu_button"><span onclick="window.location='./donate.html'">Donate</span></button>
    <button class="menu_button"><span onclick="window.location='https://cliffnotes.dev00ps.com'">Cliffnotes</span></button>
  </h3>

  <p class="description-head">Project Goals</p>
  <ul class="description">
    <li class="bullet_point">To accumulate knowledge for success in life</li>
    <li class="bullet_point">To store such knowldege in an easily accessable library</li>
    <li class="bullet_point">To condense the size of such library to fit the completion of reading withing an average lifespan</li>
  </ul>

  <p class="description-head">Description</p>

  <ul class="description">
    <li class="bullet_point">This project uses paid cloud storage to host content free to download.</li>
    <li class="bullet_point">Book organization is simply via alphbetical order in each category.</li>
    <li class="bullet_point">Google Analytics is intended to be used to measure this site's impact on the world.</li>
    <li class="bullet_point"><strong>If using Chrome,</strong> it is recommended to <a href="https://chrome.google.com/webstore/detail/pdf-viewer/oemmndcbldboiebfnladdacbdfmadadm/">install this extension</a> to view pdfs rather than downloading them.</li>
  </ul>

  <h2 class="subsubtitle">
    <button class="menu_button"><span onclick="window.location='https://github.com/gndpwnd/free_books/'">Project Github</span></button>
    <button class="menu_button"><span onclick="window.location='https://github.com/gndpwnd'">Author</span></button>
  </h2>

  </body>
</html>

'''