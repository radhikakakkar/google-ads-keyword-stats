import sys
from google.ads.googleads.client import GoogleAdsClient
# from google.ads.google_ads.errors import GoogleAdsException


client = GoogleAdsClient.load_from_storage("google-ads.yaml")

# def get_location_code(country_name):

#     gtc_service = client.get_service("GeoTargetConstantService")
#     gtc_request = client.get_type("SuggestGeoTargetConstantsRequest")

#     gtc_request.locale = "en"
#     gtc_request.country_code = country_name

#     # The location names to get suggested geo target constants.
#     gtc_request.location_names.names.extend("New Jersey")

#     results = gtc_service.suggest_geo_target_constants(gtc_request)

#     # print(results)

#     # for suggestion in results.geo_target_constant_suggestions:
#     #     # print({suggestion.id})
#     #     # print(f"{suggestion}")
#     #     geo_target_constant = suggestion.geo_target_constant_parents
#     #     print(
#     #         f"{geo_target_constant.id}"
#     #     #     f"{geo_target_constant.resource_name} "
#     #     #     f"{geo_target_constant.name} "
#     #         # f"{geo_target_constant.country_code}, "
#     # #         f"is found in locale ({suggestion.locale}) "
#     # #         f"with reach ({suggestion.reach}) "
#     # #         f"from search term ({suggestion.search_term})."
#     #     )
#     # return results.geo_target_constant.country_code
#     # for fields in results.geo_target_constant_parents:
#     print(f"{results.geo_target_constant_suggestions.geo_target_constant_parents.id}") 


def get_keyword_details(target_keyword):
   
    
    googleads_service = client.get_service("GoogleAdsService")
    keyword_plan_idea_service = client.get_service("KeywordPlanIdeaService")

    # get_location_code(current_city)
    request = client.get_type("GenerateKeywordHistoricalMetricsRequest")
    request.customer_id = '8830496594'
    request.keywords = {target_keyword}

   
    # request.keyword_plan_network = (
    #     client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH
    # )
    # curr_location_code = 
    # get_location_code(country_name)

    # Geo target constant 2840 is for USA.
    # request.geo_target_constants.append(
    #     googleads_service.geo_target_constant_path("2840")
    # )
    response = keyword_plan_idea_service.generate_keyword_historical_metrics(request=request)

    for result in response.results:
        metrics = result.keyword_metrics
        low_usd = (metrics.low_top_of_page_bid_micros)/1000000
        high_usd = (metrics.high_top_of_page_bid_micros)/1000000

        print(f"\t Approximate monthly searches: {metrics.avg_monthly_searches}")

        # Top of page bid low range (20th percentile) in micros for the keyword.
        print(f"\t Top of page bid low range: {low_usd}")

        # Top of page bid high range (80th percentile) in micros for the keyword.
        print(f"\t Top of page bid high range: {high_usd}")
        
        print(f"\t Competition index: {metrics.competition_index}")
        

if __name__ == '__main__':

    if len(sys.argv) >= 1:
        target_keyword = sys.argv[1]
    
        # country_name = "US"
    else:
        print("Arguments not enough")
    get_keyword_details(target_keyword)