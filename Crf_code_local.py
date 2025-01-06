#!/usr/bin/env python
# coding: utf-8

# In[73]:


import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import os
# Initialize the Dash app
app = dash.Dash(__name__,suppress_callback_exceptions=True)

login_layout = html.Div(
    children=[
         html.H1("Login Page", style={"margin-bottom": "30px"}),
        html.Div(
            children=[
                html.Label("Sitename"),  # Label for username
                dcc.Input(
                    id="username-input",  # Same ID for functionality
                    type="text",
                    placeholder="Enter Sitename",
                    style={
                        "marginBottom": "10px",
                        "width": "100%",
                    },
                ),
                html.Label("Password"),  # Label for password
                dcc.Input(
                    id="password-input",  # Same ID for functionality
                    type="password",
                    placeholder="Enter Password",
                    style={
                        "marginBottom": "10px",
                        "width": "100%",
                    },
                ),
                dcc.Loading(
                    id="login-loading",  # Loading spinner for login
                    children=[
                        html.Button(
                            "Login",  # Changed button text to "Login"
                            id="login-button",  # Same ID for functionality
                            n_clicks=0,
                            style={
                                        "marginBottom": "10px",
                                        "width": "20%",
                                    },
                        ),
                    ],
                    type="default",
                ),
                html.Div(
                    id='login-feedback',  # Feedback message
                    style={
                        "align-self": "flex-end",
                        "color": "red",
                        "marginTop": "10px",
                    },
                ),
            ],
            style={
                "width": "300px",
                "padding": "20px",
                "border": "1px solid #ccc",  # Same border styling
                "borderRadius": "5px",
                "marginTop": "20px",
                "fontSize": "17px",
            },
        )
    ],
    style={
        "flex": "1",
        "display": "flex",
        "flexDirection": "column",
        "alignItems": "center",
        "justifyContent": "flex-start",
        "paddingTop": "50px",
    },
)

'''
file_path = "user_data.xlsx"

# Ensure the Excel file exists with the required columns
if not os.path.exists(file_path):
    pd.DataFrame(columns=["Site Name", "ID", "Age", "Gender", "Admission Date", 
                          "Primary Diagnosis", "Fever", "Cough", "Dyspnea"]).to_excel(file_path, index=False)
'''

# --- Callback for User Authentication ---
@app.callback(
    [Output('auth-state', 'data'), Output('url', 'pathname')],
    [Input('login-button', 'n_clicks')],
    [State('username-input', 'value'), State('password-input', 'value')],
    prevent_initial_call=True
)
def authenticate_user(n_clicks, username, password):
    # Validate credentials
    if username in ['s1', 's2', 'r'] and password == 'p':
        # Store user ID and redirect
        return username, '/login'  # Redirect to user details page
    return False, '/'  # Stay on login page if authentication fails

@app.callback(
    Output('login-feedback', 'children'),
    [Input('auth-state', 'data'),   # Authentication state
     Input('login-button', 'n_clicks')],  # Button clicks
    prevent_initial_call=True
)
def display_login_feedback(authenticated, n_clicks):
    # Check if the button has been clicked
    if n_clicks > 0:
        # Verify authentication
        if authenticated is True:  # Assuming 'authenticated' is True or False
            return "Login successful!"
        else:
            return "Invalid username or password"
    return ""

