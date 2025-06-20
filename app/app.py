import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np

# Sample country data
countries_data = [
    ("USA", "North America", "USA", "🇺🇸"), ("Canada", "North America", "CAN", "🇨🇦"),
    ("Mexico", "North America", "MEX", "🇲🇽"), ("Brazil", "South America", "BRA", "🇧🇷"),
    ("Argentina", "South America", "ARG", "🇦🇷"), ("UK", "Europe", "GBR", "🇬🇧"),
    ("France", "Europe", "FRA", "🇫🇷"), ("Germany", "Europe", "DEU", "🇩🇪"),
    ("Italy", "Europe", "ITA", "🇮🇹"), ("Spain", "Europe", "ESP", "🇪🇸"), ("Russia", "Europe", "RUS", "🇷🇺"),
    ("India", "Asia", "IND", "🇮🇳"), ("China", "Asia", "CHN", "🇨🇳"), ("Japan", "Asia", "JPN", "🇯🇵"),
    ("South Korea", "Asia", "KOR", "🇰🇷"), ("Indonesia", "Asia", "IDN", "🇮🇩"),
    ("Australia", "Oceania", "AUS", "🇦🇺"), ("New Zealand", "Oceania", "NZL", "🇳🇿"),
    ("South Africa", "Africa", "ZAF", "🇿🇦"), ("Nigeria", "Africa", "NGA", "🇳🇬"),
    ("Egypt", "Africa", "EGY", "🇪🇬"), ("Kenya", "Africa", "KEN", "🇰🇪"), ("Turkey", "Asia", "TUR", "🇹🇷"),
    ("Saudi Arabia", "Asia", "SAU", "🇸🇦"), ("UAE", "Asia", "ARE", "🇦🇪"), ("Vietnam", "Asia", "VNM", "🇻🇳"),
    ("Thailand", "Asia", "THA", "🇹🇭"), ("Pakistan", "Asia", "PAK", "🇵🇰"), ("Bangladesh", "Asia", "BGD", "🇧🇩"),
    ("Ukraine", "Europe", "UKR", "🇺🇦"), ("Poland", "Europe", "POL", "🇵🇱"), ("Sweden", "Europe", "SWE", "🇸🇪"),
    ("Norway", "Europe", "NOR", "🇳🇴"), ("Finland", "Europe", "FIN", "🇫🇮"), ("Israel", "Asia", "ISR", "🇮🇱"),
    ("Iran", "Asia", "IRN", "🇮🇷"), ("Malaysia", "Asia", "MYS", "🇲🇾"), ("Philippines", "Asia", "PHL", "🇵🇭"),
    ("Colombia", "South America", "COL", "🇨🇴"), ("Chile", "South America", "CHL", "🇨🇱"),
    ("Peru", "South America", "PER", "🇵🇪"), ("Venezuela", "South America", "VEN", "🇻🇪"),
    ("Canada", "North America", "CAN", "🇨🇦"), ("Germany", "Europe", "DEU", "🇩🇪"),
    ("Netherlands", "Europe", "NLD", "🇳🇱"), ("Belgium", "Europe", "BEL", "🇧🇪"),
    ("Switzerland", "Europe", "CHE", "🇨🇭"), ("Austria", "Europe", "AUT", "🇦🇹"),
    ("Greece", "Europe", "GRC", "🇬🇷"), ("Portugal", "Europe", "PRT", "🇵🇹"),
    ("Ireland", "Europe", "IRL", "🇮🇪"), ("Denmark", "Europe", "DNK", "🇩🇰"),
    ("Czech Republic", "Europe", "CZE", "🇨🇿"), ("Hungary", "Europe", "HUN", "🇭🇺"),
    ("Romania", "Europe", "ROU", "🇷🇴"), ("Bulgaria", "Europe", "BGR", "🇧🇬"),
    ("Croatia", "Europe", "HRV", "🇭🇷"), ("Serbia", "Europe", "SRB", "🇷🇸"),
    ("Bosnia and Herzegovina", "Europe", "BIH", "🇧🇦"), ("Albania", "Europe", "ALB", "🇦🇱"),
    ("North Macedonia", "Europe", "MKD", "🇲🇰"), ("Slovenia", "Europe", "SVN", "🇸🇮"),
    ("Slovakia", "Europe", "SVK", "🇸🇰"), ("Lithuania", "Europe", "LTU", "🇱🇹"),
    ("Latvia", "Europe", "LVA", "🇱🇻"), ("Estonia", "Europe", "EST", "🇪🇪"),
    ("Belarus", "Europe", "BLR", "🇧🇾"), ("Moldova", "Europe", "MDA", "🇲🇩"),
    ("Kazakhstan", "Asia", "KAZ", "🇰🇿"), ("Uzbekistan", "Asia", "UZB", "🇺🇿"),
    ("Afghanistan", "Asia", "AFG", "🇦🇫"), ("Iraq", "Asia", "IRQ", "🇮🇶"),
    ("Syria", "Asia", "SYR", "🇸🇾"), ("Lebanon", "Asia", "LBN", "🇱🇧"),
    ("Jordan", "Asia", "JOR", "🇯🇴"), ("Yemen", "Asia", "YEM", "🇾🇪"),
    ("Oman", "Asia", "OMN", "🇴🇲"), ("Qatar", "Asia", "QAT", "🇶🇦"),
    ("Kuwait", "Asia", "KWT", "🇰🇼"), ("Bahrain", "Asia", "BHR", "🇧🇭"),
    ("Cyprus", "Asia", "CYP", "🇨🇾"), ("Georgia", "Asia", "GEO", "🇬🇪"),
    ("Armenia", "Asia", "ARM", "🇦🇲"), ("Azerbaijan", "Asia", "AZE", "🇦🇿"),
    ("Mongolia", "Asia", "MNG", "🇲🇳"), ("Nepal", "Asia", "NPL", "🇳🇵"),
    ("Sri Lanka", "Asia", "LKA", "🇱🇰"), ("Myanmar", "Asia", "MMR", "🇲🇲"),
    ("Laos", "Asia", "LAO", "🇱🇦"), ("Cambodia", "Asia", "KHM", "🇰🇭"),
    ("East Timor", "Asia", "TLS", "🇹🇱"), ("Singapore", "Asia", "SGP", "🇸🇬"),
    ("Brunei", "Asia", "BRN", "🇧🇳"), ("Papua New Guinea", "Oceania", "PNG", "🇵🇬"),
    ("Fiji", "Oceania", "FJI", "🇫🇯"), ("Solomon Islands", "Oceania", "SLB", "🇸🇧"),
    ("Vanuatu", "Oceania", "VUT", "🇻🇺"), ("Samoa", "Oceania", "WSM", "🇼🇸"),
    ("Tonga", "Oceania", "TON", "🇹🇴"), ("Kiribati", "Oceania", "KIR", "🇰🇮"),
    ("Micronesia", "Oceania", "FSM", "🇫🇲"), ("Marshall Islands", "Oceania", "MHL", "🇲🇭"),
    ("Palau", "Oceania", "PLW", "🇵🇼"), ("Nauru", "Oceania", "NRU", "🇳🇷"),
    ("Tuvalu", "Oceania", "TUV", "🇹🇻"), ("Algeria", "Africa", "DZA", "🇩🇿"),
    ("Morocco", "Africa", "MAR", "🇲🇦"), ("Tunisia", "Africa", "TUN", "🇹🇳"),
    ("Libya", "Africa", "LBY", "🇱🇾"), ("Sudan", "Africa", "SDN", "🇸🇩"),
    ("Ethiopia", "Africa", "ETH", "🇪🇹"), ("Somalia", "Africa", "SOM", "🇸🇴"),
    ("Eritrea", "Africa", "ERI", "🇪🇷"), ("Djibouti", "Africa", "DJI", "🇩🇯"),
    ("Uganda", "Africa", "UGA", "🇺🇬"), ("Rwanda", "Africa", "RWA", "🇷🇼"),
    ("Burundi", "Africa", "BDI", "🇧🇮"), ("Tanzania", "Africa", "TZA", "🇹🇿"),
    ("DR Congo", "Africa", "COD", "🇨🇩"), ("Congo", "Africa", "COG", "🇨🇬"),
    ("Gabon", "Africa", "GAB", "🇬🇦"), ("Cameroon", "Africa", "CMR", "🇨🇲"),
    ("Chad", "Africa", "TCD", "🇹🇩"), ("Niger", "Africa", "NER", "🇳🇪"),
    ("Mali", "Africa", "MLI", "🇲🇱"), ("Mauritania", "Africa", "MRT", "🇲🇷"),
    ("Senegal", "Africa", "SEN", "🇸🇳"), ("Gambia", "Africa", "GMB", "🇬🇲"),
    ("Guinea", "Africa", "GIN", "🇬🇳"), ("Sierra Leone", "Africa", "SLE", "🇸🇱"),
    ("Liberia", "Africa", "LBR", "🇱🇷"), ("Ivory Coast", "Africa", "CIV", "🇨🇮"),
    ("Ghana", "Africa", "GHA", "🇬🇭"), ("Togo", "Africa", "TGO", "🇹🇬"),
    ("Benin", "Africa", "BEN", "🇧🇯"), ("Burkina Faso", "Africa", "BFA", "🇧🇫"),
    ("Cape Verde", "Africa", "CPV", "🇨🇻"), ("Equatorial Guinea", "Africa", "GNQ", "🇬🇶"),
    ("Central African Republic", "Africa", "CAF", "🇨🇫"), ("South Sudan", "Africa", "SSD", "🇸🇸"),
    ("Zimbabwe", "Africa", "ZWE", "🇿🇼"), ("Zambia", "Africa", "ZMB", "🇿🇲"),
    ("Angola", "Africa", "AGO", "🇦🇴"), ("Mozambique", "Africa", "MOZ", "🇲🇿"),
    ("Madagascar", "Africa", "MDG", "🇲🇬"), ("Malawi", "Africa", "MWI", "🇲🇼"),
    ("Comoros", "Africa", "COM", "🇰🇲"), ("Mauritius", "Africa", "MUS", "🇲🇺"),
    ("Seychelles", "Africa", "SYC", "🇸🇨"), ("Botswana", "Africa", "BWA", "🇧🇼"),
    ("Namibia", "Africa", "NAM", "🇳🇦"), ("Lesotho", "Africa", "LSO", "🇱🇸"),
    ("Eswatini", "Africa", "SWZ", "🇸🇿"), ("Cuba", "North America", "CUB", "🇨🇺"),
    ("Dominican Republic", "North America", "DOM", "🇩🇴"), ("Haiti", "North America", "HTI", "🇭🇹"),
    ("Jamaica", "North America", "JAM", "🇯🇲"), ("Trinidad and Tobago", "North America", "TTO", "🇹🇹"),
    ("Bahamas", "North America", "BHS", "🇧🇸"), ("Belize", "North America", "BLZ", "🇧🇿"),
    ("Guatemala", "North America", "GTM", "🇬🇹"), ("Honduras", "North America", "HND", "🇭🇳"),
    ("El Salvador", "North America", "SLV", "🇸🇻"), ("Nicaragua", "North America", "NIC", "🇳🇮"),
    ("Costa Rica", "North America", "CRI", "🇨🇷"), ("Panama", "North America", "PAN", "🇵🇦"),
    ("Greenland", "North America", "GRL", "🇬🇱"), # Technically a constituent country of Denmark
    ("Iceland", "Europe", "ISL", "🇮🇸"), ("Andorra", "Europe", "AND", "🇦🇩"),
    ("San Marino", "Europe", "SMR", "🇸🇲"), ("Monaco", "Europe", "MCO", "🇲🇨"),
    ("Vatican City", "Europe", "VAT", "🇻🇦"), ("Malta", "Europe", "MLT", "🇲🇹"),
    ("Luxembourg", "Europe", "LUX", "🇱🇺"), ("Liechtenstein", "Europe", "LIE", "🇱🇮"),
    ("United Arab Emirates", "Asia", "ARE", "🇦🇪"), # Already listed as UAE, added full name for consistency
    ("Bhutan", "Asia", "BTN", "🇧🇹"), ("Maldives", "Asia", "MDV", "🇲🇻"),
    ("Timor-Leste", "Asia", "TLS", "🇹🇱"), # Already listed as East Timor, added full name for consistency
    ("Cambodia", "Asia", "KHM", "🇰🇭"), # Already listed
    ("Laos", "Asia", "LAO", "🇱🇦"), # Already listed
    ("Fiji", "Oceania", "FJI", "🇫🇯"), # Already listed
    ("Solomon Islands", "Oceania", "SLB", "🇸🇧"), # Already listed
    ("Vanuatu", "Oceania", "VUT", "🇻🇺"), # Already listed
    ("Samoa", "Oceania", "WSM", "🇼🇸"), # Already listed
    ("Tonga", "Oceania", "TON", "🇹🇴"), # Already listed
    ("Kiribati", "Oceania", "KIR", "🇰🇮"), # Already listed
    ("Micronesia", "Oceania", "FSM", "🇫🇲"), # Already listed
    ("Marshall Islands", "Oceania", "MHL", "🇲🇭"), # Already listed
    ("Palau", "Oceania", "PLW", "🇵🇼"), # Already listed
    ("Nauru", "Oceania", "NRU", "🇳🇷"), # Already listed
    ("Tuvalu", "Oceania", "TUV", "🇹🇻"), # Already listed
    ("Dominica", "North America", "DMA", "🇩🇲"),
    ("Saint Lucia", "North America", "LCA", "🇱🇨"),
    ("Saint Vincent and the Grenadines", "North America", "VCT", "🇻🇨"),
    ("Grenada", "North America", "GRD", "🇬🇩"),
    ("Antigua and Barbuda", "North America", "ATG", "🇦🇬"),
    ("Saint Kitts and Nevis", "North America", "KNA", "🇰🇳"),
    ("Barbados", "North America", "BRB", "🇧🇧"),
    ("Suriname", "South America", "SUR", "🇸🇷"),
    ("Guyana", "South America", "GUY", "🇬🇾"),
    ("Ecuador", "South America", "ECU", "🇪🇨"),
    ("Paraguay", "South America", "PRY", "🇵🇾"),
    ("Uruguay", "South America", "URY", "🇺🇾"),
    ("Bolivia", "South America", "BOL", "🇧🇴"),
    ("Chad", "Africa", "TCD", "🇹🇩"), # Already listed
    ("Eritrea", "Africa", "ERI", "🇪🇷"), # Already listed
    ("Djibouti", "Africa", "DJI", "🇩🇯"), # Already listed
    ("Comoros", "Africa", "COM", "🇰🇲"), # Already listed
    ("Sao Tome and Principe", "Africa", "STP", "🇸🇹"),
    ("Equatorial Guinea", "Africa", "GNQ", "🇬🇶"), # Already listed
    ("Burundi", "Africa", "BDI", "🇧🇮"), # Already listed
    ("Rwanda", "Africa", "RWA", "🇷🇼"), # Already listed
    ("Malawi", "Africa", "MWI", "🇲🇼"), # Already listed
    ("Lesotho", "Africa", "LSO", "🇱🇸"), # Already listed
    ("Eswatini", "Africa", "SWZ", "🇸🇿"), # Already listed
    ("Benin", "Africa", "BEN", "🇧🇯"), # Already listed
    ("Togo", "Africa", "TGO", "🇹🇬"), # Already listed
    ("Gambia", "Africa", "GMB", "🇬🇲"), # Already listed
    ("Guinea-Bissau", "Africa", "GNB", "🇬🇼"),
    ("Sierra Leone", "Africa", "SLE", "🇸🇱"), # Already listed
    ("Liberia", "Africa", "LBR", "🇱🇷"), # Already listed
    ("Côte d'Ivoire", "Africa", "CIV", "🇨🇮"), # Already listed as Ivory Coast
    ("Burkina Faso", "Africa", "BFA", "🇧🇫"), # Already listed
    ("Niger", "Africa", "NER", "🇳🇪"), # Already listed
    ("Mali", "Africa", "MLI", "🇲🇱"), # Already listed
    ("Mauritania", "Africa", "MRT", "🇲🇷"), # Already listed
    ("Western Sahara", "Africa", "ESH", "🇪🇭"), # Disputed territory
    ("South Georgia and the South Sandwich Islands", "Antarctica", "SGS", "🇬🇸"),
    ("French Southern Territories", "Antarctica", "ATF", "🇹🇫"),
    ("Heard Island and McDonald Islands", "Antarctica", "HMD", "🇭🇲"),
    # Note: Dependent territories, disputed territories, and very small island nations
    # often don't have UN-recognized ISO codes or universally agreed-upon continent classifications.
]

