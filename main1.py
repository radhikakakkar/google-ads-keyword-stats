import sys
from google.ads.googleads.client import GoogleAdsClient
# from google.ads.google_ads.errors import GoogleAdsException

def get_keyword_details(campaign_id, target_keyword):

    google_ads_client = GoogleAdsClient.load_from_storage("google-ads.yaml")
    ga_service = google_ads_client.get_service("GoogleAdsService")

    query = f"""
        SELECT
            ad_group_criterion.criterion_id,
            ad_group_criterion.keyword.text,
            ad_group_criterion.keyword.match_type,
            ad_group_criterion.cpc_bid_micros
        FROM
            ad_group_criterion
        WHERE
            campaign.id = {campaign_id}
            AND ad_group_criterion.keyword.text = '{target_keyword}'

    """    
    response = ga_service.search(customer_id='8830496594', query=query)
    

    try: 
        for row in response:
            criterion_id = row.ad_group_criterion.criterion_id
            keyword_text = row.ad_group_criterion.keyword.text
            # match_type = row.ad_group_criterion.keyword.match_type
            cpc_bid_micros = row.ad_group_criterion.cpc_bid_micros
            # Convert micros to actual currency value (USD)
            cpc_bid = cpc_bid_micros / 1_000_000.0

            # print(f"Criterion ID: {criterion_id}")
            print(f"Keyword-name: {keyword_text}")
            print(f"Keyword-id: {criterion_id}")
            print(f"Keyword-cpc: {cpc_bid}")
            # print(f"Match Type: {match_type}")

    except:
        print("Exception")


if __name__ == '__main__':
    if len(sys.argv) > 2:
        campaign_id = sys.argv[1]
        target_keyword = sys.argv[2]
    else:
        print("arguments not enough")
    get_keyword_details(campaign_id, target_keyword)