# Define the layout
app.layout = html.Div(
    children=[
        dcc.Store(id='auth-state'),
        dcc.Store(id='stored-id', data=None),
        dcc.Store(id='stored-user-data', data={}) ,
        # Header box
        html.Div(
            children="Case Report Form",
            style={
                "backgroundColor": "#000080",
                "color": "white",
                "padding": "10px",
                "textAlign": "center",
                "fontSize": "35px",
                "fontWeight": "bold",
            },
        ),
        # Main container with navigation and content
        html.Div(
            children=[
                # Navigation panel with pills/boxes
                html.Div(
                    children=[
                        html.Div(
                            dcc.Link(
                                "Patient Selection",
                                href="/login",
                                style={
                                    "textDecoration": "none",
                                    "color": "black",
                                    "display": "block",
                                    "textAlign": "center",
                                    "fontSize": "17px",
                                    "padding": "10px",
                                },
                            ),
                            style={
                                "backgroundColor": "#A7C7E7",
                                "borderRadius": "5px",
                                "marginBottom": "10px",
                                "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.2)",
                            },
                        ),
                        html.Div(
                            dcc.Link(
                                "Patient Information",
                                href="/section1",
                                style={
                                    "textDecoration": "none",
                                    "color": "black",
                                    "display": "block",
                                    "textAlign": "center",
                                    "fontSize": "17px",
                                    "padding": "10px",
                                },
                            ),
                            style={
                                "backgroundColor": "#A7C7E7",
                                "borderRadius": "5px",
                                "marginBottom": "10px",
                                "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.2)",
                            },
                        ),
                        html.Div(
                            dcc.Link(
                                "Initial Clinical Parameters",
                                href="/section2",
                                style={
                                    "textDecoration": "none",
                                    "color": "black",
                                    "display": "block",
                                    "textAlign": "center",
                                    "fontSize": "17px",
                                    "padding": "10px",
                                },
                            ),
                            style={
                                "backgroundColor": "#A7C7E7",
                                "borderRadius": "5px",
                                "marginBottom": "10px",
                                "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.2)",
                            },
                        ),
                         html.Div(
                            dcc.Link(
                                "Diagnostic and Randomization Details",
                                href="/section3",
                                style={
                                    "textDecoration": "none",
                                    "color": "black",
                                    "display": "block",
                                    "textAlign": "center",
                                    "fontSize": "17px",
                                    "padding": "10px",
                                },
                            ),
                            style={
                                "backgroundColor": "#A7C7E7",
                                "borderRadius": "5px",
                                "marginBottom": "10px",
                                "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.2)",
                            },
                        ),
                        html.Div(
                            dcc.Link(
                                "Treatment Details",
                                href="/section4",
                                style={
                                    "textDecoration": "none",
                                    "color": "black",
                                    "display": "block",
                                    "textAlign": "center",
                                    "fontSize": "17px",
                                    "padding": "10px",
                                },
                            ),
                            style={
                                "backgroundColor": "#A7C7E7",
                                "borderRadius": "5px",
                                "marginBottom": "10px",
                                "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.2)",
                            },
                        ),
                        html.Div(
                            dcc.Link(
                                "Clinical Progress and Outcomes",
                                href="/section5",
                                style={
                                    "textDecoration": "none",
                                    "color": "black",
                                    "display": "block",
                                    "textAlign": "center",
                                    "fontSize": "17px",
                                    "padding": "10px",
                                },
                            ),
                            style={
                                "backgroundColor": "#A7C7E7",
                                "borderRadius": "5px",
                                "marginBottom": "10px",
                                "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.2)",
                            },
                        ),
                        html.Div(
                            dcc.Link(
                                "Ancillary Test Results",
                                href="/section6",
                                style={
                                    "textDecoration": "none",
                                    "color": "black",
                                    "display": "block",
                                    "textAlign": "center",
                                    "fontSize": "17px",
                                    "padding": "10px",
                                },
                            ),
                            style={
                                "backgroundColor": "#A7C7E7",
                                "borderRadius": "5px",
                                "marginBottom": "10px",
                                "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.2)",
                            },
                        ),
                        html.Div(
                            dcc.Link(
                                "Antimicrobial Stewardship",
                                href="/section7",
                                style={
                                    "textDecoration": "none",
                                    "color": "black",
                                    "display": "block",
                                    "textAlign": "center",
                                    "fontSize": "17px",
                                    "padding": "10px",
                                },
                            ),
                            style={
                                "backgroundColor": "#A7C7E7",
                                "borderRadius": "5px",
                                "marginBottom": "10px",
                                "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.2)",
                            },
                        ),
                        html.Div(
                            dcc.Link(
                                "Cost-Benefit Analysis (Optional)",
                                href="/section8",
                                style={
                                    "textDecoration": "none",
                                    "color": "black",
                                    "display": "block",
                                    "textAlign": "center",
                                    "fontSize": "17px",
                                    "padding": "10px",
                                },
                            ),
                            style={
                                "backgroundColor": "#A7C7E7",
                                "borderRadius": "5px",
                                "marginBottom": "10px",
                                "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.2)",
                            },
                        ),
                        html.Div(
                            dcc.Link(
                                "Logout",
                                href="/logout",
                                style={
                                    "textDecoration": "none",
                                    "color": "black",
                                    "display": "block",
                                    "textAlign": "center",
                                    "fontSize": "17px",
                                    "padding": "10px",
                                },
                            ),
                            style={
                                "backgroundColor": "#A7C7E7",
                                "borderRadius": "5px",
                                "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.2)",
                            },
                        ),
                    ],
                    style={
                        "backgroundColor": "#E5E4E2",
                        "padding": "20px",
                        "width": "300px",
                        "height": "100vh",
                        "boxShadow": "2px 0px 5px rgba(0, 0, 0, 0.1)",
                    },
                ),
                # Content for different sections
                dcc.Location(id='url', refresh=False),

                html.Div(id='page-content', style={
                    "flex": "1",
                    "display": "flex",
                    "flexDirection": "column",
                    "alignItems": "center",
                    "justifyContent": "flex-start",
                    "paddingTop": "50px",
                }),
            ],
            style={"display": "flex"},
        ),
    ]
) 

    
@app.callback(
    [Output("existing-user-form", "style"),  # Show/hide the form
     Output("existing-user-id", "options")],  # Populate dropdown options
    [Input("user-type", "value"),            # Radio button input
     State("auth-state", "data")]            # User ID from login session
)
def toggle_user_form(user_type, user_id):
    # Path to Excel file
    file_path = "user_data.xlsx"
    
    # Check if the user type is "existing" and the file exists
    if user_type == "existing" and os.path.exists(file_path):
        # Read Excel file
        data = pd.read_excel(file_path)

        # Filter rows based on logged-in User ID
        filtered_data = data[data["Site Name"] == user_id]  # Match logged-in user ID
        
        # Extract unique patient IDs for the logged-in user
        patient_ids = filtered_data["ID"].dropna().unique()
        
        # Create dropdown options
        options = [{"label": str(pid), "value": str(pid)} for pid in patient_ids]
        
        # Show the form and populate options
        return {"display": "block"}, options

    # Hide the form if not "existing" or file doesn't exist
    return {"display": "none"}, []