np.random.seed(42)
df = pd.DataFrame(countries_data, columns=["Country", "Continent", "ISO", "Emoji"])
df["Population (M)"] = np.random.randint(10, 1500, size=len(df))
df["GDP (Billion USD)"] = np.random.randint(50, 25000, size=len(df))
df["Life Expectancy"] = np.round(np.random.uniform(58, 85, size=len(df)), 1)

# Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])
server = app.server

app.layout = dbc.Container([
    html.H2("🌐 Global Demographic Insights", className="text-center text-light mt-4 mb-3"),

    dbc.Row([
        dbc.Col([
            html.Label("🌍 Select Continent", className="text-light"),
            dcc.Dropdown(
                id="continent-dropdown",
                options=[{"label": cont, "value": cont} for cont in sorted(df["Continent"].unique())],
                value="Asia", clearable=False
            )
        ], md=6),

        dbc.Col([
            html.Label("🔎 Select Country (optional)", className="text-light"),
            dcc.Dropdown(
                id="country-dropdown",
                options=[{"label": f"{row['Emoji']} {row['Country']}", "value": row["Country"]} for _, row in df.iterrows()],
                value=None, clearable=True, placeholder="Pick a country"
            )
        ], md=6)
    ], className="mb-4"),

    dbc.Row(id="summary-cards", className="mb-4"),
    dbc.Row([dbc.Col(dcc.Graph(id="map-chart"), md=12)], className="mb-4"),
    dbc.Row([
        dbc.Col(dcc.Graph(id="pop-bar"), md=6),
        dbc.Col(dcc.Graph(id="gdp-bar"), md=6),
    ])
], fluid=True, style={"backgroundColor": "#1e1e2f", "paddingBottom": "30px"})


