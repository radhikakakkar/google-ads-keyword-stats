<?php
header('Access-Control-Allow-Origin:  *');
    $filename = "main.py";
    $url = $_SERVER['REQUEST_URI']; 
    $url_components = parse_url($url);
    parse_str($url_components['query'], $params);
    if(isset($params['keywords'])) 
    {
        $keywords = $params['keywords'];
        if(!empty($keywords)){
            $keywords_array = explode(",", $params["keywords"]);
            // echo "number of keywords " . count($keywords_array);
            $filename = "Radhika_gads/main.py";
            foreach($keywords_array as $keyword) 
            {   
                // if($keyword = "") continue
                $output = []; 
                exec("python3 $filename $keyword", $output);
                echo "<br><b> Results for $keyword </b>: <br>" . nl2br(implode("\n", $output));
            }                
        }
        else
        {
            echo "The keywords are not provided correctly, please check";
        }
    }
    else
    {
        echo "No keywords are provided";
    }

?>



<!-- //debug statements
    // echo "Output from Python script: " . implode("\n", $output);
    // echo "Return code: $err"; -->