# Define callbacks for page navigation
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')],
              [State('auth-state', 'data')])
def display_page(pathname, authenticated):
    # Redirect unauthenticated users to login
    if not authenticated:
        return login_layout

    if pathname == '/login2':  # For Login page
        return login_layout

    # After login, handle navigation
    elif pathname == '/login':  # Radio buttons for new/existing user
        return html.Div([
            html.H1("Patient Selection", style={"margin-bottom": "40px"}),

            # Radio button for New/Existing User
            dcc.RadioItems(
                id="user-type",
                options=[
                    {"label": "New User", "value": "new"},
                    {"label": "Existing User", "value": "existing"}
                ],
                value="new",
                labelStyle={"display": "block", "margin-bottom": "15px"}
            ),

            # Existing user dropdown and update button
            html.Div(id="existing-user-form", style={"display": "none"}, children=[
                html.Label("Select Patient ID:"),
                dcc.Dropdown(id="existing-user-id", placeholder="Select Patient ID"),
            ]),
            html.Button("Next Page >>", id="next-page-button", n_clicks=0, style={
            "fontFamily": "Times New Roman, serif",
            "fontSize": "15px",
            "position": "absolute",
            #"bottom": "450px",
            "right": "500px",
            "margin-top": "10px",
            "background-color": "#000080",
            "color": "white",
            "border": "none",
            "padding": "10px 20px",
            "borderRadius": "5px",
            "cursor": "pointer"
        }),
        ])

    elif pathname == '/section1':
         return html.Div([
            html.H1("Patient Information", style={"margin-bottom": "40px"}),
        # ID Input
        html.Div([
            html.Label("ID:", style={"margin-right": "10px"}),
            dcc.Input(id="input-id", type="text", placeholder="Enter ID")
        ], style={"margin-bottom": "10px", "display": "flex", "align-items": "center"}),

        # Age Input
        html.Div([
            html.Label("Age:", style={"margin-right": "10px"}),
            dcc.Input(id="input-age", type="number", placeholder="Enter Age", min=18, max=65)
        ], style={"margin-bottom": "10px", "display": "flex", "align-items": "center"}),

        # Gender Dropdown
         html.Div([
            html.Label("Gender:", style={"margin-right": "10px"}),
            dcc.Dropdown(
                id="input-gender",
                options=[
                    {"label": "Male", "value": "Male"},
                    {"label": "Female", "value": "Female"},
                ],
                placeholder="Select Gender",
                style={"width": "200px"}
            )
        ], style={"margin-bottom": "10px", "display": "flex", "align-items": "center"}),

        # Admission Date Picker
         html.Div([
            html.Label("Admission Date:", style={"margin-right": "10px"}),
            dcc.DatePickerSingle(
                id="input-admission-date", 
                placeholder="Select Admission Date",
                style={"width": "150px"},
                max_date_allowed='2025-12-31',
                initial_visible_month='2024-12'
            )
        ], style={"margin-bottom": "10px", "display": "flex", "align-items": "center"}),

        # Primary Diagnosis Input
        html.Div([
            html.Label("Primary Diagnosis:", style={"margin-right": "10px"}),
            dcc.Input(id="input-primary-diagnosis", type="text", placeholder="Enter Diagnosis")
        ], style={"margin-bottom": "10px", "display": "flex", "align-items": "center"}),

        # Save Button
        html.Div(
            html.Button(
                "Save", 
                id="save-section1", 
                n_clicks=0, 
                style={
                    "fontFamily": "Times New Roman, serif",
                    "fontSize": "15px",
                    "border": "none",
                    "padding": "10px 20px",
                    "borderRadius": "5px",
                    "cursor": "pointer",
                    "backgroundColor": "#4CAF50",  # Optional: Green color for Save button
                    "color": "white"
                }
            ),
            style={
                "display": "flex",             # Use flexbox for layout
                "justifyContent": "flex-start", # Align to the left
                "alignItems": "center",        # Vertically center
                "marginTop": "20px",           # Top margin
                "marginLeft": "50px"          # Move slightly to the left (adjust value as needed)
            }
        ),

        # Message Section
        html.Div(id="section1-message", style={"marginTop": "20px", "color": "green"}),

        # Navigation Buttons
        html.Button("Next Page >>", id="next-to-section2", n_clicks=0, style={
            "fontFamily": "Times New Roman, serif",
            "fontSize": "15px",
            "position": "absolute",
            #"bottom": "350px",
            "right": "350px",
            "background-color": "#000080",
            "color": "white",
            "border": "none",
            "padding": "10px 20px",
            "borderRadius": "5px",
            "cursor": "pointer"
        }),
        html.Button("<< Previous Page", id="prev-to-login", n_clicks=0, style={
            "fontFamily": "Times New Roman, serif",
            "fontSize": "15px", 
            "position": "absolute",
            #"bottom": "350px",
            "left": "550px",
            "background-color": "#000080",
            "color": "white",
            "border": "none",
            "padding": "10px 20px",
            "borderRadius": "5px",
            "cursor": "pointer"
        }),
    ])
    elif pathname == '/section2':
        return html.Div([
                        html.H1("Initial Clinical Parameters"),
        html.Div([
            html.Label("Fever:"),
            dcc.Checklist(
                id="input-fever",
                options=[
                    {"label": "Yes", "value": "Yes"},
                    {"label": "No", "value": "No"},
                ],labelStyle={"display": "inline-block", "margin-right": "10px"}
            )
        ], style={"display": "flex", "align-items": "center","margin-bottom": "10px"}),

        html.Div([
            html.Label("Cough:"),
            dcc.Checklist(
                id="input-cough",
                options=[
                    {"label": "Yes", "value": "Yes"},
                    {"label": "No", "value": "No"},
                ],labelStyle={"display": "inline-block", "margin-right": "10px"}
            )
        ], style={"display": "flex", "align-items": "center","margin-bottom": "10px"}),

        html.Div([
            html.Label("Dyspnea:"),
            dcc.Checklist(
                id="input-dyspnea",
                options=[
                    {"label": "Yes", "value": "Yes"},
                    {"label": "No", "value": "No"},
                ],labelStyle={"display": "inline-block", "margin-right": "10px"}
            )
        ], style={"display": "flex", "align-items": "center","margin-bottom": "10px"}),

        html.Div(
            html.Button(
                "Save", 
                id="save-section2", 
                n_clicks=0, 
                style={
                    "fontFamily": "Times New Roman, serif",
                    "fontSize": "15px",
                    "border": "none",
                    "padding": "10px 20px",
                    "borderRadius": "5px",
                    "cursor": "pointer",
                    "backgroundColor": "#4CAF50",  # Optional: Green color for Save button
                    "color": "white"
                }
            ),
            style={
                "display": "flex",             # Use flexbox for layout
                "justifyContent": "flex-start", # Align to the left
                "alignItems": "center",        # Vertically center
                "marginTop": "20px",           # Top margin
                "marginLeft": "50px"          # Move slightly to the left (adjust value as needed)
            }
        ),
        html.Div(id="section2-message", style={"marginTop": "20px", "color": "green"}),
        html.Button("Next Page >>", id="next-to-section3", n_clicks=0, style={
            "fontFamily": "Times New Roman, serif",
            "fontSize": "15px",
            "position": "absolute",
           # "bottom": "350px",
            "right": "350px",
            "background-color": "#000080",
            "color": "white",
            "border": "none",
            "padding": "10px 20px",
            "borderRadius": "5px",
            "cursor": "pointer"
        }),
         html.Button("<< Previous Page", id="prev-to-section1", n_clicks=0, style={
             "fontFamily": "Times New Roman, serif",
             "fontSize": "15px",
            "position": "absolute",
           # "bottom": "350px",
            "left": "500px",
            "background-color": "#000080",
            "color": "white",
            "border": "none",
            "padding": "10px 20px",
            "borderRadius": "5px",
            "cursor": "pointer"
        }),
    ])
    elif pathname == '/section3':
        return html.Div([
            html.H1("Diagnostic and Randomization Details", style={"margin-bottom": "40px"}),
    
            # BAL Performed
            html.Div([
                html.Label("1. Bronchoalveolar Lavage (BAL) Performed:"),
                dcc.RadioItems(
                    id="bal-performed",
                    options=[
                        {"label": "Yes", "value": "Yes"},
                        {"label": "No", "value": "No"}
                    ],
                    labelStyle={"display": "inline-block", "margin-right": "20px"},
                    value="No"
                ),
                dcc.DatePickerSingle(
                    id="bal-date",
                    placeholder="If Yes, select date",
                    style={"margin-top": "10px"}
                )
            ], style={"display": "flex", "align-items": "center", "margin-bottom": "20px"}),
    
            # Randomization Group
            html.Div([
                html.Label("2. Randomization Group:", style={"margin-right": "20px"}),
                dcc.RadioItems(
                    id="randomization-group",
                    options=[
                        {"label": "Film Array Group", "value": "Film Array"},
                        {"label": "Standard of Care Group", "value": "Standard of Care"}
                    ],
                    labelStyle={"display": "inline-block", "margin-right": "30px"}
                )
            ], style={"display": "flex", "align-items": "center", "margin-bottom": "20px"}),
    
            # BAL Results
            html.Div([
                html.Label("3. BAL Results:", style={"margin-bottom": "20px"}),
            
                # BioFire Panel Results
                html.Div([
                    html.Label("BioFire Panel Results:", style={"width": "200px", "margin-right": "10px"}),
                    dcc.Input(
                        id="biofire-results",
                        type="text",
                        placeholder="Enter BioFire Panel Results",
                        style={"flex": "1"}
                    )
                ], style={"display": "flex", "align-items": "center", "margin-bottom": "10px","margin-top": "20px"}),
            
                # Culture Results
                html.Div([
                    html.Label("Culture Results:", style={"width": "200px", "margin-right": "10px"}),
                    dcc.Input(
                        id="culture-results",
                        type="text",
                        placeholder="Enter Culture Results",
                        style={"flex": "1"}
                    )
                ], style={"display": "flex", "align-items": "center", "margin-bottom": "10px"}),
            
                # Resistance Genes Detected
                html.Div([
                    html.Label("Resistance Genes Detected:", style={"width": "200px", "margin-right": "10px"}),
                    dcc.Input(
                        id="resistance-genes",
                        type="text",
                        placeholder="Enter Resistance Genes Detected",
                        style={"flex": "1"}
                    )
                ], style={"display": "flex", "align-items": "center", "margin-bottom": "10px"})
            ])     
            , 
            # Save Button
            html.Button("Save", id="save-section3", n_clicks=0, style={
                "fontFamily": "Times New Roman, serif",
                "fontSize": "15px",
                "background-color": "#4CAF50",
                "color": "white",
                "border": "none",
                "padding": "10px 20px",
                "borderRadius": "5px",
                "cursor": "pointer",
                "margin-top": "20px",
                "marginLeft": "60px"
            }),
    
            # Message Section
            html.Div(id="section3-message", style={"marginTop": "20px", "color": "green"}),
            html.Button("Next Page >>", id="next-to-section4", n_clicks=0, style={
            "fontFamily": "Times New Roman, serif",
            "fontSize": "15px",
            "position": "absolute",
           # "bottom": "350px",
            "right": "350px",
            "background-color": "#000080",
            "color": "white",
            "border": "none",
            "padding": "10px 20px",
            "borderRadius": "5px",
            "cursor": "pointer"
        }),
         html.Button("<< Previous Page", id="prev-to-section2", n_clicks=0, style={
             "fontFamily": "Times New Roman, serif",
             "fontSize": "15px",
            "position": "absolute",
           # "bottom": "350px",
            "left": "500px",
            "background-color": "#000080",
            "color": "white",
            "border": "none",
            "padding": "10px 20px",
            "borderRadius": "5px",
            "cursor": "pointer"
        }),
        ])
    elif pathname == '/section4':
        return html.Div([
            html.H1("Treatment Details")
        ])
    elif pathname == '/section5':
        return html.Div([
            html.H1("Clinical Progress and Outcomes")
        ])
    elif pathname == '/section6':
        return html.Div([
            html.H1("Ancillary Test Results")
        ])
    elif pathname == '/section7':
        return html.Div([
            html.H1("Antimicrobial Stewardship")
        ])
    elif pathname == '/section8':
        return html.Div([
            html.H1("Cost-Benefit Analysis (Optional)")
        ])
    elif pathname == '/logout':
        return dcc.Location(href="/login2", id="redirect-login2")
    else:
        return html.H3("404 Page Not Found")




