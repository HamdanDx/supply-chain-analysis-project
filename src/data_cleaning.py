import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def clean_column_names(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace("(", "", regex = False)
        .str.replace(")", "", regex = False)
        .str.replace(" ", "_")
        
    )
    return df

def convert_dates(df: pd.DataFrame) -> pd.DataFrame:
    # Changed pd.datetime to pd.to_datetime to avoid future errors
    df['order_date'] = pd.to_datetime(df['order_date_dateorders'])
    df['shipping_date'] = pd.to_datetime(df['shipping_date_dateorders'])
    return df

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    # We are dropping columns which are not useful:
    cols_to_drop = [
        'customer_email',
        'customer_password',
        'product_description',
        'product_image',
        'customer_street',
        'customer_fname',
        'customer_lname',
        'customer_zipcode',
        'order_zipcode',
        'longitude',
        'latitude',
        'order_item_cardprod_id',
        'order_item_discount',
        'order_item_discount_rate',
        'order_item_id',
        'order_item_product_price',
        'order_item_quantity',
        'order_item_total',
        'category_id',
        'department_id',
        'order_it',
        'order_customer_id',
        'customer_id',
        'product_card_id',
        'product_category_id',
        'benefit_per_order',
        'product_status',
        'customer_city',
        'order_city',
        'order_country',
        'order_state',
        'customer_state',
        'market'
        
    ]
    df = df.drop(columns=cols_to_drop, errors='ignore')
    return df

    # Removing cancelled orders since they are not relevant for delivery time analysis and may have different patterns than completed orders
def remove_cancelled_shipping(df):
    df = df[df['delivery_status'] != 'shipping_cancelled']
    return df

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    #calculate actual processing time
    df['order_processing_time'] = (df['shipping_date']- df['order_date']).dt.days
    #calculate delay
    df['delay'] = df['order_processing_time'] - df['days_for_shipment_scheduled']
    return df

def clean_pipeline(path: str) -> pd.DataFrame:
    df = load_data(path)
    df = clean_column_names(df)
    df = convert_dates(df)
    df = handle_missing_values(df)
    df = remove_cancelled_shipping(df)
    df = create_features(df)
    return df
