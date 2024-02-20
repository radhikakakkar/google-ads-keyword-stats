
__ Google-ads.yaml __ - This file should be created as the first step in process of setting up google ads API in your app. Please refer to the template file here.

__ Form.php __ - This file takes in the user input and passes it to our python script for result computation. This is the file which is responsible for communicating with the API

__ Main.py __ - The file is importing the Google ads client and using the methods to produce results based on input i.e - Taking in keywords from the user and returning the stats available for it in the Google Keyword planner. These stats are currently independent of the location they are used in, this functionality can be added. The stats are also independent of any campaign or ad group. 

__ get_ads.php __ - This is an endpoint created to integrate the above in any app, the endpoint takes in user input in the form of URL parameters and proceeds with the computation.

Stats include - Approximate monthly searches, Top of page bid low range, Top of page bid high range and Competition index