@app.callback(
    Output('url', 'pathname', allow_duplicate=True),
    Input('next-page-button', 'n_clicks'),
    State('user-type', 'value'),
    prevent_initial_call=True
)
def go_to_section1(n_clicks, user_type):
    if user_type == "existing":  # Existing user
        return '/section1'
    return '/section1'  # Redirect for new user as well


@app.callback(
    Output('url', 'pathname', allow_duplicate=True),
    Input('next-to-section2', 'n_clicks'),
    prevent_initial_call=True
)
def go_to_section2(n_clicks):
    return '/section2'


@app.callback(
    Output('url', 'pathname', allow_duplicate=True),
    Input('next-to-section3', 'n_clicks'),
    prevent_initial_call=True
)
def go_to_section3(n_clicks):
    return '/section3'

@app.callback(
    Output('url', 'pathname', allow_duplicate=True),
    Input('next-to-section4', 'n_clicks'),
    prevent_initial_call=True
)
def go_to_section3(n_clicks):
    return '/section4'

@app.callback(
    Output('url', 'pathname', allow_duplicate=True),
    Input('prev-to-section2', 'n_clicks'),
    prevent_initial_call=True
)
def go_to_section3(n_clicks):
    return '/section2'
    

@app.callback(
    Output('url', 'pathname', allow_duplicate=True),  # Redirect to Login
    Input('prev-to-login', 'n_clicks'),
    prevent_initial_call=True
)
def go_to_login2(n_clicks):
    return '/login'