@app.callback(
    Output("country-dropdown", "value"),
    Input("continent-dropdown", "value"),
    prevent_initial_call=True
)
def reset_country_on_continent_change(_):
    return None

    
@app.callback(
    Output("map-chart", "figure"),
    Output("pop-bar", "figure"),
    Output("gdp-bar", "figure"),
    Output("summary-cards", "children"),
    Input("continent-dropdown", "value"),
    Input("country-dropdown", "value")
)
def update_dashboard(selected_continent, selected_country):
    if selected_country:
        selected_df = df[df["Country"] == selected_country]
        if selected_df.empty:
            return dash.no_update

        country_data = selected_df.iloc[0]
        lat_center, lon_center = 20, 20  # Approx center
        projection_scale = 3.5

        fig_map = px.choropleth(
            selected_df,
            locations="ISO", color="Life Expectancy",
            hover_name="Country",
            hover_data=["Population (M)", "GDP (Billion USD)"],
            color_continuous_scale="Bluered",
            title=f"{country_data['Emoji']} {selected_country} — Life Expectancy"
        )
        fig_map.update_layout(
            geo=dict(
                projection_type="natural earth",
                center=dict(lat=lat_center, lon=lon_center),
                projection_scale=projection_scale,
                showland=True
            ),
            height=500,
            margin=dict(l=10, r=10, t=40, b=10)
        )

        pop_bar = px.bar(selected_df, x="Country", y="Population (M)", title="Population")
        gdp_bar = px.bar(selected_df, x="Country", y="GDP (Billion USD)", title="GDP")

        cards = dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardHeader(f"{country_data['Emoji']} {selected_country}"),
                dbc.CardBody([
                    html.H5("👥 Population", className="card-title"),
                    html.H4(f"{country_data['Population (M)']} M", className="text-info")
                ])
            ], color="dark", outline=True), md=4),

            dbc.Col(dbc.Card([
                dbc.CardHeader(f"{country_data['Emoji']} {selected_country}"),
                dbc.CardBody([
                    html.H5("💰 GDP", className="card-title"),
                    html.H4(f"${country_data['GDP (Billion USD)']:,} B", className="text-warning")
                ])
            ], color="dark", outline=True), md=4),

            dbc.Col(dbc.Card([
                dbc.CardHeader(f"{country_data['Emoji']} {selected_country}"),
                dbc.CardBody([
                    html.H5("🌱 Life Expectancy", className="card-title"),
                    html.H4(f"{country_data['Life Expectancy']} yrs", className="text-success")
                ])
            ], color="dark", outline=True), md=4),
        ])
        return fig_map, pop_bar, gdp_bar, cards

    # === If NO country selected, fallback to continent view ===
    filtered_df = df[df["Continent"] == selected_continent]

    fig_map = px.choropleth(
        filtered_df, locations="ISO", color="Life Expectancy",
        hover_name="Country",
        hover_data=["GDP (Billion USD)", "Population (M)"],
        color_continuous_scale="Viridis",
        title=f"Life Expectancy Across {selected_continent}"
    )
    fig_map.update_layout(
        geo=dict(
            projection_type="natural earth",
            center=dict(lat=10, lon=20),
            projection_scale=1,
            showland=True
        ),
        height=600,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    pop_bar = px.bar(
        filtered_df.sort_values(by="Population (M)", ascending=False),
        x="Country", y="Population (M)", title="Top Countries by Population"
    )
    gdp_bar = px.bar(
        filtered_df.sort_values(by="GDP (Billion USD)", ascending=False),
        x="Country", y="GDP (Billion USD)", title="Top Countries by GDP"
    )

    cards = dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader(f"{selected_continent}"),
            dbc.CardBody(html.H5(f"Total Population: {filtered_df['Population (M)'].sum()} M", className="text-info"))
        ], color="dark", outline=True), md=4),
        dbc.Col(dbc.Card([
            dbc.CardHeader(f"{selected_continent}"),
            dbc.CardBody(html.H5(f"Total GDP: ${filtered_df['GDP (Billion USD)'].sum():,} B", className="text-warning"))
        ], color="dark", outline=True), md=4),
        dbc.Col(dbc.Card([
            dbc.CardHeader(f"{selected_continent}"),
            dbc.CardBody(html.H5(f"Avg Life Expectancy: {round(filtered_df['Life Expectancy'].mean(), 1)} yrs", className="text-success"))
        ], color="dark", outline=True), md=4),
    ])
    return fig_map, pop_bar, gdp_bar, cards


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
