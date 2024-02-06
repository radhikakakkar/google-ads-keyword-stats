<html>

  <head>
    <title>Test form to get parameter data</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
      crossorigin="anonymous"
    />
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://code.jquery.com/jquery-3.7.1.js"
      integrity="sha256-eKhayi8LEQwp4NKxN+CfCh+3qOVUtJn3QNZ0TciWLP4="
      crossorigin="anonymous"
    ></script>
  </head>
  <style>
    body {
      margin: 10%;
    }
  </style>
  <body>
    
  <?php
 
    if (isset($_POST["submitButton"])) {
        $target_keyword1 = $_POST["targetKeyword1"];
        $target_keyword2 = $_POST["targetKeyword2"];
        $filename = "main.py";
        // $python = // the exact path of the python executable on the server
        //installig google ads on server
        exec("python3 $filename $target_keyword1", $output1);
        echo "<b>Results for $target_keyword1</b>: <br>" . nl2br(implode("\n", $output1));
        exec("python3 $filename $target_keyword2", $output2);
        
        echo "<br><b>Results for $target_keyword2</b>: <br> " . nl2br(implode("\n", $output2));
    }
  ?>

  <form action="" method="post">
      <div class="mb-3">
        <label for="target-keyword-input" class="form-label"
          >Target Keyword 1</label
        >
        <input class="form-control" id="target-keyword-input" name="targetKeyword1"/>
        <div id="email-help" class="form-text">
          Add the first keyword most relevant to your search
        </div>
        <label for="target-keyword-input" class="form-label"
          >Target Keyword 2</label
        >
        <input class="form-control" id="target-keyword-input" name="targetKeyword2"/>
        <div id="email-help" class="form-text">
          Add the second keyword most relevant to your search
        </div>
      </div>
      <!-- <div class="mb-3">
        <label for="current-city-input" class="form-label">Current City</label>
        <input class="form-control" id="current-city-input" />
      </div> -->
     
      <button name="submitButton" value="done" type="submit" class="btn btn-primary">Get Keyword metrics</button>
    </form>
    
  </body>

</html>