@app.callback(
    Output('url', 'pathname', allow_duplicate=True),  # Redirect to Login
    Input('prev-to-section1', 'n_clicks'),
    prevent_initial_call=True
)
def go_to_login(n_clicks):
    return '/section1'
    


@app.callback(
    [Output('section1-message', 'children'), 
     Output('stored-id', 'data'),
     Output('stored-user-data', 'data', allow_duplicate=True)],
    Input('save-section1', 'n_clicks'),
    [State('input-id', 'value'),
     State('input-age', 'value'),
     State('input-gender', 'value'),
     State('input-admission-date', 'date'),
     State('input-primary-diagnosis', 'value'),
     State('auth-state', 'data'),  # User ID as Site Name
     State('stored-user-data', 'data')],
    prevent_initial_call=True
)
def save_section1(n_clicks, input_id, age, gender, admission_date, diagnosis, user_id, stored_data):
    # Validate required fields
    if not all([input_id, age, gender, admission_date, diagnosis]):
        return html.Span("", style={"color": "red"}), None, stored_data

    # Normalize inputs
    input_id = str(input_id).strip().lower()
    age = int(age)
    admission_date = str(admission_date)

    # File path
    file_path = "user_data.xlsx"

    try:
        # Load or create Excel file
        if os.path.exists(file_path):
            data = pd.read_excel(file_path, dtype={"ID": str})
        else:
            data = pd.DataFrame(columns=["Site Name", "ID", "Age", "Gender", "Admission Date", "Primary Diagnosis"])

        # Normalize IDs in data
        data['ID'] = data['ID'].astype(str).str.strip().str.lower()
        
        if input_id in data[(data['Site Name'] == user_id)]['ID'].astype(str).values:
        # Check if stored_data is empty or has a conflicting ID
            if not stored_data or stored_data.get("ID") != input_id:
                return html.Span(
                    "Error: ID already exists for the same Site Name. Please use a different ID.",
                    style={"color": "red"}
                ), None, stored_data

        # --- Check if record already exists for the current user (Site Name) and ID ---
        user_record = data[(data['ID'] == input_id) & (data['Site Name'] == user_id)]
        
        # --- Case 1: Record exists (UPDATE logic) ---
        if not user_record.empty:
            index = user_record.index[0]  # Get the row index of the existing record

            # Check if stored data matches the new data (no changes detected)
            if stored_data and stored_data.get("ID") == input_id and stored_data.get("Site Name") == user_id:
                if (stored_data.get("Age") == age and
                    stored_data.get("Gender") == gender and
                    stored_data.get("Admission Date") == admission_date and
                    stored_data.get("Primary Diagnosis") == diagnosis):
                    return "Section 1 data already saved!", input_id, stored_data

            # Update the existing record
            data.loc[index, ['Age', 'Gender', 'Admission Date', 'Primary Diagnosis']] = [
                age, gender, admission_date, diagnosis
            ]

        # --- Case 2: New record (CREATE logic) ---
        else:
            new_row = {
                "Site Name": user_id,
                "ID": input_id,
                "Age": age,
                "Gender": gender,
                "Admission Date": admission_date,
                "Primary Diagnosis": diagnosis
            }
            data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)

        # Save data to Excel
        data.to_excel(file_path, index=False)

        # Update stored data
        stored_data = {
            "Site Name": user_id,
            "ID": input_id,
            "Age": age,
            "Gender": gender,
            "Admission Date": admission_date,
            "Primary Diagnosis": diagnosis
        }

        return "Data saved successfully!", input_id, stored_data

    except Exception as e:
        return html.Span(f"Error: {str(e)}", style={"color": "red"}), None, stored_data




@app.callback(
    [Output('section2-message', 'children'),
     Output('stored-user-data', 'data', allow_duplicate=True)],
    Input('save-section2', 'n_clicks'),
    [State('stored-id', 'data'),
     State('input-fever', 'value'),
     State('input-cough', 'value'),
     State('input-dyspnea', 'value'),
     State('stored-user-data', 'data'),
     State('auth-state', 'data')],  # Include Site Name
    prevent_initial_call=True
)
def save_section2(n_clicks, stored_id, fever, cough, dyspnea, stored_data, user_id):
    # Validate ID
    if not stored_id:
        return html.Span("User ID is missing. Save previous page first!", 
                         style={"color": "red"}), stored_data

    # Ensure at least one field is filled or blank updates are required
    if fever is None and cough is None and dyspnea is None:
        return "", stored_data

    # File path
    file_path = "user_data.xlsx"

    try:
        # Load or create Excel file
        if os.path.exists(file_path):
            # Load data and normalize columns
            data = pd.read_excel(file_path, dtype={"ID": str})
            data['ID'] = data['ID'].astype(str).str.strip().str.lower()
            data['Site Name'] = data['Site Name'].astype(str).str.strip().str.lower()

            # Normalize inputs for comparison
            stored_id = str(stored_id).strip().lower()
            user_id = str(user_id).strip().lower()

            # --- Check for matching Site Name and ID ---
            user_record = data[(data['ID'] == stored_id) & (data['Site Name'] == user_id)]

            # --- Update existing user data ---
            if not user_record.empty:
                index = user_record.index[0]
                data.loc[index, 'Fever'] = fever[0] if fever else None
                data.loc[index, 'Cough'] = cough[0] if cough else None
                data.loc[index, 'Dyspnea'] = dyspnea[0] if dyspnea else None

                # Save updated data
                data.to_excel(file_path, index=False)

                # Update stored-user-data
                stored_data.update({
                    "Fever": fever[0] if fever else None,
                    "Cough": cough[0] if cough else None,
                    "Dyspnea": dyspnea[0] if dyspnea else None
                })

                return "Section 2 data saved successfully!", stored_data

            # --- Handle missing ID for the user ---
            else:
                return html.Span("Error: User ID not found! Save previous page first.", 
                                 style={"color": "red"}), stored_data
        else:
            return html.Span("Error: No data file found! Save previous page first.", 
                             style={"color": "red"}), stored_data

    except Exception as e:
        return html.Span(f"Error: {str(e)}", style={"color": "red"}), stored_data

@app.callback(
    [Output('section3-message', 'children'),
     Output('stored-user-data', 'data', allow_duplicate=True)],
    Input('save-section3', 'n_clicks'),
    [State('stored-id', 'data'),
     State('bal-performed', 'value'),
     State('bal-date', 'date'),
     State('randomization-group', 'value'),
     State('biofire-results', 'value'),
     State('culture-results', 'value'),
     State('resistance-genes', 'value'),
     State('stored-user-data', 'data'),
     State('auth-state', 'data')],  # Include Site Name for filtering
    prevent_initial_call=True
)
def save_section3(n_clicks, stored_id, bal_performed, bal_date, random_group, biofire_results, culture_results, resistance_genes, stored_data, user_id):
    # Ensure the callback only runs if the button has been clicked
    if n_clicks is None or n_clicks == 0:
        return "", stored_data  # Don't show anything or modify data until the button is clicked

    # Validate ID
    if not stored_id:
        return html.Span("User ID is missing. Save previous page first!", style={"color": "red"}), stored_data

    # File path
    file_path = "user_data.xlsx"

    try:
        # Load or create Excel file
        if os.path.exists(file_path):
            # Load data and normalize columns
            data = pd.read_excel(file_path, dtype={"ID": str})
            data['ID'] = data['ID'].astype(str).str.strip().str.lower()
            data['Site Name'] = data['Site Name'].astype(str).str.strip().str.lower()

            # Normalize inputs for comparison
            stored_id = str(stored_id).strip().lower()
            user_id = str(user_id).strip().lower()

            # Check for matching Site Name and ID
            user_record = data[(data['ID'] == stored_id) & (data['Site Name'] == user_id)]

            # Update existing user data
            if not user_record.empty:
                index = user_record.index[0]
                data.loc[index, 'BAL Performed'] = bal_performed
                data.loc[index, 'BAL Date'] = bal_date
                data.loc[index, 'Randomization Group'] = random_group
                data.loc[index, 'BioFire Panel Results'] = biofire_results
                data.loc[index, 'Culture Results'] = culture_results
                data.loc[index, 'Resistance Genes Detected'] = resistance_genes

                # Save updated data
                data.to_excel(file_path, index=False)

                # Update stored-user-data
                stored_data.update({
                    "BAL Performed": bal_performed,
                    "BAL Date": bal_date,
                    "Randomization Group": random_group,
                    "BioFire Panel Results": biofire_results,
                    "Culture Results": culture_results,
                    "Resistance Genes Detected": resistance_genes
                })

                return "Section 3 data saved successfully!", stored_data

            # Handle missing ID for the user
            else:
                return html.Span("Error: User ID not found! Save Section 1 first.", style={"color": "red"}), stored_data

        else:
            return html.Span("Error: No data file found! Save Section 1 first.", style={"color": "red"}), stored_data

    except Exception as e:
        return html.Span(f"Error: {str(e)}", style={"color": "red"}), stored_data


@app.callback(
    Output('stored-user-data', 'data'),  # Store user data globally
    Input('existing-user-id', 'value')  # Selected user ID
)
def load_user_data(user_id):
    if user_id:
        file_path = "user_data.xlsx"
        if os.path.exists(file_path):
            # Read Excel and enforce ID as string
            data = pd.read_excel(file_path, dtype={"ID": str})
            # Find the data for the selected ID
            user_data = data[data['ID'] == str(user_id)].to_dict('records')

            if user_data:
                return user_data[0]  # Return first match as a dictionary
    return {}  # Return empty if no data found


@app.callback(
    [Output('input-id', 'value'), Output('input-age', 'value'),
     Output('input-gender', 'value'), Output('input-admission-date', 'date'),
     Output('input-primary-diagnosis', 'value')],
    Input('url', 'pathname'),
    State('stored-user-data', 'data')
)
def prefill_section1(pathname, section1_data):
    if pathname == '/section1' and section1_data:
        return (section1_data.get("ID"), section1_data.get("Age"),
                section1_data.get("Gender"), section1_data.get("Admission Date"),
                section1_data.get("Primary Diagnosis"))
    return dash.no_update



    
@app.callback(
    [Output("input-fever", "value"), Output("input-cough", "value"),
     Output("input-dyspnea", "value")],
    Input("url", "pathname"),
    State("stored-user-data", "data")
)
def prefill_section2(pathname, data):
    # Prefill only when navigating to Section 2
    if pathname == '/section2' and data:
        fever = [data.get("Fever", "")] if data.get("Fever") else []
        cough = [data.get("Cough", "")] if data.get("Cough") else []
        dyspnea = [data.get("Dyspnea", "")] if data.get("Dyspnea") else []
        return fever, cough, dyspnea

    # Use dash.no_update to prevent clearing existing values
    return dash.no_update, dash.no_update, dash.no_update


@app.callback(
    [Output("bal-performed", "value"),
     Output("bal-date", "date"),
     Output("randomization-group", "value"),  # Corrected ID here
     Output("biofire-results", "value"),
     Output("culture-results", "value"),
     Output("resistance-genes", "value")],
    Input("url", "pathname"),
    State("stored-user-data", "data")
)
def prefill_section3(pathname, data):
    # Prefill only when navigating to Section 3
    if pathname == '/section3' and data:
        bal_performed = data.get("BAL Performed", "No")  # Default to "No" if not set
        bal_date = data.get("BAL Date", "")
        random_group = data.get("Randomization Group", "")
        biofire_results = data.get("BioFire Panel Results", "")
        culture_results = data.get("Culture Results", "")
        resistance_genes = data.get("Resistance Genes Detected", "")
        
        return bal_performed, bal_date, random_group, biofire_results, culture_results, resistance_genes
    
    # Use dash.no_update to prevent clearing existing values
    return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True, port=223)


# In[ ]:




